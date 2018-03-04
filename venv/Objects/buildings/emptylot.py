from Objects.building import Building
from Objects.sprite import Sprite

class EmptyLot(Building):
    def __init__(self):
        self.constructionCost = 0
        self.name = "Empty Lot"
        self.sprite = Sprite('Resources/emptylot', (0,0), (10,10))

