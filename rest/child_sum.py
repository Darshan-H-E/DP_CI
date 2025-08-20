
# Example 7.2: Given a Binary Tree, For each node, add sum of all the
# nodes in its hierarchy to its value. Below picture shows a sample input and
# output.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def add_children(node):
    if node == None:
        return

    add_children(node.left)
    add_children(node.right)

    final_sum = node.val

    if node.left != None:
        final_sum += node.left

    if node.right != None:
        final_sum += node.right

    node.val = final_sum


