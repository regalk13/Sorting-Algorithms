# It is inevitable that when converting a group of numbers into a binary tree these are ordered, thanks to their properties, (major -> right, minor <- left)
# Complexity = worst-case O(h), O(n)
#
# Why use a Binary Tree? sometimes is linear and all operations, and if it is balanced, time complexity = O(h)

# Class create the Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Insert
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)

    return root

# Print in order
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

array = [1, 5, 4, 5, 10, 2]

r = Node(arr[0])
for i in array:
    r = insert(r, i)

inorder(r)
