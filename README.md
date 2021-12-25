# quat2eul



![image](https://readthedocs.org/projects/|package|/badge/?version=latest)

<!-- :target: https://|package|.readthedocs.io/en/latest/?badge=latest
:alt: Documentation Status -->


![image](https://codecov.io/gh/ppecheux/|package|/branch/main/graph/badge.svg)

<!-- :target: https://codecov.io/gh/ppecheux/|package| -->
Provides function to convert quaternions to Euler angles


### exception quat2eul.SingularityError()
Raised when quaternion to Euler is impossible
due to singularity


### quat2eul.quat2eul(sequence: quat2eul.sequence.Sequence, quaternions: Iterator[float])
Returns the Euler angles for the input quaternions according to the rotation sequence
:param sequence: sequence of the three axes of rotation
:type sequence: Sequence
:param quaternions: list of quaternions
:type quaternions: Iterator


* **Returns**

    euler angles



* **Return type**

    Tuple[float]


### Examples

```python
>>> quat2eul(Sequence.XYX, [0.0, 0.1, 0.0, 0.0])
(,,,)
```

<!-- toctree::.. image:: https://readthedocs.org/projects/ur/badge/?version=latest

:maxdepth: 2
:caption: Contents: -->
# Indices and tables


* Index


* Module Index


* Search Page
