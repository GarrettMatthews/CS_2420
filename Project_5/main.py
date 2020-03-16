"""
Program for running the binary search tree program

Garrett Matthews

"""

from binarysearchtree import BinarySearchTree


def main():
    """Function to run the binary search tree"""
    bst = BinarySearchTree()
    lyst = [21, 26, 30, 9, 4, 14, 28, 18, 15, 10, 2, 3, 7]
    for i in lyst:
        bst.add(i)
    print(bst.preorder())
    print(bst)
    rem_lyst = [21, 9, 4, 18, 15, 7]
    for i in rem_lyst:
        bst.remove(i)
    print(bst)


if __name__ == '__main__':
    main()
