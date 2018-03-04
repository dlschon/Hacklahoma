from Objects.building import Building
from Objects.sprite import Sprite
class Stadium(Building):

  levels = [(0, 2000),
            ()]
  def __init__(self):
    self.constructionCost = 50000
    self.maxLevel = 3
    self.reputation = 0.075
    self.morale = 0.15
    self.graduationRate = 0
    self.involvement = 0.15
    self.tuition = 0
    self.enrollment = 10
    self.maxEnrollment = 0
    self.professors = 0
    self.enable = true
    self.effects = "The Stadium is a place students can go to get involved in different activities. " \
                   "Adding or upgrading the student union increases the universities reputation, morale, involvement and enrollment."
    self.name = "Stadium"
    self.sprite = Sprite('Resources/stadium', (0,0), (10,10))

  def _init_(self, constructionCost, maxLevel, reputation, morale, graduationRate, involvement, tuition, enrollment,
             maxEnrollment, professors):
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
    self.constructionCost += 3000
    self.level += 1
    self.reputation += 0.025
    self.morale += 0.1
    self.involvement += 0.1
    self.enrollment += 5
    if self.level == self.maxLevel:
      self.enable = false