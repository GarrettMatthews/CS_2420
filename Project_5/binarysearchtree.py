"""

Binary Search Tree Program

Garrett Matthews

"""

from recursioncounter import RecursionCounter


class Node:
    """Node class for a binary search tree"""

    def __init__(self, data, left_child = None, right_child = None):
        self.data = data
        self.left = left_child
        self.right = right_child
        self.height = None

    def is_leaf(self):
        """Returns a boolean if a node is a leaf or not"""
        return bool(self.left is None and self.right is None)

    def update_height(self):
        """Returns height?"""
        return self.height

    def __str__(self):
        """Returns a string of self.data"""
        return self.data


class BinarySearchTree:
    """Binary search tree class made with a linked list"""

    def __init__(self):
        self.root = None

    def add(self, item):
        """Function for adding items to the proper place in the binary tree"""

        def add_helper(node):
            """Recursive helper to add items to the binary tree"""
            RecursionCounter()
            if item < node.data:
                if node.left is None:
                    node.left = Node(item)
                else:
                    add_helper(node.left)
            elif node.right is None:
                node.right = Node(item)
            else:
                add_helper(node.right)

        if self.is_empty():
            self.root = Node(item)
        else:
            add_helper(self.root)

    def is_empty(self):
        """Returns a boolean of whether the tree is empty"""
        return bool(self.root is None)

    def find(self, item):
        """Finds an item in the binary search tree and returns it. Returns none otherwise"""

        def find_helper(node):
            """Recursive helper function for find"""
            RecursionCounter()
            if node is None:
                return None
            elif node.data == item:
                return node.data
            elif node.data > item:
                return find_helper(node.left)
            else:
                return find_helper(node.right)

        return find_helper(self.root)

    def remove(self, item, start=None):
        """Removes an item from the binary tree"""
        if start is None:
            start = self.root

        def remove_helper(node):
            """Recursive helper for the remove function"""
            if node is None:
                return None
            elif item < node.data:
                return remove_helper(node.left)
            elif item > node.data:
                return remove_helper(node.right)
            else:
                if node.left is None:
                    temp = node.data
                    node.data = node.right
                    return temp
                elif node.right is None:
                    temp = node.data
                    node.data = node.left
                    return temp
                temp = min_value(node.right)
                found = node.data
                node.data = temp.data
                current = node
                while current.left != node.data and current.left is not None:
                    current = current.left
                current.left = None
                return found

        def min_value(node):
            """Helper function to return the minimum value of a tree"""
            current = node
            while current.left is not None:
                current = current.left
            return current

        remove_helper(start)

    def preorder(self):
        """Returns a list formatted in preorder"""
        lyst = []

        def preorder_helper(node):
            """Helper recursion method"""
            RecursionCounter()
            if node is not None:
                lyst.append(node.data)
                preorder_helper(node.left)
                preorder_helper(node.right)

        preorder_helper(self.root)
        return lyst

    def inorder(self):
        """Returns a list formatted in inorder"""
        lyst = []

        def inorder_helper(node):
            """Helper recursive function for inorder traversal"""
            if node is not None:
                inorder_helper(node.left)
                lyst.append(node.data)
                inorder_helper(node.right)

        inorder_helper(self.root)
        return lyst

    def height(self, start=None):
        """Returns the height of the tree"""
        lyst = []
        if start is None:
            start = self.root

        def max_depth(node, count=0):
            """Helper recursive function for the height function"""
            RecursionCounter()
            if node is None:
                return 0
            else:
                lyst.append(count)
                l_depth = (max_depth(node.left, count + 1))
                r_depth = (max_depth(node.right, count + 1))
                return max(lyst)

        return max_depth(start)

    def __len__(self):
        """Returns the number of nodes in the binary tree"""

        def len_helper(node):
            """Recursive helper function for len"""
            RecursionCounter()
            if node is None:
                return 0
            else:
                return len_helper(node.left) + 1 + len_helper(node.right)

        return len_helper(self.root)

    def __str__(self):
        """Returns a string representation of the binary search tree"""

        def str_helper(node, indent=0):
            """Recursive helper function for the str method"""
            result = ''
            if node is not None:
                item = str(node.data)
                below = self.height(node)
                tab = ''
                for i in range(indent):
                    tab += '\t'
                result += tab + item
                result += ' (' + str(below) + ')'
                if below == 0:
                    result += "[Leaf]"
                result += '\n'
                if node.left is None and below != 0:
                    tab += '\t'
                    result += tab + "[Empty]" + '\n'
                result += str_helper(node.left, indent + 1)
                if node.right is None and below != 0:
                    tab += '\t'
                    result += tab + "[Empty]" + '\n'
                result += str_helper(node.right, indent + 1)
            return result

        return str_helper(self.root)
