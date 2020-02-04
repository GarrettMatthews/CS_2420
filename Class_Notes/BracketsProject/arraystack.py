"""
File: arraystack.py
Project 7.1
"""

from arrays import Array
from abstractstack import AbstractStack

class ArrayStack(AbstractStack):
    """An array-based stack implementation."""

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.items = Array(ArrayStack.DEFAULT_CAPACITY)
        AbstractStack.__init__(self, sourceCollection)

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self.
        Visits items from bottom to top of stack."""
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1

    def peek(self):
        """Returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises: KeyError if stack is empty."""
        if self.isEmpty():
            raise KeyError("The stack is empty")
        return self.items[len(self) - 1]

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.size = 0
        self.items = Array(ArrayStack.DEFAULT_CAPACITY)

    def push(self, item):
        """Inserts item at top of the stack."""
        # Resize array here if necessary
        if len(self) == len(self.items):
            temp = Array(2 * len(self))
            for i in range(len(self)):
                temp[i] = self.items[i]
            self.items = temp
        self.items[len(self)] = item
        self.size += 1

    def pop(self):
        """Removes and returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises: KeyError if stack is empty.
        Postcondition: the top item is removed from the stack."""
        if self.isEmpty():
            raise KeyError("The stack is empty")
        oldItem = self.items[len(self) - 1]
        self.size -= 1
        # Resize the array here if necessary
        if len(self) <= len(self.items) // 4 and \
           len(self.items) >= 2 * ArrayStack.DEFAULT_CAPACITY:
            temp = Array(len(self.items) // 2)          
            for i in range(len(self)):     
                temp [i] = self.items[i]  
            self.items = temp             
        return oldItem
        
         
