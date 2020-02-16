"""

A stack class - follows the Last In First Out style
Garrett Matthews

"""


class Stack:
    """A stack class"""

    def __init__(self):
        self.stack = []

    def push(self, item):
        """Adds an item on to the top of the stack"""
        self.stack.append(item)

    def pop(self):
        """Removes the top item of the stack"""
        if len(self.stack) == 0:
            raise IndexError("Error- the stack is empty and nothing is left to remove")
        removed = self.stack[-1]
        del self.stack[-1]
        return removed

    def peek(self):
        """Returns the top item of the stack without removing it"""
        if len(self.stack) == 0:
            raise IndexError("Error - the stack is empty, nothing to peek on")
        peeked = self.stack[-1]
        return peeked

    def size(self):
        """Returns the size of the stack"""
        return len(self.stack)

    def clear(self):
        """Empties the stack"""
        self.stack = []


def main():
    """Main function to test that stack is opperating correctly"""
    stack = Stack()
    for i in range(10):
        stack.push(i)
    print(stack.peek())
    for i in range(stack.size()):
        print(stack.pop())


if __name__ == "__main__":
    main()
