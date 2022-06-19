from abc import ABC
from core.domain.usecases.apply_mask_from_corners import ApplyMaskFromCorners


class ImageService(ApplyMaskFromCorners, ABC):
    pass