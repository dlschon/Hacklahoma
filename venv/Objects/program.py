import global_var
from Objects.finance import Finance

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
	self.desc = "Foundation for Alumni to give back through"
	self.title = "Alumni Foundation"
	self.unlocked = false
	self.cost = 1000
  
  def impact(self):
	f = Finance()
	f.desciption = "The Alumni Foundation gives back"
	f.value = 1000
	global_var.university.finances.append(f)
	
    
class CareerServices(Program):
  def __init__(self):
	self.title = "Career Services"
	self.desc = "An office to assist student in finding careers after college"
	self.unlocked = false
	self.cost = 1000
  
  def impact(self):
	for s in global_var.university.students:
		s.productivity += 0.5 

#library programs
class Scholarships(Program):
  def __init__(self):
	self.title = "Scholarships"
	self.desc = "Money given to achieving students by the university for tuition"
	self.unlocked = false
	self.cost = 1000

  def impact(self):
	for s in global_var.university.students:
		s.morale += 0.5

class FinancialAid(Program):
  def __init__(self):
	self.title = "Financial Aid"
	self.desc = "Money given to students with financial need by the university for tuition"
	self.unlocked = false
	self.cost = 1000

  def impact(self):
	for s in global_var.university.students:
		s.morale += 0.5

class StudyAbroad(Program):
 def __init__(self):
	self.title = "Study Abroad Program"
	self.desc = "A program for students to complete courses for credit while abroad"
	self.unlocked = false
	self.cost = 1000
 def impact(self):
	for s in global_var.university.students:
		s.productivity += 0.5
		s.morale += 0.5

class AcademicAdvisor(Program):
 def __init__(self):
	self.title = "Academic Advisors"
	self.desc = "Advisors to assist students in picking out classes"
	self.unlocked = false
	self.cost = 1000

 def impact(self):
	for s in global_var.university.students:
		s.productivity += 0.5
		s.morale += 0.5

#stadium program
class Rivalry(Program):
 def __init__(self):
	self.title = "Strike up a rivalry"
	self.desc = "Another local university believes their athletics team is superior. Prove them wrong"
	self.unlocked = false
	self.cost = 1000

 def impact(self):
	f = Finance()
	f.description = "Heated football rivalry sells tickets"
	f.value = 1000
	global_var.university.finances.append(f)
	for s in global_var.university.students:
		s.morale += 0.5

class HeadCoach(Program):
 def __init__(self):
	self.title = "Hire a head coach"
	self.desc = "Every good team has a great leader. Hiring one will strike up the fans"
	self.unlocked = false
	self.cost = 1000

 def impact(self):
	for s in global_var.university.students:
		s.morale += 0.5

class BetterBranding(Program):
 def __init__(self):
	self.title = "Unify the athletic brand"
	self.desc = "Sell merchandise of your universities' team"
	self.unlocked = false
	self.cost = 1000

 def impact(self):
	f = Finance()
	f.description = "Fans love buying clothing with your athletics brand"
	f.value = 1000
	global_var.university.finances.append(f)
	for s in global_var.university.students:
		s.morale += 0.5

#research lab programs
class Groundbreaking(Program):
 def __init__(self):
	self.title = "Groundbreaking Research"
	self.desc = "A professor discovers something great"
	self.unlocked = false
	self.cost = 1000

 def impact(self):
	f = Finance()
	f.description = "New groundbreaking research brings in new funding"
	f.value = 1000
	global_var.university.finances.append(f)
	for t in global_var.university.teachers:
		t.research += 0.5

class Collaborative(Program):
 def __init__(self):
	self.title = "Collaborative Research"
	self.desc = "Professors collaborate alongside other universities"
	self.unlocked = false
	self.cost = 1000

 def impact(self):
	f = Finance()
	f.description = "Your professors start to collaborate with other universities and bring in new funding"
	f.value = 1000
	global_var.university.finances.append(f)
	for t in global_var.university.teachers:
		t.research += 0.5

class UndergradResearch(Program):
 def __init__(self):
	self.title = "Undergraduate Research"
	self.desc = "Implement a new undergraduate research program"
	self.unlocked = false
	self.cost = 1000
 def impact(self):
	f = Finance()
	f.description = "Undergrad assitence boost research and bring in new grants"
	f.value = 1000
	global_var.university.finances.append(f)
	for t in global_var.university.teachers:
		t.research += 0.5
	for s in global_var.university.students:
		s.productivity += 0.5

#dining hall
class Buffet(Program):
 def __init__(self):
	self.title = "Buffet Menu"
	self.desc = "All you can eat"
	self.unlocked = false
	self.cost = 1000

 def impact(self):
	for s in global_var.university.students:
		s.morale += 0.5

class Freshness(Program):
 def __init__(self):
	self.title = "Fresh Ingredients"
	self.desc = "Fresher food for fresher folks"
	self.unlocked = false
	self.cost = 1000

 def impact(self):
	for s in global_var.university.students:
		s.morale += 0.5

class MoreOptions(Program):
 def __init__(self):
	self.title = "More Dining Options"
	self.desc = "Variety is the spice of life"
	self.unlocked = false
	self.cost = 1000
 def impact(self):
	for s in global_var.university.students:
		s.morale += 0.5
#housing
class AcademicHalls(Program):
 def __init__(self):
	self.unlocked = false
	self.cost = 1000

 def impact(self):
	for s in global_var.university.students:
		s.morale += 0.5

class CoedHousing(Program):
 def __init__(self):
	self.title = "Coed Housing"
	self.desc = "Allow for intermingling"
	self.unlocked = false
	self.cost = 1000

 def impact(self):
	for s in global_var.university.students:
		s.morale += 0.5

class ResidentPrograms(Program):
 def __init__(self):
	self.title = "Housing Center Programs"
	self.desc = "Put on events for the students within housing"
	self.unlocked = false
	self.cost =1000

 def impact(self):
	for s in global_var.university.students:
		s.morale += 0.5
