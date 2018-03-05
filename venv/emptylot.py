from building import Building
from sprite import Sprite

class EmptyLot(Building):
    def __init__(self, pos):
        Building.__init__(self)
        self.constructionCost = 0
        self.name = "Empty Lot"
        self.pos = pos
        self.sprite = Sprite('Resources/emptylot', (0,0), (10,10))

