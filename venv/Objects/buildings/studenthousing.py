from Objects.building import Building
from Objects.sprite import Sprite
import global_vars
from Objects.finance import Finance
class StudentHousing(Building):
  def __init__(self):
    super().__init__()
    self.constructionCost = 10000
    self.constructionTime = 4
    self.finances = Finance()

    self.maxLevel = 3
    self.reputation = 0
    self.morale = 0
    self.graduationRate = 0
    self.involvement = 0
    self.tuition = 0
    self.enrollment = 0
    self.enable = True
    self.maxEnrollment = 20
    self.capacity = 20
    self.professors = 0
    self.effects = ["Student Housing is where the students stay while they are going to the university.",\
                   " Student Housing increases max enrollment."]
    self.name = "Student Housing"
    self.sprite = Sprite('Resources/studenthousing', (0,0), (10,10))

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
    self.constructionCost += 2000
    self.level += 1
    self.maxEnrollment += 20
    self.enrollment -= self.professors / self.enrollment * 10
    if self.level == self.maxLevel:
      self.enable = false

  def activate(self):
    super().activate()
    self.finances.description = "Housing: "
    self.finances.value = 2000
    global_vars.university.finances.append(self.finances)