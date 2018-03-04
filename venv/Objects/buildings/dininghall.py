from Objects.building import Building
from Objects.sprite import Sprite
class DiningHall(Building):
  def _init_(self):
    self.constructionCost = 15000
    self.maxLevel = 3
    self.level = 1
    self.reputation = 0.025
    self.morale = 0.025
    self.graduationRate = 0
    self.involvement = 0
    self.tuition = 0
    self.enrollment = 2
    self.maxEnrollment = 0
    self.professors = 0
    self.enable = True
    self.name = "Dining Hall"
    self.effects = "The Dining Hall is where students eat.  Adding or upgrading a lecture hall increases universities student morale and reputation."
    self.sprite = Sprite('Dininghall', (0,0), (10,10))

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
    self.reputation += 0.01
    self.morale += 0.01
    self.enrollment += 1
    if self.level == self.maxLevel:
      self.enable = false