class Building:
  def __init__(self):
    self.level = 1
    self.impact = null
    self.monthlyCost = 0
    self.constructionCost = 0
    self.capacity = 0
    self.maxLevel = 1
    self.type = null
    self.sprite = null;

  def __init__(self, type, level, impact, monthlyCost, constructionCost, capacity, maxLevel):
    self.type = type
    self.impact = impact
    self.monthlyCost = monthlyCost
    self.constructionCost = constructionCost
    self.capacity = capacity
    self.maxLevel = maxLevel
    self.sprite = null;
