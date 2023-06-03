import dataclasses

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: Node | None = None

class LinkedList:
    def __init__(self, first: int):
        self.head: Node | None = Node(first)
        self.tail: Node | None = self.head

    def print(self):
        output: str = ""
        curr = self.head
        while curr != None:
            output += str(curr.data) + " -> "
            curr = curr.next
        output += "None"
        print(output)

    # O(N)
    def read(self, index):
        if index < 0:
            return None
        curr = self.head
        curr_index: int = 0
        while curr_index < index:
            curr = curr.next
            curr_index += 1
            if curr == None:
                return None
        return curr.data

    # O(1)
    def last_element(self) -> int:
        return self.tail.data

    # O(N)
    def index_of(self, value):
        curr = self.head
        curr_index: int = 0
        while curr != None:
            if curr.data == value:
                return curr_index
            curr = curr.next
            curr_index += 1
        return

    # O(1) with a tail
    # O(N) without a tail
    def append(self, data):
        self.tail.next = Node(data)
        self.tail = self.tail.next

    # O(N)
    # Best case of O(1) when inserting at beginning
    def insert(self, index, data) -> None:
        if index < 0:
            return None
        newNode: Node = Node(data)
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return None

        prev_new: Node | None = self.head
        prev_index: int = 0
        while prev_index < index - 1:
            prev_new = prev_new.next
            if prev_new == None:
                return None
            prev_index += 1

        newNode.next = prev_new.next
        prev_new.next = newNode
        return None

    def delete(self, index) -> None:
        if index < 0:
            return None

        prev_to_delete = self.head
        prev_to_delete_index: int = 0
    
        if index == 0:
            if self.head != None:
                self.head = self.head.next
            return None

        while prev_to_delete_index < index - 1 and prev_to_delete != None:
            prev_to_delete = prev_to_delete.next
            prev_to_delete_index += 1

        if prev_to_delete == None or prev_to_delete.next == None:
            return None

        prev_to_delete.next = prev_to_delete.next.next
        return None

    def reverse(self) -> None:
        curr = self.head
        while curr != self.tail:
            self.head = curr.next
            curr.next = self.tail.next
            self.tail.next = curr
            curr = self.head
        return None


myLinkedList = LinkedList(3)
myLinkedList.append(1)
myLinkedList.append(5)

print("Read Test")
print(myLinkedList.read(-1))
print(myLinkedList.read(0))
print(myLinkedList.read(1))
print(myLinkedList.read(2))
print(myLinkedList.read(3))

print("")
print("Index Of Test")
print(myLinkedList.index_of(1))
print(myLinkedList.index_of(5))
print(myLinkedList.index_of(3))
print(myLinkedList.index_of(300))

print("")
print("Insert Test")
myLinkedList.print()
myLinkedList.insert(0,8)
myLinkedList.print()

myLinkedList.print()
myLinkedList.insert(3,4)
myLinkedList.print()

print("")
print("Delete Test")
myLinkedList.print()
myLinkedList.delete(6)
myLinkedList.print()

print("")
print("Last Element Test")
print(myLinkedList.last_element())

print("")
print("Reverse Test")
myLinkedList.print()
myLinkedList.reverse()
myLinkedList.print()
