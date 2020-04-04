"""

Hashmap class for Project 7

Garrett Matthews

"""


class HashMap(object):
    """Class to make a list based Hash Map"""

    def __init__(self):
        self.lyst = []
        self.start()

    def start(self):
        """Function to initialize the hash list"""
        for i in range(8):
            self.lyst.append(None)
            j = i
            j = j + i

    def capacity(self):
        """Returns the capacity of the list"""
        return len(self.lyst)

    def size(self):
        """Returns how many items are in the list"""
        count = 0
        for i in self.lyst:
            if i is not None:
                count += 1
        return count

    def clear(self):
        """Empties the hash list"""
        self.lyst = []
        self.start()

    def rehash(self):
        """Rebuilds the hash list when the size gets too big"""
        new_size = self.capacity() * 2
        temp = self.lyst.copy()
        self.lyst = []
        for i in range(new_size):
            self.lyst.append(None)
            j = i
            j = i + j
        for i in temp:
            position = 0
            while self.lyst[position] is not None:
                position += 1
            self.lyst[position] = temp[position]

    def keys(self):
        """Returns a  list of keys in the hash list"""
        temp = []
        for i in self.lyst:
            if i is not None:
                temp.append(i[0])
        return temp

    def get(self, key, default=None):
        """Returns the value for key if key is in hash map, or the default if it is not there"""
        position = 0
        answer = default
        while position < len(self.lyst) and self.lyst[position] is not None:
            if self.lyst[position][0] == key:
                answer = self.lyst[position][1]
            position += 1
        return answer

    def set(self, key, value):
        """Adds the key,value pair to hash map as a list"""
        position = 0
        present = False
        while position < len(self.lyst) and self.lyst[position] is not None:
            if self.lyst[position][0] == key:
                present = True
                break
            position += 1
        if present:
            self.lyst[position][1] = value
        else:
            position = 0
            while self.lyst[position] is not None:
                position += 1
            self.lyst[position] = [key, value]
        if self.size() / self.capacity() >= 0.80:
            self.rehash()
