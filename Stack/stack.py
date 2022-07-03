from inspect import stack


class Stack:

    def __init__(self) -> None:
        self.stack = []

    def append(self,value):
        self.stack.append(value)

    def pop(self):
        self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def __str__(self) -> str:
        return str(self.stack)