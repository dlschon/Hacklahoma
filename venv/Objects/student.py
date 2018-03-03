class Student(Person):
  def __init__(self):
    self.major = null
    self.productivity = null
    self.gender = null
    self.involvement = null
    self.gpa = 0
    self.morale = 0
    self.year = 0

  def __init__(self, major, homeState, productivity, gender, involvement, gpa, morale, year):
    self.major = major
    self.productivity = productivity
    self.gender = gender
    self.involvement = involvement
    self.gpa = gpa
    self.morale = morale
    self.year = year