import dataclasses
import typing
import numpy

class Point:
  def __init__(self, x: float, y: float, z: float):
    self.x: float = x
    self.y: float = y
    self.z: float = z
  def tuple(self) -> tuple:
    return tuple((self.x, self.y, self.z))
  def numpyArray(self) -> numpy.array:
    return numpy.array
  @classmethod
  def parse_tuple(cls, point_tuple) -> "Point":
    return Point(point_tuple[0], point_tuple[1], point_tuple[2])
  @classmethod
  def parse_numpyArray(cls, point_numpyArray) -> "Point":
    return Point(point_numpyArray[0], point_numpyArray[1], point_numpyArray[2])

class Range:
  def __init__(self, min: float, max: float):
    self.min: float = min
    self.max: float = max
  def include(self, value: float) -> bool:
    """Check whether the value falls within the range
    ### Parameters
    - `value` (float): Detection value
    ### Returns
    - `bool`: `self.min <= value <= self.max`
    """
    return self.min <= value <= self.max

class Area:
  def __init__(self, x: Range, y: Range, z: Range):
    self.x: Range = x
    self.y: Range = y
    self.z: Range = z
  def include(self, point: Point) -> bool:
    """Check whether the point falls within the range
    ### Parameters
    - `point` (Point): Detection point
    ### Returns
    - `bool`: `self.min <= value <= self.max`
    """
    return self.x.include(point.x) and self.y.include(point.y) and self.z.include(point.z)

class Areas:
  def __init__(self, name: str = "", areas: list[Area] = list()):
    self.name = name
    self.areas = areas
  def include(self, point: Point) -> bool:
    for area in self.areas:
      if area.x.min <= point.x <= area.x.max and area.y.min <= point.y <= area.y.max and area.z.min <= point.z <= area.z.max:
        return True
    return False