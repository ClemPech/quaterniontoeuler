"""Provides function to convert quaternions to Euler angles"""
from math import pi, acos, atan2, asin
from typing import Iterator, Tuple
from quat2eul.sequence import Sequence


def quat2eul(sequence: Sequence, quaternions: Iterator[float]) -> Tuple[float]:
    """Returns the Euler angles for the input quaternions according to the rotation sequence
    Args:
        sequence (Sequence): sequence of the three axes of rotation
        quaternions (Iterator): list of quaternions

    Returns:
        Tuple[float]: euler angles

    Examples:
        >>> quat2eul(Sequence.XYX, [0.0, 0.1, 0.0, 0.0])
        (,,,)
    """
    q0, q1, q2, q3 = quaternions

    psi, theta, phi = {
        Sequence.XYX: (
            atan2((q1 * q2 + q3 * q0), (q2 * q0 - q1 * q3)),
            acos(q0 * q0 + q1 * q1 - q2 * q2 - q3 * q3),
            atan2((q1 * q2 - q3 * q0), (q1 * q3 + q2 * q0)),
        ),
        Sequence.YZY: (
            atan2((q1 * q0 + q2 * q3), (q3 * q0 - q1 * q2)),
            acos(q0 * q0 - q1 * q1 + q2 * q2 - q3 * q3),
            atan2((q2 * q3 - q1 * q0), (q1 * q2 + q3 * q0)),
        ),
        Sequence.ZXZ: (
            atan2((q1 * q3 + q2 * q0), (q1 * q0 - q2 * q3)),
            acos(q0 * q0 - q1 * q1 - q2 * q2 + q3 * q3),
            atan2((q1 * q3 - q2 * q0), (q1 * q0 + q2 * q3)),
        ),
        Sequence.XZX: (
            atan2((q1 * q3 - q2 * q0), (q1 * q2 + q3 * q0)),
            acos(q0 * q0 + q1 * q1 - q2 * q2 - q3 * q3),
            atan2((q1 * q3 + q2 * q0), (q3 * q0 - q1 * q2)),
        ),
        Sequence.YXY: (
            atan2((q1 * q2 - q3 * q0), (q1 * q0 + q2 * q3)),
            acos(q0 * q0 - q1 * q1 + q2 * q2 - q3 * q3),
            atan2((q1 * q2 + q3 * q0), (q1 * q0 - q2 * q3)),
        ),
        Sequence.ZYZ: (
            atan2((q2 * q3 - q1 * q0), (q1 * q3 + q2 * q0)),
            acos(q0 * q0 - q1 * q1 - q2 * q2 + q3 * q3),
            atan2((q1 * q0 + q2 * q3), (q2 * q0 - q1 * q3)),
        ),
        Sequence.XYZ: (
            atan2(
                2 * (q1 * q0 - q2 * q3),
                (q0 * q0 - q1 * q1 - q2 * q2 + q3 * q3),
            ),
            asin(2 * (q1 * q3 + q2 * q0)),
            atan2(
                2 * (q3 * q0 - q1 * q2),
                (q0 * q0 + q1 * q1 - q2 * q2 - q3 * q3),
            ),
        ),
        Sequence.YZX: (
            atan2(
                2 * (q2 * q0 - q1 * q3),
                (q0 * q0 + q1 * q1 - q2 * q2 - q3 * q3),
            ),
            asin(2 * (q1 * q2 + q3 * q0)),
            atan2(
                2 * (q1 * q0 - q3 * q2),
                (q0 * q0 - q1 * q1 + q2 * q2 - q3 * q3),
            ),
        ),
        Sequence.ZXY: (
            atan2(
                2 * (q3 * q0 - q1 * q2),
                (q0 * q0 - q1 * q1 + q2 * q2 - q3 * q3),
            ),
            asin(2 * (q1 * q0 + q2 * q3)),
            atan2(
                2 * (q2 * q0 - q3 * q1),
                (q0 * q0 - q1 * q1 - q2 * q2 + q3 * q3),
            ),
        ),
        Sequence.XZY: (
            atan2(
                2 * (q1 * q0 + q2 * q3),
                (q0 * q0 - q1 * q1 + q2 * q2 - q3 * q3),
            ),
            asin(2 * (q3 * q0 - q1 * q2)),
            atan2(
                2 * (q1 * q3 + q2 * q0),
                (q0 * q0 + q1 * q1 - q2 * q2 - q3 * q3),
            ),
        ),
        Sequence.YXZ: (
            atan2(
                2 * (q1 * q3 + q2 * q0),
                (q0 * q0 - q1 * q1 - q2 * q2 + q3 * q3),
            ),
            asin(2 * (q1 * q0 - q2 * q3)),
            atan2(
                2 * (q1 * q2 + q3 * q0),
                (q0 * q0 - q1 * q1 + q2 * q2 - q3 * q3),
            ),
        ),
        Sequence.ZYX: (
            atan2(
                2 * (q1 * q2 + q3 * q0),
                (q0 * q0 + q1 * q1 - q2 * q2 - q3 * q3),
            ),
            asin(2 * (q2 * q0 - q1 * q3)),
            atan2(
                2 * (q1 * q0 + q3 * q2),
                (q0 * q0 - q1 * q1 - q2 * q2 + q3 * q3),
            ),
        ),
    }[sequence]

    if sequence.singularity_group == 1 and pi - theta < pi / 180:
        raise SingularityError(f"{pi-theta} || {theta} < rad")
    if sequence.singularity_group == 2 and abs(theta - pi / 2) < pi / 180:
        raise SingularityError(f"{abs(theta-pi/2)} < {pi/180} rad")

    return psi, theta, phi


class SingularityError(Exception):
    """Raised when quaternion to Euler is impossible
    due to singularity
    """
