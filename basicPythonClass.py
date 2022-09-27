class Student:
    numStudent = 0
    def __init__(self, name, age):
        Student.numStudent += 1
        self.__name = name
        self.__age = age

rahul = Student("Rahul", 18)
Student.numStudent += 1
print(Student.numStudent)
