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
        self.building = building

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
        r=1
        for label, value in zip(self.labels, self.values):
            Label(width=15, text=label, anchor='w').grid(column=1,row=r)
            Label(text=value, anchor='e').grid(column=2,row=r)
            r+=1
        Label(width=15, text='Effects', anchor='w').grid(column=1, columnspan=2,row=r)

        def upgrade():
            UpgradeBuilding(self.building)

        def clearLot():
            # add function to change building to empty lot
            pass

        if type(self.effects) == str:
            Label(text=self.effects, anchor='w', wraplength=100).grid(column=1, columnspan=2,row=r+1)
        else:
            for effect in self.effects:
                Label(text=effect, anchor='w').grid(column=1, columnspan=2,row=r+1)
                r+=1
        Button(building_info_frame, text='Upgrade!', command=(upgrade)).grid(column=1, columnspan=2,row=r+2)
        Button(building_info_frame, text='Destroy', command=(clearLot)).grid(column=1, columnspan=2,row=r+3)

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


class BuyBuilding(InfoPane):
    def __init__(self, lot):
        InfoPane.__init__(self, 'Construct New Building')
        construct_frame = Tk()
        construct_frame.title(self.title)
        r=1
        def buy1():
            if global_vars.university.buy(building1.constructionCost):
                global_vars.map.construct_building(lot.pos, building1)
        def buy2():
            if global_vars.university.buy(building2.constructionCost):
                global_vars.map.construct_building(lot.pos, building2)
        def buy3():
            if global_vars.university.buy(building3.constructionCost):
                global_vars.map.construct_building(lot.pos, building3)

        def buy4():
            if global_vars.university.buy(building4.constructionCost):
                global_vars.map.construct_building(lot.pos, building4)

        def buy5():
            if global_vars.university.buy(building5.constructionCost):
                global_vars.map.construct_building(lot.pos, building5)

        def buy6():
            if global_vars.university.buy(building6.constructionCost):
                global_vars.map.construct_building(lot.pos, building6)

        def buy7():
            if global_vars.university.buy(building7.constructionCost):
                global_vars.map.construct_building(lot.pos, building7)

        building1 = Map.getList()[0]
        Label(text=building1 .name, anchor='center').grid(column=1, columnspan=2, row=r)
        Label(text=building1 .effects, anchor='center', wraplength=500).grid(column=1, columnspan=2, row=r+1)
        Label(text='Price: $'+str(building1.constructionCost)).grid(column=1, row=r+2)
        Label(text='Build Time: '+str(building1.constructionTime)+ ' months').grid(column=2, row=r+2)
        Button(construct_frame, text="Begin Construction", command=(buy1)).grid(column=1, columnspan=2, row=r+3)
        r+=4

        building2 = Map.getList()[1]
        Label(text=building2.name, anchor='center').grid(column=1, columnspan=2, row=r)
        Label(text=building2.effects, anchor='center', wraplength=500).grid(column=1, columnspan=2, row=r+1)
        Label(text='Price: $'+str(building2.constructionCost)).grid(column=1, row=r+2)
        Label(text='Build Time: '+str(building2.constructionTime)+ ' months').grid(column=2, row=r+2)
        Button(construct_frame, text="Begin Construction", command=(buy2)).grid(column=1, columnspan=2, row=r+3)
        r+=4

        building3 = Map.getList()[2]
        Label(text=building3.name, anchor='center').grid(column=1, columnspan=2, row=r)
        Label(text=building3.effects, anchor='center', wraplength=500).grid(column=1, columnspan=2, row=r+1)
        Label(text='Price: $'+str(building3.constructionCost)).grid(column=1, row=r+2)
        Label(text='Build Time: '+str(building3.constructionTime)+ ' months').grid(column=2, row=r+2)
        Button(construct_frame, text="Begin Construction", command=(buy3)).grid(column=1, columnspan=2, row=r+3)
        r+=4

        building4 = Map.getList()[3]
        Label(text=building4.name, anchor='center').grid(column=1, columnspan=2, row=r)
        Label(text=building4.effects, anchor='center', wraplength=500).grid(column=1, columnspan=2, row=r+1)
        Label(text='Price: $'+str(building4.constructionCost)).grid(column=1, row=r+2)
        Label(text='Build Time: '+str(building4.constructionTime)+ ' months').grid(column=2, row=r+2)
        Button(construct_frame, text="Begin Construction", command=(buy4)).grid(column=1, columnspan=2, row=r+3)
        r+=4

        building5 = Map.getList()[4]
        Label(text=building5.name, anchor='center').grid(column=1, columnspan=2, row=r)
        Label(text=building5.effects, anchor='center', wraplength=500).grid(column=1, columnspan=2, row=r+1)
        Label(text='Price: $'+str(building5.constructionCost)).grid(column=1, row=r+2)
        Label(text='Build Time: '+str(building5.constructionTime)+ ' months').grid(column=2, row=r+2)
        Button(construct_frame, text="Begin Construction", command=(buy5)).grid(column=1, columnspan=2, row=r+3)
        r+=4

        building6 = Map.getList()[5]
        Label(text=building6.name, anchor='center').grid(column=1, columnspan=2, row=r)
        Label(text=building6.effects, anchor='center', wraplength=500).grid(column=1, columnspan=2, row=r+1)
        Label(text='Price: $'+str(building6.constructionCost)).grid(column=1, row=r+2)
        Label(text='Build Time: '+str(building6.constructionTime)+ ' months').grid(column=2, row=r+2)
        Button(construct_frame, text="Begin Construction", command=(buy6)).grid(column=1, columnspan=2, row=r+3)
        r+=4

        building7 = Map.getList()[6]
        Label(text=building7.name, anchor='center').grid(column=1, columnspan=2, row=r)
        Label(text=building7.effects, anchor='center', wraplength=500).grid(column=1, columnspan=2, row=r+1)
        Label(text='Price: $'+str(building7.constructionCost)).grid(column=1, row=r+2)
        Label(text='Build Time: '+str(building7.constructionTime)+ ' months').grid(column=2, row=r+2)
        Button(construct_frame, text="Begin Construction", command=(buy7)).grid(column=1, columnspan=2, row=r+3)
        r+=4

        while True:
            try:
                construct_frame.update()
            except:
                break;


class UpgradeBuilding(InfoPane):
    def __init__(self, building):
        InfoPane.__init__(self, 'Upgrade Building')
        upgrade_frame = Tk()
        upgrade_frame.title(self.title)
        prog_map = global_vars.programs
        progs = prog_map[building.name]
        def buy1():
            progs[0].trigger()
            upgrade_frame.destroy()
        def buy2():
            progs[1].trigger()
            upgrade_frame.destroy()

        def buy3():
            progs[2].trigger()
            upgrade_frame.destroy()

        def buy4():
            progs[3].trigger()
            upgrade_frame.destroy()

        buycmd = [buy1, buy2, buy3, buy4]
        r=1; p=0
        for prog in progs:
            Label(upgrade_frame, text='Pick a program to implement in the '+str(building.name)).grid(column=1, row=r, columnspan=2)
            Label(upgrade_frame, text=prog.title).grid(column=1, row=r+1)
            Label(upgrade_frame, text=prog.desc).grid(column=1, columnspan=2, row=r+2)
            r+=4
            if prog.unlocked:
                Button(upgrade_frame, text="Implement this Program", command=(buycmd[p])).grid(column=1, columnspan=2, row=r+3)

            else: Label(upgrade_frame, text="Program already implemented").grid(column=1, columnspan=2, row=r+3)
            r+=4; p+=1

        while True:
            try:
                upgrade_frame.update()
            except:
                break;

class PauseMenu(InfoPane):
    def __init__(self):
        InfoPane.__init__(self, 'Game Paused')
        pause_frame = Tk()
        pause_frame.minsize(300, 300)
        pause_frame.geometry("500x500")
        pause_frame.title(self.title)
        Label(pause_frame, text='GAME IS PAUSED', font=('Arial', 20, 'bold')).grid(row=1,column=1)
        
        while True:
            try:
                pause_frame.update()
            except:
                break;

class InitialMessage():
    def __init__(self):
        Tk().wm_withdraw()  # to hide the main window
        messagebox.showinfo('Info',
                            'Congratulations! You have been elected President of a small land-grant University! Invest your resources wisely and grow your University!')
        self.name = simpledialog.askstring('Prompt', 'What is your University called?')
