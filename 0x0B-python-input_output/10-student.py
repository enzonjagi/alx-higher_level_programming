#!/usr/bin/python3
"""
A module containing:
a class Student that defines a student
"""


class Student:
    """
    a class Student that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Class attribute instantiation
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves
        a dictionary representation of a Student instance
        """

        this_dict = {}
        if attrs is None:
            return self.__dict__
        else:
            for i in attrs:
                try:

                    this_dict[i] = self.__dict__[i]
                except:  # catch the keyword error
                    pass
            return this_dict


if __name__ == '__main__':
    student_1 = Student("John", "Doe", 23)
    student_2 = Student("Bob", "Dylan", 27)

    j_student_1 = student_1.to_json()
    j_student_2 = student_2.to_json(['first_name', 'age'])
    j_student_3 = student_2.to_json(['middle_name', 'age'])

    print(j_student_1)
    print(j_student_2)
    print(j_student_3)
