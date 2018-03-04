from Objects.finance import Finance

class University:
    def __init__(self):
        self.money = 20000
        self.grad_rate = .6
        self.reputation = 0
        self.sudent_satisfaction = 0
        self.opportunity = 0
        self.tuition = 200
        self.name = ""
        self.target_gpa = 2.5
        self.accept_gpa = 0
        self.max_enrollment = 50
        self.tuition_income = Finance()
        self.tuition_income.description = 'Tuition: '
        self.tuition_income.value = 0
        self.maintenance = Finance()
        self.maintenance.description = 'Building maintenance'
        self.maintenance.value = 0

        self.teachers = []
        self.students = []
        self.programs = []
        self.buildings = []
        self.finances = []

        self.finances.append(self.tuition_income)
        self.finances.append(self.maintenance)

    def calc_maintenance(self):
        self.maintenance.value = len(self.buildings) * -750

    def update_tuition(self):
        self.tuition_income.value = len(self.students)*self.tuition

    def capacity(self):
        sum = 0
        for building in self.buildings:
            sum += building.capacity
        return sum

    def buy(self, cost):
        if (self.money > cost):
            self.money -= cost
            return True
        else:
            return False;

    def calcRevenue(self):
        revenue = []
        total = 0
        for finance in self.finances:
            if finance.value >= 0:
                revenue.append(finance)
                total += finance.value
        return total, revenue

    def calcExpense(self):
        expense = []
        total = 0
        for finance in self.finances:
            if finance.value < 0:
                expense.append(finance)
                total += finance.value
        return total, expense

    def calcMorale(self):
        cum_sum = 0;
        for student in self.students:
            cum_sum += student.morale

        if len(self.students) == 0:
            self.opportunity = .5
        else:
            self.opportunity = cum_sum / len(self.students)
        return self.opportunity
