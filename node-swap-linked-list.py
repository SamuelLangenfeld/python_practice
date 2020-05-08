# Hi, here's your problem today. This problem was recently asked by Twitter:

# Given a linked list, swap the position of the 1st and 2nd node, then swap the position of the 3rd and 4th node etc.

# Here's some starter code:


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value}, ({self.next.__repr__()})"

def swap_every_two(llist):
    # Start with one node, need to switch references on every node
    # Start: 1 points to 2 points to 3 points to 4 points to None
    # becomes: 2 points to 1 points to 4 points to 3 points to None
    # aka: reference to 2, reference to 3, reference to 4, None reference
    
    # naive solution -> just make a list, use indexes to swap references, nice and easy
    # O(2n), there might be a O(n) solution that I'm not seeing
    node_list = []
    current_node = llist
    current_index = 0
    while current_node:
        node_list.append(current_node)
        # every two indexes, swap nodes in list
        if current_index % 2 == 1:
            node_list[current_index] = node_list[current_index - 1]
            node_list[current_index - 1] = current_node
        current_node = current_node.next
        current_index += 1
    # [node2, node1, node4, node3]
    # then change references for nodes to next one in the list
    for index in range(len(node_list)):
        if index < len(node_list) - 1:
            node_list[index].next = node_list[index + 1]
        else:
            node_list[index].next = None
    return node_list[0]

llist = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(swap_every_two(llist))
# Correct answer:
# 2, (1, (4, (3, (5, (None)))))
