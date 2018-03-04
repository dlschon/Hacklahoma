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
