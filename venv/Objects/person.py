from names import Names
from main import Program

class Person:
    MALE = 0
    FEMALE = 1

    def __init__(self):
        main.names
        self.name = ""
        self.satisfaction = 0
        self.age = 0
        self.gender = null
        self.homeState = null

    def __init__(self, satisfaction, age, gender, homeState):
        self.satisfaction = satisfaction
        self.age = age
        self.gender = gender
        self.name = Program.names.generate_name_full_male() if gender == Person.MALE else Program.names.generate_name_full_female()
        self.homeState = homeState