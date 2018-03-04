from Objects.building import Building
from Objects.sprite import Sprite

class EmptyLot(Building):
    def __init__(self, pos):
        super().__init__()
        self.constructionCost = 0
        self.name = "Empty Lot"
        self.pos = pos
        self.sprite = Sprite('Resources/emptylot', (0,0), (10,10))

