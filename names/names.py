import time
import sys

sys.setrecursionlimit(20999)

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# THE RUNTIME FOR THIS STARTER CODE IS O(m*n) BECAUSE THE INPUT COMES FROM TWO DIFFERENT FILES THAT COULD BE DIFFERENT SIZES.
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value[0] < self.value[0]:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        # elif value[0] >= self.value[0]:
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
    
    def contains(self, target):
        if target == self.value:
            return True
        if target[0] < self.value[0]:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # def contains(self, target):
    #     current = self
    #     while current is not None:
    #         # if target == current.value:
    #         #     return True
    #         if target[0] < current.value[0]:
    #             current = current.left
    #         elif target[0] > current.value[0]:
    #             current = current.right
    #         # elif target == current.value:
    #         #     return True
    #         else:
    #             print(current.value)
    #             return True
    #     return False

# name_1_tree = []
# i = 0

# for name_1 in names_1:
#     if i == 0:
#         name_1_tree = BinarySearchTree(name_1)
#         i += 1
#     else:
#         name_1_tree.insert(name_1)
#         i += 1
# for name_2 in names_2:
#     if name_1_tree.contains(name_2):
#         duplicates.append(name_2)

# First, we create a Binary Search Tree using Names as the root node.
name_1_tree = BinarySearchTree("Names")

# Second, we populate the tree by looping through the first file
for name_1 in names_1:
    name_1_tree.insert(name_1)

# Then we loop through the second file and check to see which names from the second list are in the tree we just created, and for any that return true, we append that name to the duplicates list.
for name_2 in names_2:
    if name_1_tree.contains(name_2):
        duplicates.append(name_2)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


