class Stack:
    stack = []

    def add(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[len(self.stack) - 1]

    def print(self):
        print(self.stack)


thestack = Stack()

mystring = "Hello, World!"

for c in mystring:
    thestack.add(c)

mystring = ""
while thestack.peek() != None:
    c = thestack.pop()
    mystring += c

print(mystring)
