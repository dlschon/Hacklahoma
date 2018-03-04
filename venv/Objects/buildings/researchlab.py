from Objects.building import Building
from Objects.sprite import Sprite
class ResearchLab(Building):

  def __init__(self):
    self.constructionCost = 10000
    self.name = "Research Lab"
    self.sprite = Sprite('Resources/researchlab', (0,0), (10,10))
