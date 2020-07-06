
# Below we are initialising a class for a student with variables name, age and course.

class Student():
    def __init__(self, name, age, course, topic):
        self.__name = name
        self.age = age
        self.course = course
        self.topic = topic

# Below we are creating two functions, one to state the student is on lunch and one to state that they are at home.


    def lunch(self):
        print(self.name + " " + "is on lunch")

    def home(self):
        print(self.name + "is at home")

    def __change_course(self, course):
        self.course = course

    def fave_topic(self):
        print("My favourite topic is Communication Skills")


m = Student("Mehdi", "21", "DevOps", "Communication Skills")




