"""
Class to generate a linked list
"""

from recursioncounter import RecursionCounter


class Node:
    """Basic node class to implement linked lists"""

    def __init__(self,data, next=None):
        self.data = data
        self.next = next


class CourseList:
    """Creates a list of course objects"""

    def __init__(self, data=None, next_course=None):
        self.data = data
        self.next = next_course
        self.courselyst = []
        self.head = Node(data, next_course)

    def quicksort(self, lyst):
        """Uses the quicksort algorithm to sort a lyst"""
        if not isinstance(lyst, list):
            raise ValueError("Error. Must submit a list")
        self.quicksort_helper(lyst, 0, len(lyst) - 1)
        return lyst

    def quicksort_helper(self, lyst, low, high):
        """Recursive helper for the quicksort algorithm"""
        RecursionCounter()
        if low < high:
            pivot_point = self.quicksort_pivot(lyst, low, high)
            self.quicksort_helper(lyst, low, pivot_point - 1)
            self.quicksort_helper(lyst, pivot_point + 1, high)

    def quicksort_pivot(self, lyst, left, right):
        """Algorithm to manage the swapping and pivot points for the quicksort function"""
        midpoint = (left + right) // 2
        pivot = lyst[midpoint].number()
        lyst[midpoint], lyst[right] = lyst[right], lyst[midpoint]
        border = left
        for i in range(left, right):
            if lyst[i].number() < pivot:
                self.swap(lyst, i, border)
                border += 1
        self.swap(lyst, right, border)
        return border

    def swap(self, lyst, index_1, index_2):
        """Function to swap the places of two indexes in a list"""
        lyst[index_1], lyst[index_2] = lyst[index_2], lyst[index_1]
        return lyst[index_1], lyst[index_2]

    def insert(self, course_item):
        """Inserts a course item into the CourseList, and sorts it by number in ascending order"""
        self.courselyst.append(course_item)
        self.quicksort(self.courselyst)
        new_node = Node(course_item)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def remove(self, course_number):
        """Removes an item from the list based off of the course number"""
        if isinstance(self.head, None):
            return None
        cur = self.head
        data_point, previous = self.remove_helper(cur, course_number)
        if data_point and previous != -1:
            print("Previous ", previous)
            print("Data_Point ", data_point)
            previous.next = data_point.next
            response = "Data successfully removed"
            return response
        else:
            response = "Data not found"
            return response

    def remove_helper(self, data_point, target, previous=None):
        """Recursive helper function for the remove function"""
        RecursionCounter()
        while data_point is not None and data_point.data.number() != target:
            previous = data_point
            data_point = data_point.next
            return self.remove_helper(data_point, target, previous)
        if data_point is not None:
            if data_point.data.number() == target:
                return data_point, previous
        else:
            return -1, -1

    def remove_all(self, course_number):
        """Removes all instances of the course number in the list"""
        if self.head is None:
            return None
        cur = self.head
        data_point, previous = self.remove_helper(cur, course_number)
        if data_point and previous == -1:
            return
        else:
            if data_point is None:
                previous.next = None
            else:
                previous.next = data_point.next
            return self.remove_all(course_number)

    def remove_all_helper(self, data_point, target, count=0, previous=None):
        """Recursive helper function for the remove function"""
        RecursionCounter()
        print("New loop")
        if data_point is not None:
            if data_point.data.number() == target:
                return data_point, previous, count
        while data_point is not None and data_point.data.number() != target:
            print(data_point.data.number())
            count += 1
            previous = data_point
            data_point = data_point.next
            return self.remove_all_helper(data_point, target, count, previous)
        return -1, -1, -1

    def find(self, number):
        """
        Finds the first instance of the course number in the list, and returns -1 if
        it is not there
        """
        if not isinstance(number, int):
            raise ValueError("Course number must be an integer")
        if self.head is None:
            return None
        cur_node = self.head
        return self.finder_helper(cur_node, number)

    def finder_helper(self, data_point, target):
        """Recursive helper function for the find function"""
        RecursionCounter()
        while data_point is not None and data_point.data.number() != target:
            data_point = data_point.next
            return self.finder_helper(data_point, target)
        if data_point is not None:
            if data_point.data.number() == target:
                return data_point.data
        else:
            return -1

    def size(self):
        """Returns the size of course list"""
        if self.head is None:
            return None
        cur = self.head
        return self.size_helper(cur)

    def size_helper(self, data_point, count=0):
        """Recursive helper function for the size call"""
        RecursionCounter()
        while data_point:
            count += 1
            data_point = data_point.next
            return self.size_helper(data_point, count)
        return count

    def calculate_gpa(self):
        """Returns the total gpa for all listed classes"""
        if len(self.courselyst) == 0:
            return 0.0
        cur = self.head
        gpa, count = self.calculate_gpa_helper(cur)
        if gpa or count == 0:
            return 0.0
        else:
            return gpa / count

    def calculate_gpa_helper(self, data_point, gpa=0, count=0):
        """Recursive function helper to calculate gpa """
        RecursionCounter()
        while data_point is not None:
            gpa += data_point.data.grade()
            count += 1
            return self.calculate_gpa_helper(data_point.next, gpa, count)
        return gpa, count

    def is_sorted(self):
        """Checks to see if the list is in sorted order"""
        lyst_copy = self.courselyst.copy()
        self.quicksort(lyst_copy)
        return bool(lyst_copy == self.courselyst)

    def __str__(self):
        if self.head is None:
            return None
        str_format = ""
        for i in self.courselyst:
            str_format += ("{}{}{}{}{}{}{}{}{}".format("cs", i.number(), " ", i.name(),
                                                       " Grade: ", i.grade(),
                                                       " Credit Hours: ", i.credit_hr(), '\n'))
        str_format += ("{}{}".format('\n', "Cumulative Gpa: "))
        str_format += ("{0:.3f}".format(self.calculate_gpa()))
        return str_format

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node
            current_node = current_node.next

