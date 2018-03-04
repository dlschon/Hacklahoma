import global_vars
from Objects.student import Student
from Objects.person import Person
import random

def first_students():
	for i in range(0,10):
		global_vars.university.students.append(Student(0, random.randint(0,1), random.random(),random.randrange(2.3,4.0,0.1)))

def admit_students():
	rep = global_vars.university.reputation
	grad_rates = global_vars.university.graduation_rates
	opp = global_vars.university.oppurtunity
	tuit = global_vars.university.tuition
	programs = global_vars.university.programs
	max_pop = global_vars.university.capacity

	app_amt = 20
	app_amt += (30 * grad_rates)
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
	for p in range(population):
		p = Student(0, random.randint(0,1), random.random(),random.randrange(2.0,4.0,0.1))
		if(p.gpa >  global_var.university.accept_gpa):
			accept.append(p)
	curr_students = global_var.university.students
	
	#keep acceptances under capacity
	while(len(curr_students) + len(accept) > max_pop):
		accept.pop()
	
	#add in the new students
	global_var.university.students.append(accept)	
