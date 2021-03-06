from Objects.person import Person
import global_vars

class Student(Person):
  def __init__(self):
    self.major = None
    self.productivity = None
    self.gender = None
    self.involvement = None
    self.name = ""
    self.gpa = 0
    self.morale = 0
    self.year = 0

  def __init__(self, productivity, gender, involvement, gpa, morale, year):
    self.productivity = productivity
    self.gender = gender
    self.involvement = involvement
    try:
      self.name = global_vars.names.generate_name_full_male() if gender == 0 else global_vars.names.generate_name_full_female()
    except:
      self.name = "Jay Leno"
    self.gpa = gpa
    self.morale = morale
    self.year = year

  def evalSchool(self):
    programs = global_vars.university.programs
    happy = ((len(programs) / 18) * 30) + (self.involvement * 20) + ((self.gpa / 4.0) * 30) + (self.morale * 20)
    global_vars.university.reputation += int((100 / len(global_vars.university.students))*(happy / 100))

