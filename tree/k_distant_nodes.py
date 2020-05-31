from node import Node


def print_k_distant_node_down(root, k):
    if root is None or k < 0:
        return

    if k == 0:
        print root.data
        return
    print_k_distant_node_down(root.left, k-1)
    print_k_distant_node_down(root.right, k-1)


# Prints all nodes at distance k from a given target node
# The k distant nodes may be upward or downward. This function
# returns distance of root from target node, it returns -1
# if target node is not present in tree rooted with root
def print_k_distant_node(root, target, k):
    if root is None:
        return -1

    if root.data == target.data:
        print_k_distant_node_down(root, k)
        return 0

    distance_left = print_k_distant_node(root.left, target, k)

    if distance_left != -1:

        if distance_left + 1 == k:
            print root.data

        else:
            # Note: that the right child is 2 edges away from
            # left chlid
            print_k_distant_node_down(root.right, k - distance_left - 2)

        return 1 + distance_left

    distance_right = print_k_distant_node(root.right, target, k)

    if distance_right != -1:

        if distance_right + 1 == k:
            print root.data

        else:
            # Note: that the right child is 2 edges away from
            # right chlid
            print_k_distant_node_down(root.right, k - distance_right - 2)

        return 1 + distance_right

    # If target was neither present in left nor in right subtree
    return -1


if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    target = root.left.right
    print_k_distant_node(root, target, 2)

# Time Complexity: At first look the time complexity looks more than O(n), but if we take a closer look,
# we can observe that no node is traversed more than twice. Therefore the time complexity is O(n).
