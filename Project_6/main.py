from binarysearchtree import BinarySearchTree


bst = BinarySearchTree()
lyst = [1,2,3,4,5,6,7,8]
for i in lyst:
    bst.add(i)
#print(bst)
bst.add(0)
bst.add(-6)
bst.add(-3)

bst.rebalance_tree()
print(bst)
