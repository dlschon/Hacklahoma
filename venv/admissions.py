import global_vars
from Objects.student import Student
from Objects.person import Person
import random

def first_students():
	for i in range(0,10):
		global_vars.university.students.append(Student(0, random.randint(0,1), random.random(),random.uniform(2.3,4.0),.5,0))

def admit_students():
	global_vars.university.calcMorale()
	rep = global_vars.university.reputation
	grad_rate = global_vars.university.grad_rate
	opp = global_vars.university.opportunity
	tuit = global_vars.university.tuition
	programs = global_vars.university.programs
	max_pop = global_vars.university.capacity()

	app_amt = 20
	app_amt += (30 * grad_rate)
	if ((tuit / 1000) >= 10):
		if(rep + opp >= 0.9):
			app_amt += 30 * (rep + opp)
		elif (rep + opp >= 0.7):
			app_amt += 25 * (rep + opp)
		elif (rep + opp >= 0.5):
			app_amt += 20 * (rep + opp)
		else:
			app_amt += 10 * (rep + opp)
	elif ((tuit / 1000) >= 5):
		if(rep + opp >= 0.7):
			app_amt += 25 * (rep + opp)
		elif (rep + opp >= 0.5):
			app_amt += 20 * (rep + opp)
		else:
			app_amt += 15 * (rep + opp)
	elif ((tuit / 1000) >= 1):
		if(rep + opp >= 0.5):
			app_amt += 25 * (rep + opp)
		else:
			app_amt += 15 * (rep + opp)
	else:
		if((rep + opp) >= 0.6):
			app_amt += 30 * (rep + opp)
		else:
			app_amt += 15 * (rep + opp)
	
	app_amt += 20 * (len(programs) / 8)

	rand_num = random.random()
	population = max_pop/3
	population *= (app_amt / 100)
	
	population += 100 * rand_num

	#generate population
	accept = [] 
	for p in range(int(population)):
		p = Student(0, random.randint(0,1), random.random(), random.uniform(2.0,4.0), .5, 0)
		if(p.gpa >  global_vars.university.accept_gpa):
			accept.append(p)
	curr_students = global_vars.university.students
	
	#keep acceptances under capacity
	while(len(curr_students) + len(accept) > max_pop):
		accept.pop()
	
	#add in the new students
	print (len(accept))
	for student in accept:
		global_vars.university.students.append(student)
