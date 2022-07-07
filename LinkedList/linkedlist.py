class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def push(self,data):
        temp = self.head
        self.head = Node(data)
        self.head.next =  temp

    def insert(self,prev,data):
        if prev is None:
            return

        temp = prev.next
        prev.next = Node(data)
        prev.next.next = temp


    def append(self,data):
        new_node = Node(data)
        
        if self.head == None:
            self.head = new_node
            return

        last_node = self.head
        while(last_node.next):
            last_node = last_node.next

        last_node.next = new_node

    def delete(self,key):
        
        temp = self.head

        if temp != None:
            if temp.data == key:
                self.head = temp.next
                return

        while(temp.next):
            if temp.next.data == key:
                temp.next = temp.next.next
                return
            temp = temp.next

    def reverse(self):
        prev = None
        while(self.head != None):
            temp = self.head.next
            self.head.next = prev
            prev = self.head
            self.head = temp
        self.head = prev

    def __str__(self) -> str:
        temp = self.head
        node_list = ""
        while(temp):
            node_list += str(temp.data) + " "
            temp = temp.next

        return node_list