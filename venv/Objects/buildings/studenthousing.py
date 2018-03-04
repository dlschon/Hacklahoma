from Objects.building import Building
from Objects.sprite import Sprite
class StudentHousing(Building):
  def __init__(self):
    self.constructionCost = 100
    self.name = "Student Housing"
    self.sprite = Sprite('Resources/studenthousing', (0,0), (10,10))
