"""
Class to read in course data from a text file
Garrett Matthews
"""


class Course(object):
    """Class to generate a course object"""

    def __init__(self, course_number=0, name="", credit_hour=0.0, grade=0.0):
        if not isinstance(course_number, int):
            raise ValueError("Class number must be a number")
        if course_number < 0:
            raise ValueError("Class number must be positive")
        if not isinstance(name, str):
            raise ValueError("Class name must be a string")
        if not isinstance(credit_hour, float):
            raise ValueError("Credit hour must be a float")
        if credit_hour < 0:
            raise ValueError("Credit hour must be greater than 0")
        if not isinstance(grade, float):
            raise ValueError("Grade must be a float")
        if grade < 0:
            raise ValueError("Grade must be greater than 0")
        self.course_number = course_number
        self.course_name = name
        self.credit_hour = credit_hour
        self.course_grade = grade
        self.next = None

    def number(self):
        """Retrieves the course number as an integer"""
        return self.course_number

    def name(self):
        """Retrieves the course name as a string"""
        return self.course_name

    def credit_hr(self):
        """Returns the credit hours as a float"""
        return self.credit_hour

    def grade(self):
        """Returns the grade as a float"""
        return self.course_grade

    def __str__(self):
        """Print format for Course object"""
        str_format = ("{}{}{}{}{}{}{}{}".format("cs", self.course_number, " ", self.course_name,
                                                " Grade: ", self.course_grade, " Credit Hours: ",
                                                self.credit_hour))
        return str_format
