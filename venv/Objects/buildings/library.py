from Objects.building import Building
from Objects.sprite import Sprite
import global_vars

class Library(Building):
  def __init__(self):
    super().__init__()
    self.constructionCost = 100
    self.name = "Library"
    self.sprite = Sprite('Resources/library', (0,0), (10,10))
