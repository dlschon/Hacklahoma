from Objects.building import Building
from Objects.sprite import Sprite
class DiningHall(Building):
  def __init__(self):
    super().__init__()
    self.constructionCost = 100
    self.name = "Dining Hall"
    self.sprite = Sprite('Resources/dininghall', (0,0), (10,10))
