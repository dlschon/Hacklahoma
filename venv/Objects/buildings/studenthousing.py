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
    self.effects = "Student Housing is where the students stay while they are going to the university."\
                   " Student Housing increases max enrollment."
    self.name = "Student Housing"
    self.sprite = Sprite('Resources/studenthousing', (0,0), (10,10))

  def activate(self):
    super().activate()
    self.finances.description = "Housing: "
    self.finances.value = 2000
    global_vars.university.finances.append(self.finances)