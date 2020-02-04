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
    head = None
    for i in course_lyst:
        head = CourseList(i, head)








if __name__ == "__main__":
    main()
