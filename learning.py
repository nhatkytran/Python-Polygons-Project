# https://www.calculatorsoup.com/calculators/geometry-plane/polygon.php
# https://stackoverflow.com/questions/59812398/is-there-a-reduce-function-for-python-in-which-we-can-access-index-of-current-it#:~:text=Explanation%3A,the%20index%20to%20the%20callback.

import math
from functools import reduce

class Polygon:
  def __init__(self, edge, circumradius):
    if edge < 3:
      raise ValueError(f'{self.__class__.__name__} must have at least 3 edges (sides)')
    if circumradius < 0:
      raise ValueError('Circumradius must have to be greater than 0')
    self._n = edge
    self._R = circumradius
    self._pt = self._n, self._R

  @property
  def edges(self):
    return self._n

  @property
  def vertices(self):
    return self._n

  @property
  def circumradius(self):
    return self._R
      
  @property
  def interior_angle(self):
    return 180 * (self._n - 2) / self._n

  @property
  def edge_length(self):
    return 2 * self._R * math.sin(math.pi / self._n)

  @property
  def apothem(self):
    return round(self._R * math.cos(math.pi / self._n), 2)

  @property
  def area(self):
    return self._n * self.edge_length * self.apothem / 2

  @property
  def perimeter(self):
    return self._n * self.edge_length

  @property
  def ratio(self):
    return self.area / self.perimeter

  @property
  def details(self):
    return f'''{self.__class__.__name__}(edges(n)={self.edges},
        vertices(n)={self.vertices},
        circumradius(R)={self.circumradius},
        interior_angle={self.interior_angle},
        edge_length(s)={self.edge_length},
        apothem(a)={self.apothem})
        area(A)={self.area}
        perimeter(P)={self.perimeter}'''

  def __repr__(self):
    return f'{self.__class__.__name__}(edge={self._n}, circumradius={self._R})'

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      raise TypeError(f'Only compare {self.__class__.__name__} instances')
    return (self.vertices == other.vertices
            and self.circumradius == other.circumradius)

  def __gt__(self, other):
    if not isinstance(other, self.__class__):
      raise TypeError(f'Only compare {self.__class__.__name__} instances')
    return self.vertices > other.vertices

  def __getitem__(self, value):
    return self._pt[value]


# class Polygons:
#   def __init__(self, *plgs):
#     max_edge = 8
#     common_circumradius = 10
#     self.polygons = []

#     for edge, circumradius in plgs:
#       if edge > max_edge:
#         raise ValueError(f'Edge must have to be less than {max_edge}')
#       if circumradius != common_circumradius:
#         raise ValueError(f'Circumradius must have to be {common_circumradius}')
#       self.polygons.append(Polygon(edge, circumradius))

#   def __repr__(self):
#     string_polygons = ', '.join([str(item) for item in self.polygons])
#     return f'{self.__class__.__name__}({string_polygons})'

#   @property
#   def efficiency(self):
#     if self.polygons:

#       index_of_max = 0
#       def func_reduce_efficiency(acc, cur):
#         nonlocal index_of_max

#         if acc[1].ratio < cur[1].ratio:
#           index_of_max = cur[0]
#           return cur
#         return acc

#       reduce(func_reduce_efficiency, enumerate(self.polygons))

#       return self.polygons[index_of_max]
#     else:
#       return f'Emplty {self.__class__.__name__}'

#   def __len__(self):
#     return len(self.polygons)

#   def __getitem__(self, value):
#     return self.polygons[value]

# POLYGONS as the instruction
# ---------------------------

class Polygons:
  def __init__(self, m, R):
    if m < 3:
      raise ValueError(f'Polygons must have at least 3 edges (sides)')
    if R < 0:
      raise ValueError('Circumradius must have to be greater than 0')
    self._m = m
    self._R = R
    self._polygons = [Polygon(i, R) for i in range(3, m + 1)]

  def __repr__(self):
    return f'{self.__class__.__name__}(m={self._m}, R={self._R})'

  @property
  def details(self):
    return self._polygons

  def __len__(self):
    return len(self._polygons)

  @property
  def efficiency(self):
    [efficiency, *_] = sorted(self._polygons, key=lambda polygon: polygon.ratio, reverse=True)
    return efficiency

  def __getitem__(self, value):
    return self._polygons[value]
