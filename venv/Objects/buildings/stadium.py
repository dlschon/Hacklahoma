from Objects.building import Building
from Objects.sprite import Sprite
class Stadium(Building):

  levels = [(0, 2000),
            ()]
  def __init__(self):
    super().__init__()
    self.constructionCost = 50000
    self.name = "Stadium"
    self.sprite = Sprite('Resources/stadium', (0,0), (10,10))
