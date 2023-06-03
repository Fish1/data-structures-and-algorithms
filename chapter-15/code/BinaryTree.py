class Node:
    def __init__(self, value: int, left: Node | None = None, right: Node | None = None):
        self.value = value
        self.left = left
        self.right = right


n1 = Node(25)
n2 = Node(75)
n3 = Node(50, n1, n2)

print(n3)
