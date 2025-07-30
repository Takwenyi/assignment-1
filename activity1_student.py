# Activity: Create a class with at least three attributes and one method
# This class will store basic details about a student and display them

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

# Create an object of the Student class
student1 = Student("Celia", 19, "Software Engineering")

# Call the method to display the student's info
student1.display_info()
