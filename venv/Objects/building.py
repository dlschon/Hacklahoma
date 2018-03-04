class Building:
  def __init__(self):
    self.level = 1
    self.impact = null
    self.monthlyCost = 0
    self.constructionCost = 0
    self.capacity = 0
    self.maxLevel = 1
    self.constructionTime
    self.type = None
    self.sprite = None

  def __init__(self, name, type, level, impact, monthlyCost, constructionCost, capacity, maxLevel):
    self.name = name
    self.type = type
    self.level = level
    self.impact = impact
    self.monthlyCost = monthlyCost
    self.constructionCost = constructionCost
    self.capacity = capacity
    self.maxLevel = maxLevel
    self.sprite = None
