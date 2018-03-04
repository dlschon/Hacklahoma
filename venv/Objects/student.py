from Objects.person import Person

class Student(Person):
  def __init__(self):
    self.major = None
    self.productivity = None
    self.gender = None
    self.involvement = None
    self.gpa = 0
    self.morale = 0
    self.year = 0

  def __init__(self, productivity, gender, involvement, gpa, morale, year):
    self.productivity = productivity
    self.gender = gender
    self.involvement = involvement
    self.gpa = gpa
    self.morale = morale
    self.year = year

  def evalSchool(self):
    programs = global_var.university.programs
    happy = ((len(programs) / 18) * 30) + (self.involvement * 20) + ((self.gpa / 4.0) * 30) + (self.morale * 20)
    global_var.university.reputation += (100 / len(global_var.university.students))(happy / 100)

