"""
Main function to run the course and courselist classes
"""

from course import Course
from courselist import CourseList


def main():
    """Function that runs the the assignments for project 3"""
    # Reading in the data.txt file into a list of course objects
    course_lyst = []
    with open("data.txt", 'r') as file:
        for line in file:
            # List is created at top of each loop so linked list can be a nested list
            temp_lyst = []
            temp_lyst.append(line.split(','))
            for i in temp_lyst:
                temp_lyst = [j.replace('\n', '') for j in i]
            course = Course(int(temp_lyst[0]), temp_lyst[1], float(temp_lyst[2]), float(temp_lyst[3]))
            course_lyst.append(course)

    # Creating a linked list for course objects
    #head = None
    #for i in course_lyst:
        #head = CourseList(i, head)

    #print(head.find(1031))
    #print(head.remove(1030))
    #print(head.size())
    #print(head.find(1400))

    #while head is not None:
        #print(head.data)
        #head = head.next

    empty = CourseList()
    print(empty)


    """
    lyst = CourseList(None, None)
    for i in course_lyst:
        lyst.insert(i)
    print(lyst)
    lyst.remove(1030)
    print(lyst)
    course = Course(1111, "Help Desk", 2.0, 4.0)
    lyst.insert(course)
    print(lyst)
    print(lyst.size())
    print(lyst.is_sorted())
    """


if __name__ == "__main__":
    main()
