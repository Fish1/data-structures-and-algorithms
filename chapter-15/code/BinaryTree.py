from typing_extensions import Self
from typing import Tuple

class Node:
    def __init__(self, value: int, left: Self | None = None, right: Self | None = None):
        self.value = value
        self.left = left
        self.right = right


def search(search_value: int, node: Node | None):
    if node is None or node.value == search_value:
        return node
    if search_value > node.value:
        return search(search_value, node.right)
    if search_value < node.value:
        return search(search_value, node.left)

def insert(insert_value: int, node: Node):

    if insert_value < node.value:
        if node.left is None:
            node.left = Node(insert_value)
        else:
            insert(insert_value, node.left)

    elif insert_value > node.value:
        if node.right is None:
            node.right = Node(insert_value)
        else:
            insert(insert_value, node.right)

def delete(delete_value: int, node: Node | None):
    if node is None:
        return

    if delete_value > node.value:
        node.right = delete(delete_value, node.right)
        return node

    elif delete_value < node.value:
        node.left = delete(delete_value, node.left)
        return node

    elif delete_value == node.value:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        else:
            node.right = lift(node.right, node)
            return node

def lift(node, node_to_delete):
    if node.left:
        node.left = lift(node.left, node_to_delete)
        return node
    else:
        return node.right

def greatest(node: Node) -> int:
    if node.left is None and node.right is None:
        return node.value

    elif node.left is None and node.right is not None:
        return max(node.value, greatest(node.right))

    elif node.left is not None and node.right is None:
        return max(node.value, greatest(node.left))

    else:
        left = greatest(node.left)
        right = greatest(node.right)
        return max(node.value, left, right)


def print_tree(node: Node | None):
    if node is None:
        return
    print_tree(node.left)
    print(node.value)
    print_tree(node.right)

left = Node(25)
right = Node(75)
head = Node(50, left, right)

insert(27, head)
insert(23, head)
insert(44, head)
insert(99, head)

print_tree(head)

print("")

print(greatest(head))
