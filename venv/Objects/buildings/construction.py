from Objects.building import Building
from Objects.sprite import Sprite

class EmptyLot(Building):
    def __init__(self, months, name):
        super().__init__()
        self.constructionCost = 0
        self.name = name
        self.effects = name + " will be completed in " + str(months)
        self.sprite = Sprite('Resources/construction', (0,0), (10,10))

