from Objects.building import Building
from Objects.sprite import Sprite
class ResearchLab(Building):

  def __init__(self):
    super().__init__()
    self.constructionCost = 50000
    self.constructionTime = 7
    self.maxLevel = 3
    self.reputation = 0.125
    self.morale = 0
    self.graduationRate = 0.075
    self.involvement = 0.075
    self.tuition = 0
    self.enable = True
    self.enrollment = 2
    self.maxEnrollment = 0
    self.professors = 5
    self.name = "Research Lab"
    self.effects = "The research lab gives students a place todo undergraduate research. Adding or upgrading a research lab increases universities reputation, student morale, and graduation rate."
    self.sprite = Sprite('Resources/researchlab', (0,0), (10,10))

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
    self.constructionCost += 3000
    self.level += 1
    self.reputation += 0.1
    self.graduationRate += 0.05
    self.involvement += 0.05
    self.enrollment += 2
    self.professors += 3
    self.enrollment += self.professors / self.enrollment * 10
    if self.level == self.maxLevel:
      self.enable = false
