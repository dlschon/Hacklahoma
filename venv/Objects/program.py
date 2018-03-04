class Program:
  def __init__(self):
    self.amountInvested = 0
    self.unlocked = false

  def __init__(self, amountInvested, unlocked):
    self.amountInvested = amountInvested
    self.unlocked = unlocked

#union programs
class AlumniFoundation(Program):
  def __init__(self):
	self.unlocked = false
	self.cost = 1000
  
  def impact(self):
	global_var.university.money += 1000
    
class CareerServices(Program):
  def __init__(self):
	self.unlocked = false
	self.cost = 1000
  
  def impact(self):
	for s in global_var.university.students:
		s.productivity += 0.5 

#library programs
class Scholarships(Program):
  def __init__(self):

  def impact(self):
	for s in global_var.university.students:
		s.morale += 0.5

class FinancialAid(Program):
  def __init__(self):

  def impact(self):
	for s in global_var.university.students:
		s.morale += 0.5

class StudyAbroad(Program):
 def __init__(self):

 def impact(self):
	for s in global_var.university.students:
		s.productivity += 0.5
		s.morale += 0.5

class AcademicAdvisor(Program):
 def __init__(self):

 def impact(self):
	for s in global_var.university.students:
		s.productivity += 0.5
		s.morale += 0.5

#stadium program
class Rivalry(Program):
 def __init__(self):

 def impact(self):
	global_var.university.money += 1000
	for s in global_var.university.students:
		s.morale += 0.5

class HeadCoach(Program):
 def __init__(self):

 def impact(self):
	for s in global_var.university.students:
		s.morale += 0.5

class BetterBranding(Program):
 def __init__(self):

 def impact(self):
	global_var.unviersity.money += 1000
	for s in global_var.university.students:
		s.morale += 0.5

#research lab programs
class Groundbreaking(Program):
 def __init__(self):

 def impact(self):
	global_var.university.money += 1000
	for t in global_var.university.teachers:
		t.research += 0.5

class Collaborative(Program):
 def __init__(self):

 def impact(self):
	global_var.university.money += 1000
	for t in global_var.university.teachers:
		t.research += 0.5

class UndergradResearch(Program):
 def __init__(self):

 def impact(self):
	global_var.university.money += 1000
	for t in global_var.university.teachers:
		t.research += 0.5
	for s in global_var.university.students:
		s.productivity += 0.5

#dining hall
class Buffet(Program):
 def __init__(self):

class Freshness(Program):
 def __init__(self):

class MoreOptions(Program):
 def __init__(self):

#housing
class AcademicHalls(Program):
 def __init__(self):

class CoedHousing(Program):
 def __init__(self):

class ResidentPrograms(Program):
 def __init__(self):
