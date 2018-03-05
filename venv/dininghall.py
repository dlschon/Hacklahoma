from building import Building
from sprite import Sprite
import global_vars
from finance import Finance

class DiningHall(Building):
  def __init__(self):
    Building.__init__(self)
    self.constructionCost = 20000
    self.constructionTime = 4
    self.finances = Finance()
    self.name = "Dining Hall"
    self.effects = "The Dining Hall is where students eat.  Adding or upgrading a lecture hall increases universities student morale and reputation."
    self.sprite = Sprite('Resources/dininghall', (0,0), (10,10))

  def activate(self):
    Building.activate(self)
    self.finances.description = "Dining Hall: "
    self.finances.value = 2000
    global_vars.university.finances.append(self.finances)

  def level_upgrade(self):
    self.constructionCost += 2000
    self.level += 1
    self.reputation += 0.01
    self.morale += 0.01
    self.enrollment += 1
    if self.level == self.maxLevel:
      self.enable = false
