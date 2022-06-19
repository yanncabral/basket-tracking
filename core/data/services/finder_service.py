import cv2
from PIL import ImageEnhance, Image
import numpy as np
import imutils

from typing import List, Optional
from numpy.typing import ArrayLike


from detectron2.utils.logger import setup_logger

from core.domain.entities.ball import Ball
from core.domain.entities.player import Player
from core.domain.services.finder_service import FinderService
from core.infra.scene_objects.corners import Corners

setup_logger()


# import some common detectron2 utilities
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog, DatasetCatalog

_ballColorLower = (5, 65, 115) 
_ballColorUpper = (11, 105, 155)

points_from_topdown = np.array([
      [40,420],  # RIGHT BOTTOM
      [40,42],  # LEFT BOTTOM
      [752, 42],     # TOP LEFT (7 o'clock)
      [752,  420]   # TOP RIGHT  (4 o'clock)
    ])  

points_from_camera = np.array(sorted([[16, 752], [1903, 716], [227, 477], [1641, 456]]))

class DefaultFinderService(FinderService):

    def findBall(self, frame: ArrayLike) -> Optional[Ball]:
        original_frame = frame
        frame = np.array(ImageEnhance.Contrast(Image.fromarray(original_frame[:,:,::-1])).enhance(0.5))[:, :, ::-1]

        blurred = cv2.GaussianBlur(frame, (1, 1), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

        # TODO: botar isso numa class de tratamento de imagem (?)
        # construct a mask for the color, then perform a series of dilations and erosions to remove any small blobs left in the mask

        mask = cv2.inRange(hsv, _ballColorLower, _ballColorUpper) # handles the actual localization of the ball
        mask = cv2.erode(mask, None, iterations=1) # erode and dilate to remove small blobs
        mask = cv2.dilate(mask, None, iterations=1)

        # result = original_frame.copy()
        result: Optional[Ball] = None

        contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)

        for contour in sorted(contours, key=cv2.contourArea, reverse=True):
            epsilon = 0.01 * cv2.arcLength(contour,True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            if len(approx) > 6:
                moments = cv2.moments(contour)
                center_x = int(moments['m10'] / moments['m00'])
                center_y = int(moments['m01'] / moments['m00'])
                result = Ball((center_x, center_y))
                break

        return result

    def _apply_homography(self, H, pts) :
        """
        Apply a specified homography H to a set of 2D point coordinates

        Parameters
        ----------
        H : 3x3 array
            matrix describing the transformation

        pts : 2xN array
            2D coordinates of points to transform

        Returns
        -------
        numpy.array (dtype=float)
            2xN array containing the transformed points

        """

        #assert expected dimensions of input
        assert(H.shape==(3,3))
        assert(pts.shape[0]==2)
        assert(pts.shape[1]>=1)

        tpts = np.zeros(pts.shape)
        for i in range(pts.shape[1]):
            u = H[0][0]*pts[0][i] + H[0][1]*pts[1][i] + H[0][2]
            v = H[1][0]*pts[0][i] + H[1][1]*pts[1][i] + H[1][2]
            w = H[2][0]*pts[0][i] + H[2][1]*pts[1][i] + H[2][2]

            x_prime = u/w
            y_prime = v/w

            tpts[0][i] = x_prime
            tpts[1][i] = y_prime
        
        #make sure transformed pts are correct dimension
        assert(tpts.shape[0]==2)
        assert(tpts.shape[1]==pts.shape[1])

        return tpts

    
    def findPlayers(self, frame: ArrayLike) -> Optional[List[Player]]:
        cfg = get_cfg()

        cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"))

        cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5  # set threshold for this model
        cfg.MODEL.WEIGHTS = "detectron2://COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x/137849600/model_final_f10217.pkl"
        cfg.MODEL.DEVICE = 'cpu'
        predictor = DefaultPredictor(cfg)
        
        players_output = predictor(frame)
        instances = players_output["instances"]
        pred_boxes = instances.get("pred_boxes")
        pred_classes = instances.get("pred_classes")

        h, status = cv2.findHomography(points_from_camera, points_from_topdown)

        players = []

        for box, predicted_class in zip(pred_boxes, pred_classes):
            if predicted_class == 0: # 0 is an human
                x1 = int(box[0]) # coordenada x do top left
                y1 = int(box[1]) # coordenada y do top left
                x2 = int(box[2]) # coordenada x do bottom right
                y2 = int(box[3]) # coordenada y do bottom right

                corners = Corners.from_rectangle(x1, y1, x2, y2)

                player = Player.from_corners(corners=corners, name=f"Player {len(players)}")

                players.append(player)

                
                # xc = x1 + int((x2 - x1)/2)
                # player_pos1 = (xc - 1, y2)
                # player_pos2 = (xc + 1, y2 + 1)

                # player_posx = np.array([xc])
                # player_posy = np.array([y2])

                # player_pos = np.array([player_posx, player_posy])
                # new_player_pos = self._apply_homography(h, player_pos)

                # player_to_append = Player(corners=Corners(), position=Position(int(new_player_pos[0][0]), int(new_player_pos[1][0])))
                # players.apppend(player_to_append)

                # # cria o objeto player
                # # pega um metodo que retorne o pezinho dele
                # # passa o pezinho dele
                # players.append(
                #     # Player(
                #     #     name=f"player-{str(len(players))}",
                #     #     position=tuple(float(i[0]) for i in new_player_pos[:2])
                #     #     # position=tuple(new_player_pos[:2])
                #     # )
                # )

        return players
