"""In this exercise I will be implementing a binary search tree and the insert operation.
Each node is greater then every node is its left subtree, and each node is less than every node in its right subtree.
BST operations: 
1)insert: start at root and always insert as a leaf.
2) find: start at root
3) delete: leaf node - deleted without problem.
            node that has 1 child - his child takes his place. the grandchild doesnt change.
            node that has 2 children - find the next higher node and take its leaf
advantage - speed of O(log n)

>>> test1 = BinarySearchTree()
>>> test1.insert(4)
True
>>> test1.insert(4)
False
>>> test1.insert(7)
True
>>> test1.insert(2)
True
"""

# the TreeNode class has the internal methods that the user doesn't interact with.
class TreeNode:
    def __init__(self, new_value, left_child = None, right_child = None):
        self.new_value = new_value
        self.left_child = left_child
        self.right_child = right_child

    # implementing the insert method
    def insert(self,new_value):
        # checking if the current node has the new value, if so, no need to put it there
        if self.new_value == new_value:
            return False
        # if its smaller
        elif new_value < self.new_value:
            # if there is a node on the left
            if self.left_child:
                # recursively repeat the process starting at that node, and try insert the new value. now the root is the left node.
                return self.left_child.insert(new_value)
            # else : create a new node on the left that contains the new value
            else:
                self.left_child = TreeNode(new_value)
                return True
        # if the new value is greater than the current node:
        else:
            # if there is a node on the right
            if self.right_child:
                # recursively repeat the process starting at that node, and try insert the new value. now the root is the right node.
                return self.right_child.insert(new_value)
            # else : create a new node on the right that contains the new value
            else:
                self.right_child = TreeNode(new_value)
                return True        

# the BinarySearchTree class is a wrapper for the TreeNode class.
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # implementing the insert method
    def insert(self,new_value):
        # if there is a root
        if self.root:
            # recursively calling the insert from TreeNode class. It returns false when the new value equals the value at the root (node). It returns true when it successfully inserts the value in the left or right node.
            return self.root.insert(new_value)
        # if there is no root  
        else:
            # creating a new root which is a node object of the class TreeNode.
            self.root = TreeNode(new_value)
            return True

    # I chose to implement one way of traversing: in-order, sorting from least to greatest. left to right. Returns a list of all the numbers in the tree sorted.
    def inorder(self, tree_as_sorted_list_of_numbers):
        # if there is a number on the left, recursively call again inorder and check if there is a number on the left of that current left. 
        if self.left_child:
            self.left_child.inorder(tree_as_sorted_list_of_numbers)

        tree_as_sorted_list_of_numbers.append(self.new_value)


        



if __name__ == "__main__":
    import doctest
    doctest.testmod()