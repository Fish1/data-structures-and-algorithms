
class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: None | Node = None

class LinkedList:
    def __init__(self, first: int):
        self.head = Node(first)
        self.tail = self.head
        self.curr = self.head

    def print(self):
        output = ""
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
        curr_index = 0
        while curr_index < index:
            curr = curr.next
            curr_index += 1
            if curr == None:
                return None
        return curr.data

    # O(N)
    def index_of(self, value):
        curr = self.head
        curr_index = 0
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
    def insert(self, index, data):
        if index < 0:
            return
        newNode = Node(data)
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return

        prev_new = self.head
        prev_index = 0
        while prev_index < index - 1:
            prev_new = prev_new.next
            if prev_new == None:
                return
            prev_index += 1

        newNode.next = prev_new.next
        prev_new.next = newNode

    def delete(self, index):
        if index < 0:
            return

        prev_to_delete = self.head
        prev_to_delete_index = 0
    
        if index == 0:
            if self.head != None:
                self.head = self.head.next
            return

        while prev_to_delete_index < index - 1 and prev_to_delete != None:
            prev_to_delete = prev_to_delete.next
            prev_to_delete_index += 1

        if prev_to_delete == None or prev_to_delete.next == None:
            return

        prev_to_delete.next = prev_to_delete.next.next


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
