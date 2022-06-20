import cv2
import numpy as np
from numpy.typing import ArrayLike
from core.domain.services.image_service import ImageService
from core.infra.scene_objects.corners import Corners
from core.infra.scene_objects.offset import Offset


class DefaultImageService(ImageService):

    def applyMaskFromCorners(self, frame: ArrayLike, region_of_interest: Corners) -> ArrayLike: 
        mask = np.zeros(frame.shape[:2], dtype="uint8")
        top_left = region_of_interest.top_left
        bottom_right = region_of_interest.bottom_right
        cv2.rectangle(mask, top_left.to_tuple(), bottom_right.to_tuple(), 255, -1)
        masked = cv2.bitwise_and(frame, frame, mask=mask)

        return masked
        
    def drawCircleInFrame(self, frame: ArrayLike, center: Offset) -> ArrayLike:
        color = [0, 0, 255]
        radius = 10
        thickness = -1
        result = frame.copy()
        cv2.circle(result, list(map(int, center.to_tuple())), radius, color, thickness)

        return result

    def drawRectangleInFrame(self, frame: ArrayLike, corners: Corners) -> ArrayLike:
        color = [255, 0, 0]   
        thickness = 8
        result = frame.copy()
        cv2.rectangle(result, list(map(int, corners.top_left.to_tuple())), list(map(int, corners.bottom_right.to_tuple())), color, thickness)

        return result