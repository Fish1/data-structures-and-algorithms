import random

class Heap:
    def __init__(self, head: int) -> None:
        self.data = [head]

    def print(self) -> None:
        print(self.data)

    def root(self) -> int:
        return self.data[0]

    def last(self) -> int:
        return self.data[len(self.data) - 1]

    def left_child(self, index: int) -> int | None:
        if self.left_child_index(index) >= len(self.data):
            return None
        return self.data[self.left_child_index(index)]

    def left_child_index(self, index: int) -> int:
        return 2 * index + 1

    def right_child(self, index: int) -> int | None:
        if self.right_child_index(index) >= len(self.data):
            return None
        return self.data[self.right_child_index(index)]

    def right_child_index(self, index: int) -> int:
        return 2 * index + 2

    def parent(self, index: int) -> int:
        return self.data[self.parent_index(index)]

    def parent_index(self, index: int) -> int:
        return (index - 1) // 2

    def append(self, value: int) -> None:
        self.data.append(value)
        current_index = len(self.data) - 1
        parent_index = self.parent_index(current_index)

        while current_index > 0 and self.data[current_index] > self.data[parent_index]:
            self.data[parent_index], self.data[current_index] = self.data[current_index], self.data[parent_index]
            current_index = parent_index
            parent_index = self.parent_index(current_index)


    def pop(self) -> int:
        head = self.data[0]
        self.data[0] = self.data.pop()
        current_index = 0

        current = self.data[current_index]
        left_child = self.left_child(current_index)
        left_child_index = self.left_child_index(current_index)
        right_child = self.right_child(current_index)
        right_child_index = self.right_child_index(current_index)

        while (left_child and current < left_child) or (right_child and current < right_child):
            if left_child and right_child and left_child > right_child:
                self.data[current_index], self.data[left_child_index] = self.data[left_child_index], self.data[current_index]
                current_index = self.left_child_index(current_index)
            elif left_child and right_child and left_child < right_child:
                self.data[current_index], self.data[right_child_index] = self.data[right_child_index], self.data[current_index]
                current_index = self.right_child_index(current_index)
            elif left_child and not right_child:
                self.data[current_index], self.data[left_child_index] = self.data[left_child_index], self.data[current_index]
                current_index = self.left_child_index(current_index)

            current = self.data[current_index]
            left_child = self.left_child(current_index)
            left_child_index = self.left_child_index(current_index)
            right_child = self.right_child(current_index)
            right_child_index = self.right_child_index(current_index)

        return head




myheap = Heap(34)

# randomly insert some values

count = 50

for i in range(count):
    myheap.append(int(random.random() * 100))

myheap.print()

for i in range(count):
    print(myheap.pop())
