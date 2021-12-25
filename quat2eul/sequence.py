"""Sequence of axis"""
from enum import Enum


class Sequence(Enum):
    """All axis sequences"""

    XYX = "xyx"
    YZY = "yzy"
    ZXZ = "zxz"
    XZX = "xzx"
    YXY = "yxy"
    ZYZ = "zyz"
    XYZ = "xyz"
    YZX = "yzx"
    ZXY = "zxy"
    XZY = "xzy"
    YXZ = "yxz"
    ZYX = "zyx"

    @property
    def singularity_group(self) -> int:
        """group to check singularity exception"""
        return len(set(self.value())) - 1
