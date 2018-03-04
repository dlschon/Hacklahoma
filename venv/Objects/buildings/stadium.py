from Objects.building import Building
from Objects.sprite import Sprite
class Stadium(Building):
  def __init__(self):
    self.constructionCost = 100
    self.name = "Stadium"
    self.sprite = Sprite('Resources/stadium', (0,0), (10,10))
