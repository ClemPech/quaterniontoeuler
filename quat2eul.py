from typing import Callable, Tuple
import numpy as np
from math import pi
from enum import Enum


class Sequence(Enum):
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
        len(set(self.value())) - 1


def quat2eul(sequence: Sequence, q: Callable) -> Tuple[float]:
    """
    Renvoie les angles d'euler pour les quaternions en entrée (liste q des quaternions) suivant la sequence de rotation (string sequence des trois axes de rotation)
    exemple : quat2eul(Sequence.XYX , [0.0, 0.1, 0.0, 0.0])
    """
    psi = theta = phi = 0

    if Sequence.XYX == sequence:
        psi = np.arctan2((q[1] * q[2] + q[3] * q[0]),
                         (q[2] * q[0] - q[1] * q[3]))
        theta = np.arccos(q[0] * q[0] + q[1] * q[1] -
                          q[2] * q[2] - q[3] * q[3])
        phi = np.arctan2((q[1] * q[2] - q[3] * q[0]),
                         (q[1] * q[3] + q[2] * q[0]))
    elif Sequence.YZY == sequence:
        psi = np.arctan2((q[1] * q[0] + q[2] * q[3]),
                         (q[3] * q[0] - q[1] * q[2]))
        theta = np.arccos(q[0] * q[0] - q[1] * q[1] +
                          q[2] * q[2] - q[3] * q[3])
        phi = np.arctan2((q[2] * q[3] - q[1] * q[0]),
                         (q[1] * q[2] + q[3] * q[0]))
    elif Sequence.ZXZ == sequence:
        psi = np.arctan2((q[1] * q[3] + q[2] * q[0]),
                         (q[1] * q[0] - q[2] * q[3]))
        theta = np.arccos(q[0] * q[0] - q[1] * q[1] -
                          q[2] * q[2] + q[3] * q[3])
        phi = np.arctan2((q[1] * q[3] - q[2] * q[0]),
                         (q[1] * q[0] + q[2] * q[3]))
    elif Sequence.XZX == sequence:
        psi = np.arctan2((q[1] * q[3] - q[2] * q[0]),
                         (q[1] * q[2] + q[3] * q[0]))
        theta = np.arccos(q[0] * q[0] + q[1] * q[1] -
                          q[2] * q[2] - q[3] * q[3])
        phi = np.arctan2((q[1] * q[3] + q[2] * q[0]),
                         (q[3] * q[0] - q[1] * q[2]))
    elif Sequence.YXY == sequence:
        psi = np.arctan2((q[1] * q[2] - q[3] * q[0]),
                         (q[1] * q[0] + q[2] * q[3]))
        theta = np.arccos(q[0] * q[0] - q[1] * q[1] +
                          q[2] * q[2] - q[3] * q[3])
        phi = np.arctan2((q[1] * q[2] + q[3] * q[0]),
                         (q[1] * q[0] - q[2] * q[3]))
    elif Sequence.ZYZ == sequence:
        psi = np.arctan2((q[2] * q[3] - q[1] * q[0]),
                         (q[1] * q[3] + q[2] * q[0]))
        theta = np.arccos(q[0] * q[0] - q[1] * q[1] -
                          q[2] * q[2] + q[3] * q[3])
        phi = np.arctan2((q[1] * q[0] + q[2] * q[3]),
                         (q[2] * q[0] - q[1] * q[3]))
    elif Sequence.XYZ == sequence:
        psi = np.arctan2(2 * (q[1] * q[0] - q[2] * q[3]),
                         (q[0] * q[0] - q[1] * q[1] - q[2] * q[2] + q[3] * q[3]))
        theta = np.arcsin(2 * (q[1] * q[3] + q[2] * q[0]))
        phi = np.arctan2(2 * (q[3] * q[0] - q[1] * q[2]),
                         (q[0] * q[0] + q[1] * q[1] - q[2] * q[2] - q[3] * q[3]))
    elif Sequence.YZX == sequence:
        psi = np.arctan2(2 * (q[2] * q[0] - q[1] * q[3]),
                         (q[0] * q[0] + q[1] * q[1] - q[2] * q[2] - q[3] * q[3]))
        theta = np.arcsin(2 * (q[1] * q[2] + q[3] * q[0]))
        phi = np.arctan2(2 * (q[1] * q[0] - q[3] * q[2]),
                         (q[0] * q[0] - q[1] * q[1] + q[2] * q[2] - q[3] * q[3]))
    elif Sequence.ZXY == sequence:
        psi = np.arctan2(2 * (q[3] * q[0] - q[1] * q[2]),
                         (q[0] * q[0] - q[1] * q[1] + q[2] * q[2] - q[3] * q[3]))
        theta = np.arcsin(2 * (q[1] * q[0] + q[2] * q[3]))
        phi = np.arctan2(2 * (q[2] * q[0] - q[3] * q[1]),
                         (q[0] * q[0] - q[1] * q[1] - q[2] * q[2] + q[3] * q[3]))
    elif Sequence.XZY == sequence:
        psi = np.arctan2(2 * (q[1] * q[0] + q[2] * q[3]),
                         (q[0] * q[0] - q[1] * q[1] + q[2] * q[2] - q[3] * q[3]))
        theta = np.arcsin(2 * (q[3] * q[0] - q[1] * q[2]))
        phi = np.arctan2(2 * (q[1] * q[3] + q[2] * q[0]),
                         (q[0] * q[0] + q[1] * q[1] - q[2] * q[2] - q[3] * q[3]))
    elif Sequence.YXZ == sequence:
        psi = np.arctan2(2 * (q[1] * q[3] + q[2] * q[0]),
                         (q[0] * q[0] - q[1] * q[1] - q[2] * q[2] + q[3] * q[3]))
        theta = np.arcsin(2 * (q[1] * q[0] - q[2] * q[3]))
        phi = np.arctan2(2 * (q[1] * q[2] + q[3] * q[0]),
                         (q[0] * q[0] - q[1] * q[1] + q[2] * q[2] - q[3] * q[3]))
    else:
        psi = np.arctan2(2 * (q[1] * q[2] + q[3] * q[0]),
                         (q[0] * q[0] + q[1] * q[1] - q[2] * q[2] - q[3] * q[3]))
        theta = np.arcsin(2 * (q[2] * q[0] - q[1] * q[3]))
        phi = np.arctan2(2 * (q[1] * q[0] + q[3] * q[2]),
                         (q[0] * q[0] - q[1] * q[1] - q[2] * q[2] + q[3] * q[3]))

    if sequence.singularity_group == 1 and pi-theta < pi/180:
        raise SingularityError(f'{pi-theta} || {theta} < rad')
    elif sequence.singularity_group == 2 and abs(theta-pi/2) < pi/180:
        raise SingularityError(f'{abs(theta-pi/2)} < {pi/180} rad')

    return psi, theta, phi


class SingularityError(Exception):
    pass
