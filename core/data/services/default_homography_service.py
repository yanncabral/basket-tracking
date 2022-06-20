import cv2
import numpy as np
from core.domain.entities.ball import Ball
from core.domain.entities.court import Court
from core.domain.entities.player import Player
from core.domain.entities.scene import Scene
from core.domain.services.homography_service import HomographyService
from core.infra.scene_objects.corners import Corners
from core.infra.scene_objects.offset import Offset

def _apply_homography_in_frame(H, pts) :
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
        

        return tpts


class DefaultHomographyService(HomographyService):

    def _apply_homography_to_offset(self, h, offset: Offset) -> Offset:
        x = np.array([offset.x])
        y = np.array([offset.y])
        pos = _apply_homography_in_frame(h, np.array([x, y]))

        return Offset(x=pos[0][0], y=pos[1][0])

    def _apply_homography_to_corners(self, h, corners: Corners) -> Corners:
        return Corners(
            bottom_left=self._apply_homography_to_offset(h=h, offset=corners.bottom_left),
            bottom_right=self._apply_homography_to_offset(h=h, offset=corners.bottom_right),
            top_left=self._apply_homography_to_offset(h=h, offset=corners.top_left),
            top_right=self._apply_homography_to_offset(h=h, offset=corners.top_right),
        )

    def applyHomography(self, scene: Scene, from_corners: Corners, to_corners: Corners) -> Scene:
        # points_from_topdown = np.array([
        #     [40,420],  # RIGHT BOTTOM
        #     [40,42],  # LEFT BOTTOM
        #     [752, 42],     # TOP LEFT (7 o'clock)
        #     [752,  420]   # TOP RIGHT  (4 o'clock)
        #     ])  

        to_points = np.array([
            list(to_corners.bottom_right.to_tuple()),  # RIGHT BOTTOM
            list(to_corners.bottom_left.to_tuple()),  # LEFT BOTTOM
            list(to_corners.top_left.to_tuple()),     # TOP LEFT (7 o'clock)
            list(to_corners.top_right.to_tuple())   # TOP RIGHT  (4 o'clock)
            ])  

        # from_points = np.array([
        #     list(from_corners.bottom_right.to_tuple()),  # RIGHT BOTTOM
        #     list(from_corners.bottom_left.to_tuple()),  # LEFT BOTTOM
        #     list(from_corners.top_left.to_tuple()),     # TOP LEFT (7 o'clock)
        #     list(from_corners.top_right.to_tuple())   # TOP RIGHT  (4 o'clock)
        #     ])  

        # h, status = cv2.findHomography(points_from_camera_video, points_from_topdown)
        # print("treta:", points_from_topdown, np.array(to_corners.to_tuple()))
        h, _ = cv2.findHomography(np.array(from_corners.to_tuple()), to_points)
        

        new_players = []
        # dst_points = []
        for player in scene.players:
            new_player_pos = self._apply_homography_to_offset(h=h, offset=player.position)
            new_player_corners = self._apply_homography_to_corners(h=h, corners=player.corners)
            new_player = Player(corners=new_player_corners, position=new_player_pos, name=player.name)
            new_players.append(new_player)

        new_ball = Ball(position=self._apply_homography_to_offset(h=h, offset=scene.ball.position))
        new_court = Court(corners=self._apply_homography_to_corners(h=h, corners=scene.court.corners))

        return Scene(players=new_players, ball=new_ball, court=new_court)

