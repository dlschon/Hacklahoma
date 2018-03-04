from Objects.building import Building
from Objects.sprite import Sprite
class LectureHall(Building):
  def __init__(self):
    super().__init__()
    self.constructionCost = 10000
    self.maxLevel = 3
    self.level = 1
    self.reputation = 0.05
    self.morale = 0.05
    self.graduationRate = 0.05
    self.involvement = 0
    self.tuition = 0
    self.enrollment = 10
    self.maxEnrollment = 0
    self.professors = 2
    self.enable = true
    self.name = "Lecture Hall"
    self.lectureType = "Arts and Sciences"
    self.effects = "The Lecture Hall is where classes take place. Adding or upgrading a lecture hall increases universities reputation, student morale, graduation rate, and professors"
    self.sprite = Sprite('Resources/lecturehall', (0,0), (10,10))

  def _init_(self,constructionCost, maxLevel, reputation, morale, graduationRate, involvement, tuition, enrollment, maxEnrollment, professors):
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
    self.constructionCost += 2000
    self.level += 1
    self.reputation += 0.025
    self.morale += 0.025
    self.graduationRate += 0.025
    self.professors += 3
    self.enrollment += self.professors/self.enrollment *10
    if self.level == self.maxLevel:
      self.enable = false
