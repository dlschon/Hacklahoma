from tkinter import *
from tkinter import ttk
from Objects.building import Building
import global_vars
from Objects.finance import Finance
from Objects.map import Map
import copy

university = global_vars.university

class InfoPane:
    def __init__(self, title):
        self.title = title

class BuildingInfo(InfoPane):
    def __init__(self, building):
        InfoPane.__init__(self, 'Building Info')
        self.labels = [
            'Name',
            'Level',
            'Monthly Cost',
            'Capacity'
        ]
        self.values = [
            str(building.name),
            str(building.level),
            str(building.monthlyCost),
            str(building.capacity) + ' students'
        ]
        self.effects = building.effects
        self.makeform()

    def makeform(self):
        building_info_frame = Tk()
        building_info_frame.title(self.title)
        for label, value in zip(self.labels, self.values):
            row = Frame(building_info_frame)
            lab = Label(row, width=15, text=label, anchor='w')
            val = Label(row, text=value, anchor='e')
            row.pack(side=TOP, fill=X, padx=5, pady=5)
            lab.pack(side=LEFT)
            val.pack(side=RIGHT, expand=YES, fill=X)
        row = Frame(building_info_frame)
        lab = Label(row, width=15, text='Effects', anchor='w')
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)

        if type(self.effects) == str:
            row = Frame(building_info_frame)
            lab = Label(row, text=self.effects, anchor='w')
            row.pack(side=TOP, fill=X, padx=5, pady=1)
            lab.pack(side=LEFT, padx=15)
        else:
            for effect in self.effects:
                row = Frame(building_info_frame)
                lab = Label(row, text=effect, anchor='w')
                row.pack(side=TOP, fill=X, padx=5, pady=1)
                lab.pack(side=LEFT, padx=15)
        b2 = Button(building_info_frame, text='Destroy', command=())
        b2.pack(side=BOTTOM, padx=5, pady=5)
        b1 = Button(building_info_frame, text='Upgrade!', command=())
        b1.pack(side=BOTTOM, padx=5, pady=10)

        while True:
            try:
                building_info_frame.update()
            except:
                break

class StudentInfo(InfoPane):
    def __init__(self):
        InfoPane.__init__(self, 'Student Info')
        student_info_frame = Tk()
        student_info_frame.title(self.title)
        Label(text='Target GPA').grid(column=1, row=1, columnspan=2, pady=(10,0))
        slider = Scale(from_=2.0, to=4.0, orient=HORIZONTAL, resolution=0.1, length=400)
        slider.set(university.target_gpa)
        slider.grid(column=1, row=2, columnspan=2, pady=(0,15))
        #university.target_gpa = slider.set(3.0)
        Label(text='Current Enrollment: ', anchor='w').grid(column=1, row=3)
        Label(text=len(university.students), anchor='e').grid(column=2, row=3)
        Label(text='Max Enrollment: ', anchor='w').grid(column=1, row=4)
        Label(text=university.capacity(), anchor='e').grid(column=2, row=4)
        pbar = ttk.Progressbar(orient=HORIZONTAL, length=300, mode='determinate',
                               value=(len(university.students)/university.max_enrollment*100))
        pbar.grid(column=1, row=5, columnspan=2, pady=(0,15))
        Label(text='Average GPA: ').grid(column=1, row=6, pady=15)
        # need to add grad_rate
        Label(text=2.3).grid(column=2, row=6, pady=15)
        Label(text='Graduation Rate: ').grid(column=1, row=7, pady=15)
        Label(text=university.grad_rate).grid(column=2, row=7, pady=15)
        Label(text='Average Morale: ').grid(column=1, row=8, pady=(15,0))
        # need to add morale
        Label(text='78%').grid(column=2, row=8, pady=(15,0))
        # need to add morale to value
        pbar = ttk.Progressbar(orient=HORIZONTAL, length=300, mode='determinate', value=(78))
        pbar.grid(column=1, row=9, columnspan=2, pady=(0,15))

        while True:
            try:
                student_info_frame.update()
            except:
                break


class MoneyInfo(InfoPane):
    def __init__(self):
        InfoPane.__init__(self, 'Money Info')
        money_info_frame = Tk()
        money_info_frame.title(self.title)
        Label(text='Monthly Income: ').grid(column=1, row=1, pady=(0,10))
        print(university)
        revenue, revenues = university.calcRevenue()
        expense, expenses = university.calcExpense()
        income = revenue - expense
        if income >= 0: Label(text='+ $'+str(income), anchor='w').grid(column=2, row=1, pady=(0, 10))
        else: Label(text='+ $'+str(income), anchor='w').grid(column=2, row=1, pady=(0, 10))
        Label(text='Revenues: ', anchor='w').grid(column=1, row=2)
        Label(text='+$'+str(revenue), anchor='w').grid(column=2, row=2)
        r = 3
        for rev in revenues:
            Label(text=rev.description, anchor='w').grid(column=1, row=r)
            Label(text='+$'+str(rev.value), anchor='w').grid(column=2, row=r)
            r+=1
        Label(text='Expenses: ', anchor='w').grid(column=1, row=r)
        Label(text='-$'+str(expense), anchor='w').grid(column=2, row=r)
        r+=1
        for exp in expenses:
            Label(text=exp.description, anchor='w').grid(column=1, row=r)
            Label(text='-$'+str(exp.value), anchor='w').grid(column=2, row=r)
            r+=1

        while True:
            try:
                money_info_frame.update()
            except:
                break;

class InitialMessage():
    def __init__(self):
        Tk().wm_withdraw() #to hide the main window
        messagebox.showinfo('Info','Congratulations! You have been elected President of a small land-grant University! Invest your resources wisely and grow your University!')
        self.name = simpledialog.askstring('Prompt', 'What is your University called?')

class BuyBuilding(InfoPane):
    def __init__(self, lot):
        InfoPane.__init__(self, 'Construct New Building')
        construct_frame = Tk()
        construct_frame.title(self.title)
        r=1

        def buy(building):
            if global_vars.university.buy(building.constructionCost):
                global_vars.map.construct_building(lot.pos, type(building)())
                construct_frame.quit()

        for building in Map.getList():
            Label(text=building.name, anchor='center').grid(column=1, columnspan=2, row=r)
            Label(text=building.effects, anchor='center', wraplength=500).grid(column=1, columnspan=2, row=r+1)
            Label(text='Price: $'+str(building.constructionCost)).grid(column=1, row=r+2)
            Label(text='Build Time: '+str(building.constructionTime)+ ' months').grid(column=2, row=r+2)
            Button(construct_frame, text="Begin Construction", command=(buy(building))).grid(column=1, columnspan=2, row=r+3)
            r+=4

        while True:
            try:
                construct_frame.update()
            except:
                break;

