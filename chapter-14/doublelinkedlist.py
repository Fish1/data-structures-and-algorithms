class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: Node | None = None
        self.prev: Node | None = None

class DoubleLinkedList:
    def __init__(self, data: int):
        self.head: Node | None = Node(data)
        self.tail: Node | None = self.head

    def print(self):
        output: str = ""
        curr: Node | None = self.head
        while curr != None:
            output += str(curr.data) + " -> "
            curr = curr.next
        output += "None"
        print(output)
    
    def print_reverse(self):
        output: str = ""
        curr: Node | None = self.tail
        while curr != None:
            output += str(curr.data) + " -> "
            curr = curr.prev
        output += "None"
        print(output)

    def append(self, data: int):
        new_node: Node = Node(data)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = self.tail.next

mylist = DoubleLinkedList(7)
mylist.append(5)
mylist.print()
mylist.print_reverse()
