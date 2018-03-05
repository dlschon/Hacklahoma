from Objects.building import Building
from Objects.sprite import Sprite
import global_vars
from Objects.finance import Finance

class DiningHall(Building):
  def __init__(self):
    super().__init__()
    self.constructionCost = 20000
    self.constructionTime = 4
    self.finances = Finance()
    self.name = "Dining Hall"
    self.effects = "The Dining Hall is where students eat.  Adding or upgrading a lecture hall increases universities student morale and reputation."
    self.sprite = Sprite('Resources/dininghall', (0,0), (10,10))

  def activate(self):
    super().activate()
    self.finances.description = "Dining Hall: "
    self.finances.value = 2000
    global_vars.university.finances.append(self.finances)
