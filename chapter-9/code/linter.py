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

  
mycode = "(hello[world{}] yooo)"

parens = Stack()

def is_open(c):
    return c == "(" or c == "{" or c == "["

def is_close(c):
    return c == ")" or c == "}" or c == "]"

def matches(a, b):
    return a == "(" and b == ")" or a == ")" and b == "(" or a == "{" and b == "}" or a == "}" and b == "{" or a == "[" and b == "]" or a == "]" and b == "["

for c in mycode:
    if is_close(c) == False and is_open(c) == False:
        continue

    if is_open(c):
        parens.add(c)

    if is_close(c):
        top = parens.pop()
            if matches(top, c):

            

