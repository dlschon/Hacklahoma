import global_vars
from Objects.student import Student
from Objects.person import Person
import random

def admit_students(students):
	rep = global_vars.University().reputation
	grad_rates = global_vars.University().graduation_rates
	opp = global_vars.University().oppurtunity
	tuit = global_vars.University().tuition
	programs = global_vars.University().programs
	max_pop = global_vars.University().capacity

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
		if(p.gpa >  global_var.University().accept_gpa):
			accept.append(p)
	curr_students = global_var.University().students
	
	#keep acceptances under capacity
	while(len(curr_students) + len(accept) > max_pop):
		accept.pop()
	
	#add in the new students
	curr_students.append(accept)	
