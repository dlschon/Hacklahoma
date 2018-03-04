from Objects.building import Building
from Objects.sprite import Sprite
class StudentUnion(Building):
  def __init__(self):
    super().__init__()
    self.constructionCost = 25000
    self.maxLevel = 3
    self.reputation = 0.05
    self.morale = 0.075
    self.graduationRate = 0
    self.involvement = 0.15
    self.tuition = 0
    self.enrollment = 2
    self.maxEnrollment = 0
    self.professors = 0
    self.enable = true
    self.name = "Student Union"
    self.effects = "The Student Union is a place students can go to get involved in different activities. " \
                   "Adding or upgrading the student union increases the universities reputation, morale, involvement and enrollment."
    self.sprite = Sprite('Resources/studentunion', (0,0), (10,10))

  def _init_(self, constructionCost, maxLevel, reputation, morale, graduationRate, involvement, tuition, enrollment, maxEnrollment, professors):
    self.constructionCost = constructionCost
    self.maxLevel = maxLevel
    self.reputation = reputation
    self.morale = morale
    self.graduationRate = graduationRate
    self.involvement = involvement
    self.tuition = tuition
    self.enrollment = enrollment
    self.maxEnrollment = maxEnrollment
    self.professors = professors

  def level_upgrade(self):
    self.constructionCost += 2500
    self.level += 1
    self.reputation += 0.025
    self.morale += 0.05
    self.involvement += 0.75
    self.enrollment += 1
    if self.level == self.maxLevel:
      self.enable = false