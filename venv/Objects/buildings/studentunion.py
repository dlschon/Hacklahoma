from Objects.building import Building
from Objects.sprite import Sprite
class StudentUnion(Building):
  def __init__(self):
    super().__init__()
    self.constructionCost = 100
    self.name = "Student Union"
    self.sprite = Sprite('Resources/studentunion', (0,0), (10,10))
