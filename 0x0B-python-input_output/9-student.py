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
        Instantiation of the class attributes
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        The function that retrieves a dictionary repr,
        of an instance of the Student class
        """

        return self.__dict__


if __name__ == '__main__':
    students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

    for student in students:
        j_student = student.to_json()
        print(type(j_student))
        print(j_student['first_name'])
        print(type(j_student['first_name']))
        print(j_student['age'])
        print(type(j_student['age']))
