from linkedlist import LinkedList

def reverse(head, k):
    # create n linked list of k elements
    l_list = []
    m = 0
    while(head):
        i = k
        l_list.append(LinkedList())
        while(i!=0) and (head):
            l_list[m].push(head.data)
            head = head.next            
            i = i - 1
        m = m + 1 

    # create new linked list with appending elements by traversing n linked list
    r_list = LinkedList()
    for n in range(len(l_list)):
        while(l_list[n].head):
            r_list.append(data=l_list[n].head.data)
            l_list[n].head = l_list[n].head.next

    return(r_list.head)


if __name__ == "__main__":

    linked_list = LinkedList()

    for i in range(1,11,1):
        linked_list.push(i)

    print(linked_list)

    reverse_head = reverse(linked_list.head, 4)

    while(reverse_head):
        print(reverse_head.data,end=" ")
        reverse_head = reverse_head.next