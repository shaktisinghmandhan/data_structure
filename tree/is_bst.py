# A program to check if a binary tree is BST or not
# A binary search tree (BST) is a node based binary tree data structure which has the following properties.
# • The left subtree of a node contains only nodes with keys less than the node’s key.
# • The right subtree of a node contains only nodes with keys greater than the node’s key.
# • Both the left and right subtrees must also be binary search trees.

from node import Node


# travelling in inorder fashion
def is_bst(root, previous_node):
    if root:
        if is_bst(root.left, previous_node):
            return False

        if previous_node and root.data < previous_node.data:
            return False
        previous_node = root

        return is_bst(root.right, previous_node)
    return True


if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)

    if is_bst(root, None):
        print "Is BST"
    else:
        print "Not a BST"
