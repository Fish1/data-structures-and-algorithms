from typing import Self, List

class Vertex:
    def __init__(self, value: str):
        self.adjacent_vertices: List[Self] = []
        self.value = value

    def add_adjacent_verticies(self, vertices: list[Self]):
        for vertex in vertices:
            self.add_adjacent_vertex(vertex)

    def add_adjacent_vertex(self, vertex: Self):
        if vertex not in self.adjacent_vertices:
            self.adjacent_vertices.append(vertex)
            vertex.add_adjacent_vertex(self)


def search_depth(value: str, vertex: Vertex, visited: List[Vertex] = []) -> Vertex | None:
    visited.append(vertex)
    print(vertex.value)
    if vertex.value == value:
        return vertex
    else:
        for adjacent_vertex in vertex.adjacent_vertices:
            if adjacent_vertex in visited:
                continue
            found = search_depth(value, adjacent_vertex, visited)
            if found is not None:
                return found
        return None

def search_breadth(value: str, vertex: Vertex) -> Vertex | None:
    visited = [vertex]
    queue = [vertex]

    while len(queue) > 0:
        current_vertex = queue.pop(0)
        print(current_vertex.value)
        if current_vertex.value == value:
            return current_vertex
        for next_vertex in current_vertex.adjacent_vertices:
            if next_vertex in visited:
                continue
            else:
                visited.append(next_vertex)
                queue.append(next_vertex)



alice = Vertex("alice")
bob = Vertex("bob")
fred = Vertex("fred")
helen = Vertex("helen")
candy = Vertex("candy")
derek = Vertex("derek")
gina = Vertex("gina")
irena = Vertex("irena")
elaine = Vertex("elaine")

alice.add_adjacent_verticies([bob, candy, derek, elaine])
bob.add_adjacent_verticies([fred, alice])
fred.add_adjacent_verticies([helen, bob])
helen.add_adjacent_verticies([fred, candy])
candy.add_adjacent_verticies([helen, alice])

derek.add_adjacent_verticies([elaine, gina, alice])
elaine.add_adjacent_verticies([derek, alice])
gina.add_adjacent_verticies([derek, irena])
irena.add_adjacent_verticies([gina])


search = "irena"

print("Depth First...")
y = search_depth(search, alice)
if y is not None:
    print(y.value)

print("\nBreadth First...")

z = search_breadth(search, alice)
if z is not None:
    print(z.value)

