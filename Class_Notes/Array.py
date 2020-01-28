"""
File:arrays.py
An Array is like a list, but the client can use only [], len, iter, 
and str. To instantiate, use <variable>=Array(<capacity>,<optionalfillvalue>)
The fill value is None bydefault.
Downloaded from a class website/page
""" 
class Array (object):
    """Represents an array."""

    def __init__(self, capacity, fillValue=None):
        """Capacity is the static size of the array. 
        fillValue is placed in each position."""
        self.items = list()
        for count in range(capacity):
            self.items.append(fillValue)

    def __len__(self):
        """The capacity of the array."""
        return len(self.items)
    
    def __str__(self):
        """The string representation of the array."""
        return str(self.items)
    
    def __iter__(self):
        """Supports traversal with a for loop."""
        return iter(self.items)

    def __getitem__(self,index):
        """Subscript operator for access at index."""
        return self.items[index]

    def __setitem__(self,index,newItem):
        """Subscript operator for replacement at index."""
        self.items[index] = newItem
    
def main():
    """Test code for Array class."""
    """Notes taken in class"""
    DEFAULT_CAPACITY = 5
    a = Array(DEFAULT_CAPACITY)
    logicalSize = 0

    ## To increase the size of an array by one ##
    for i in range(len(a)):
        a[i] = i+1
        logicalSize += 1

    if len(a) == logicalSize:
        temp = Array(len(a) + 1)
        for i in range(len(a)):
            temp[i] = a[i]
        a = temp
    print("temp array: ", temp)
    print("a array: ", a)

    ## Decrease the size of an array ##
    temp2 = Array(len(a)//2)
    for i in range(len(temp2)):
        temp2[i] = a[i]
        logicalSize -= 1
    a = temp2

    a[2] = None
    logicalSize = 2

    print("temp2 array: ", temp2)
    print("a array: ", a)

    targetIndex = 1
    for i in range(logicalSize, targetIndex, -1):
        a[i] = a[i - 1]
    a[targetIndex] = 10

    logicalSize = 3
    print("a array: ", a)
    
    targetIndex = 1
    for i in range(targetIndex, logicalSize -1):
        a[i] = a[i-1]
    logicalSize -= 1

    print("a array: ", a)





if __name__ == "__main__":
    main()

    



