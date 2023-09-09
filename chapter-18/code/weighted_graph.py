from ctypes import wstring_at
from typing_extensions import Self

class Vertex:
    def __init__(self, value: str):
        self.adjacent_vertices: dict[Self, int] = {}
        self.value = value

    def add_adjacent_vertex(self, vertex: Self, weight: int):
        self.adjacent_vertices[vertex] = weight


atlanta = Vertex("Atlanta")
boston = Vertex("Boston")
chicago = Vertex("Chicago")
denver = Vertex("Denver")
el_paso = Vertex("El Paso")

atlanta.add_adjacent_vertex(boston, 100)
atlanta.add_adjacent_vertex(denver, 160)

boston.add_adjacent_vertex(chicago, 120)
boston.add_adjacent_vertex(denver, 180)

chicago.add_adjacent_vertex(el_paso, 80)

denver.add_adjacent_vertex(chicago, 40)
denver.add_adjacent_vertex(el_paso, 140)

el_paso.add_adjacent_vertex(boston, 100)


