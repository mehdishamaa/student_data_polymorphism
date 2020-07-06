from student_data import Student


# Below is the child class
# Below we are initialising a class for a student with variables name, age and course.

class Devops(Student):
    def __init__(self, name, age, course, topic):
        self.__name = name
        self.age = age
        self.__protected_course = course
        self.topic = topic


# Below we are creating two functions, one to state the student is on lunch and one to state that they are at home.

    def lunch(self):
        print(self.name + " " + "is on lunch")

    def home(self):
        print(self.name + "is at home")

    def __change_course(self, course):
        self.course = course

    def fave_topic(self):
        print("My favourite topic is AWS")


# Below we create two objects

bob = Student("Bob", "21", "Business", "Communication Skills")

tim = Devops("Tim", "20", "DevOps", "AWS")


# The below function overrides the method from the first file -

print(tim.fave_topic())



