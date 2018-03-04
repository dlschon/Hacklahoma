from tkinter import *
from Objects.building import Building

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
        for effect in self.effects:
            row = Frame(building_info_frame)
            lab = Label(row, width=15, text=effect, anchor='w')
            row.pack(side=TOP, fill=X, padx=5, pady=1)
            lab.pack(side=LEFT, padx=15)
        b2 = Button(building_info_frame, text='Destroy', command=())
        b2.pack(side=BOTTOM, padx=5, pady=5)
        b1 = Button(building_info_frame, text='Upgrade!', command=())
        b1.pack(side=BOTTOM, padx=5, pady=10)
        info_open = True;

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
        lbl = Label(text='Target GPA')
        lbl.grid(column=1, row=1)


        student_info_frame.mainloop()

