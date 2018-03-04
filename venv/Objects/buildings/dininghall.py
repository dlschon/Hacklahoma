from Objects.building import Building
from Objects.sprite import Sprite
from program import *

class DiningHall(Building):
  def __init__(self):
    super().__init__()
    self.cost = 10000
    self.upgrade_cost = 10000
    self.name = "Dining Hall"
    self.sprite = Sprite('Resources/dininghall', (0,0), (10,10))

