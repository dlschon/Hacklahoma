from Objects.building import Building
from Objects.sprite import Sprite
import global_vars
from Objects.finance import Finance

class Stadium(Building):

  def __init__(self):
    super().__init__()
    self.constructionCost = 60000
    self.constructionTime = 8
    self.maxLevel = 3
    self.reputation = 0.075
    self.morale = 0.15
    self.graduationRate = 0
    self.involvement = 0.15
    self.tuition = 0
    self.enrollment = 10
    self.maxEnrollment = 0
    self.professors = 0
    self.enable = True
    self.effects = "The Stadium is a place students can go to get involved in different activities. " \
                   "Adding or upgrading the student union increases the universities reputation, morale, involvement and enrollment."
    self.name = "Stadium"
    self.sprite = Sprite('Resources/stadium', (0,0), (10,10))

  def activate(self):
    super().activate()
    self.finances = Finance()
    self.finances.description = "Football: "
    self.finances.value = 4500
    global_vars.university.finances.append(self.finances)
