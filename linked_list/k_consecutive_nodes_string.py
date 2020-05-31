from linked_list import LinkedList


def k_consecutive_nodes_string(head, k):
    result = ""
    j = k
    while head and j >= 0:
        if j == 0:
            j = k
            result += " "
        else:
            j = j - 1
            result += head.data
            head = head.next

    return result


if __name__ == '__main__':
    head = LinkedList('a')
    head.next = LinkedList('b')
    head.next.next = LinkedList('c')
    head.next.next.next = LinkedList('d')
    head.next.next.next.next = LinkedList('e')
    head.next.next.next.next.next = LinkedList('f')
    head.next.next.next.next.next.next = LinkedList('g')
    head.next.next.next.next.next.next.next = LinkedList('h')
    print k_consecutive_nodes_string(head, 3)
