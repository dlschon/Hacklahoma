from building import Building
from sprite import Sprite
import global_vars
from finance import Finance
class StudentHousing(Building):
  def __init__(self):
    Building.__init__(self)
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


  def level_upgrade(self):
    self.constructionCost += 2000
    self.level += 1
    self.maxEnrollment += 20
    self.enrollment -= self.professors / self.enrollment * 10
    if self.level == self.maxLevel:
      self.enable = false

  def activate(self):
    Building.activate(self)
    self.finances.description = "Housing: "
    self.finances.value = 2000
    global_vars.university.finances.append(self.finances)
