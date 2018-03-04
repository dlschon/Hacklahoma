from Objects.building import Building
from Objects.sprite import Sprite

class Construction(Building):
    def __init__(self, months, pos, name):
        super().__init__()
        self.name = name
        self.counter = months
        self.effects = [name + " will be ",
                        "completed in ",
                        str(months) + " months"]
        self.future = None
        self.pos = pos
        self.sprite = Sprite('Resources/construction', (0,0), (10,10))

