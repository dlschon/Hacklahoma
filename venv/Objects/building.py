class Building:
  def __init__(self):
    self.level = 0
    self.cost = 0
    self.upgradeFee = 0
    self.capacity = 0
    self.maxLevel = 1
    self.constructionTime = 6
    self.effects = 'The effects of the building'
    self.type = None
    self.sprite = None
    self.programs = []
    self.num_programs = 0

  #def __init__(self, name, type, level, impact, monthlyCost, constructionCost, capacity, maxLevel):
  #  self.name = name
  #  self.type = type
  #  self.level = level
  #  self.impact = impact
  #  self.monthlyCost = monthlyCost
  #  self.constructionCost = constructionCost
  #  self.capacity = capacity
  #  self.maxLevel = maxLevel
  #  self.sprite = None

  def upgrade(self):
    if(global_var.university.buy(self.upgrade_cost)):
     self.level += 1
     self.upgrade_cost += 5000 * self.level

  def add_program(self,program):	
    if(global_var.university.buy(program.cost)):
     self.programs.append(program)
