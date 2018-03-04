from Objects.building import Building
from Objects.sprite import Sprite
import global_vars

class Library(Building):
  def __init__(self):
    super().__init__()
    self.constructionCost = 30000
    self.maxLevel = 3
    self.constructionCost = 100
    self.reputation = 0.05
    self.morale = 0.05
    self.graduationRate = 0.1
    self.involvement = 0
    self.tuition = 0
    self.enrollment = 3
    self.enable = true
    self.maxEnrollment = 0
    self.professors = 0
    self.name = "Library"
    self.effects = "The library is where students at your university will study. Adding or upgrading a library increases universities reputation, student morale, and graduation rate."
    self.sprite = Sprite('Resources/library', (0,0), (10,10))

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
    self.constructionCost += 2500
    self.level += 1
    self.reputation += 0.025
    self.morale += 0.025
    self.graduationRate += 0.05
    self.enrollment += 1
    if self.level == self.maxLevel:
      self.enable = false
