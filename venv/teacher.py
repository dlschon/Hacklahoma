import global_vars
import random
from person import Person
from finance import Finance

class Teacher(Person):
    def __init__(self):
        self.research = 0
        self.teaching = 0
        self.prestige = 0
        self.salary = 0
        self.name = global_vars.names.generate_name_last()
        
    def hire(self):
        finance = Finance()
        finance.description = 'Dr. '+ self.name
        finance.value = -self.salary
        global_vars.university.teachers.append(self)
        global_vars.university.finances.append(finance)

    def generate():
        teacher = Teacher()
        teacher.salary = random.randrange(500, 3000, 25)
        if (teacher.salary >= 2500):
            val = (random.uniform(.8, 1), random.uniform(.8, 1), random.uniform(.8, 1))
        elif (teacher.salary >= 1500):
            val = (random.uniform(.5, .85), random.uniform(.5, .85), random.uniform(.5, .85))
        elif (teacher.salary >= 1000):
            val = (random.uniform(.2, .6), random.uniform(.2, .6), random.uniform(.2, .6))
        else:
            val = (random.uniform(0, .25), random.uniform(0, .25), random.uniform(0, .25))
        teacher.research = val[0]
        teacher.teaching = val[1]
        teacher.prestige = val[2]
        return teacher
