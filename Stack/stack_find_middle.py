class Node:

    def __init__(self,item) -> None:
        self.prev = None
        self.data = item
        self.next = None

class Stack:

    def __init__(self) -> None:
        self.head = None
        self.count = 0
        self.middle = None

    def push(self, item):
        # create a new node
        new_node = Node(item)
        
        # add a node in the stack
        if self.head == None:
            self.head = new_node
        else:
            self.head.next = new_node
            new_node.prev = self.head
            self.head = new_node

        # increase counter
        self.count += 1

        # add a middle node
        if self.count == 1:
            self.middle = new_node
        elif (self.count % 2) != 0:
            self.middle = self.middle.next

    def pop(self):
        # remove a node
        if self.count == 0:
            return -1

        self.head = self.head.prev
        if self.head != None:
            self.head.next = None
        self.count -= 1

        # change a middle element
        if self.count == 0:
            self.middle = None
        else:
            if (self.count % 2) == 0:
                self.middle = self.middle.prev


    def find_middle(self):
        # find a middle element
        if self.count == 0:
            return None
        else:
            return self.middle.data

    def delete_middle(self):
        # delete a midddle element
        if self.count == 0:
            return None
        
        self.count -= 1
        if self.middle.prev != None:
            self.middle.prev.next = self.middle.next
        if self.middle.next != None:
            self.middle.next.prev = self.middle.prev
        
        if (self.count % 2) == 0:
            self.middle = self.middle.prev
        else:
            self.middle = self.middle.next

        

if __name__ == "__main__":
    new_stack = Stack()
    new_stack.push(1)
    new_stack.push(2)
    new_stack.push(3)
    new_stack.push(4)
    new_stack.push(5)
    new_stack.pop()
    new_stack.delete_middle()
    print(new_stack.find_middle())