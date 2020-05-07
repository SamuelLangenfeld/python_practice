# Given a binary tree and an integer k, filter the binary tree such that its leaves don't contain the value k. Here are the rules:

# - If a leaf node has a value of k, remove it.
# - If a parent node has a value of k, and all of its children are removed, remove it.


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"value: {self.value}, \
            left: ({self.left.__repr__()}), \
            right: ({self.right.__repr__()})"

# Definitely want recursion right? split -> go left, go right.
# If value = k and no children, remove self


def filter(node, k):
    # Fill this in.
    # I can mutate node. But the parent will always point to node.
    # Basically I can access/modify node's properties using its access points
    # but reassigning node will only change the 'node' reference locally
    if node.left:
        node.left = filter(node.left, k)
    if node.right:
        node.right = filter(node.right, k)
    if node.value == k and node.left is None and node.right is None:
        # filter self
        return None
    return node


#     1
#    / \
#   1   1
#  /   /
# 2   1
n5 = Node(1)
n4 = Node(2)
n3 = Node(1, n5)
n2 = Node(1, n4)
n1 = Node(1, n2, n3)

n3.identifier = 'n3'
n5.identifier = 'n5'

print(n1)
print(filter(n1, 1))
#     1
#    /
#   1
#  /
# 2
# value: 1, left: (value: 1, left: (value: 2, left: (None), right: (None)), right: (None)), right: (None)
