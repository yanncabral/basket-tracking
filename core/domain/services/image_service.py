from abc import ABC

from core.domain.usecases.images.apply_mask_from_corners import ApplyMaskFromCorners
from core.domain.usecases.images.draw_circle_in_frame import DrawCircleInFrame
from core.domain.usecases.images.draw_rectangle_in_frame import DrawRectangleInFrame

class ImageService(ApplyMaskFromCorners, DrawCircleInFrame, DrawRectangleInFrame, ABC):
    pass