import global_vars
import random
from person import Person
class Teacher(Person):
    def __init__(self):
        self.research = 0
        self.teaching = 0
        self. prestige = 0
        self.salary = 0
    def __init__(self, research, teaching, prestige, salary, tenured):
        self.research = research
        self.teaching = teaching
        self. prestige = prestige
        self.salary = salary
        
    def hire(self):
        self.salary = random.randrange(500,3000,25)
        if(salary >= 2500):
            val = (random.randrange(.8,1,.05),random.randrange(.8,1,.05),random.randrange(.8,1,.05))
        elif (salary >= 1500):
            val = (random.randrange(.5,.85,.05),random.randrange(.5,.85,.05),random.randrange(.5,.85,.05))
        elif (salary >= 1000):
            val = (random.randrange(.2,.6,.02),random.randrange(.2,.6,.02),random.randrange(.2,.6,.02))
        else:
            val = (random.randrange(0,.25,.01),random.randrange(0,.25,.01),random.randrange(0,.25,.01))
        research = val(0)
        teaching = val(1)
        prestige = val(2)
        global_vars.university.teachers.append(self)
