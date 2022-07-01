from linkedlist import LinkedList

if __name__ == "__main__":

    linked_list = LinkedList()

    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    linked_list.push(4)
    linked_list.push(5)
    linked_list.push(6)
    linked_list.push(7)

    print(linked_list)

    linked_list.reverse()

    print(linked_list)