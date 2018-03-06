from Objects.building import Building
from Objects.sprite import Sprite
import global_vars
from Objects.finance import Finance

class ResearchLab(Building):

  def __init__(self):
    super().__init__()
    self.constructionCost = 60000
    self.constructionTime = 7
    self.maxLevel = 3
    self.reputation = 0.125
    self.morale = 0
    self.graduationRate = 0.075
    self.involvement = 0.075
    self.tuition = 0
    self.enable = True
    self.enrollment = 2
    self.teachers = 2
    self.maxEnrollment = 0
    self.professors = 5
    self.name = "Research Lab"
    self.effects = "The research lab gives students a place to research. Adding or upgrading a research lab increases  reputation, student morale, and graduation rate."
    self.sprite = Sprite('Resources/researchlab', (0,0), (10,10))

  def activate(self):
    super().activate()
    self.finances = Finance()
    self.finances.description = "Reasearch grant: "
    self.finances.value = 4000
    global_vars.university.finances.append(self.finances)
