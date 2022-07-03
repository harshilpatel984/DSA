from stack import Stack

if __name__ == "__main__":

    stack = Stack()
    print(stack.isEmpty())
    stack.append(1)
    stack.append(2)
    stack.append(4)
    stack.append(5)
    print(stack.isEmpty())
    print(stack)
    stack.pop()
    print(stack)
    print(stack.peek())
