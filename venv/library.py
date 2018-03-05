from building import Building
from sprite import Sprite
import global_vars

class Library(Building):
  def __init__(self):
    Building.__init__(self)
    self.constructionCost = 25000
    self.maxLevel = 3
    self.constructionTime = 5
    self.reputation = 0.05
    self.morale = 0.05
    self.graduationRate = 0.1
    self.involvement = 0
    self.tuition = 0
    self.enrollment = 3
    self.enable = True
    self.maxEnrollment = 0
    self.professors = 0
    self.name = "Library"
    self.effects = ["The library is where students at your university will study. Adding or upgrading a library increases ",
                   "universities reputation, student morale, and graduation rate."]
    self.sprite = Sprite('Resources/library', (0,0), (10,10))

  def level_upgrade(self):
    self.constructionCost += 2500
    self.level += 1
    self.reputation += 0.025
    self.morale += 0.025
    self.graduationRate += 0.05
    self.enrollment += 1
    if self.level == self.maxLevel:
      self.enable = false
