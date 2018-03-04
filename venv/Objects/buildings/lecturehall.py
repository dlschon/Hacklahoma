from Objects.building import Building
from Objects.sprite import Sprite
class LectureHall(Building):
  def __init__(self):
    self.constructionCost = 100
    self.name = "Lecture Hall"
    self.lecuretype = "Arts and Sciences"
    self.sprite = Sprite('Resources/lecturehall', (0,0), (10,10))
