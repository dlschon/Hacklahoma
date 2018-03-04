import global_vars

class Building:

  def __init__(self):
    self.level = 1
    self.impact = None
    self.monthlyCost = 0
    self.constructionCost = 0
    self.capacity = 0
    self.maxLevel = 1
    self.constructionTime = 6
    self.effects = ['The effects of',
                    'the building']
    self.type = None
    self.sprite = None

  def activate(self):
    global_vars.university.calc_maintenance()
