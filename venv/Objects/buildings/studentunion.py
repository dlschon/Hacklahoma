from Objects.building import Building
from Objects.sprite import Sprite

class StudentUnion(Building):

  def __init__(self):
    super().__init__()
    self.constructionCost = 30000
    self.constructionTime = 6
    self.maxLevel = 3
    self.reputation = 0.05
    self.morale = 0.075
    self.graduationRate = 0
    self.involvement = 0.15
    self.tuition = 0
    self.enrollment = 2
    self.maxEnrollment = 0
    self.professors = 0
    self.enable = True
    self.name = "Student Union"
    self.effects = "The Student Union is a place students can go to get involved in different activities. \
                   Adding or upgrading the student union increases the universities reputation, morale, involvement and enrollment."
    self.sprite = Sprite('Resources/studentunion', (0,0), (10,10))
