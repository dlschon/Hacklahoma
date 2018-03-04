from Objects.building import Building
from Objects.sprite import Sprite

class Library(Building):
  def __init__(self):
    self.constructionCost = 100
    self.name = "Library"
    self.sprite = Sprite('Resources/library', (0,0), (10,10))
