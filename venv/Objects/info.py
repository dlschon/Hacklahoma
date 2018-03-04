from tkinter import *
from tkinter import ttk
from building import Building

class InfoPane:
    def __init__(self, title):
        self.title = title

class BuildingInfo(InfoPane):
    def __init__(self, building):
        InfoPane.__init__(self, 'Building Info')
        self.labels = [
            'Name',
            'Type',
            'Level',
            'Monthly Cost',
            'Capacity'
        ]
        self.values = [
            building.name,
            building.type,
            building.level,
            building.monthlyCost,
            building.capacity + ' students'
        ]
        self.effects = [
            '+3 morale/student',
            '+10 reputation',
            '+$2000/month'
        ]
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

        building_info_frame.mainloop()


class StudentInfo(InfoPane):
    def __init__(self):
        InfoPane.__init__(self, 'Student Info')
        student_info_frame = Tk()
        student_info_frame.title(self.title)
        lbl = Label(text='Target GPA')
        lbl.grid(column=1, row=1, columnspan=2, pady=(10,0))
        slider = Scale(from_=2.0, to=4.0, orient=HORIZONTAL, resolution=0.1, length=400)
        # Arbitrarily set to 2.8, need to add set(curr_val)
        slider.set(2.8)
        slider.grid(column=1, row=2, columnspan=2, pady=(0,15))
        lbl = Label(text='Current Enrollment: ', anchor='w')
        lbl.grid(column=1, row=3)
        # Arbitrarily set to 50, need to set(curr_val)
        lbl = Label(text=50, anchor='e')
        lbl.grid(column=2, row=3)
        lbl = Label(text='Max Enrollment: ', anchor='w')
        lbl.grid(column=1, row=4)
        # Arbitrarily set to 150, need to set(curr_val)
        lbl = Label(text=150, anchor='e')
        lbl.grid(column=2, row=4)
        # Arbitrarily set to 50/150, need to set(curr_val)
        pbar = ttk.Progressbar(orient=HORIZONTAL, length=300, mode='determinate', value=(50/150*100))
        pbar.grid(column=1, row=5, columnspan=2, pady=(0,15))
        lbl = Label(text='Average GPA: ')
        lbl.grid(column=1, row=6, pady=15)
        lbl = Label(text=2.3)
        lbl.grid(column=2, row=6, pady=15)
        lbl = Label(text='Graduation Rate: ')
        lbl.grid(column=1, row=7, pady=15)
        lbl = Label(text='70%')
        lbl.grid(column=2, row=7, pady=15)
        lbl = Label(text='Average Morale: ')
        lbl.grid(column=1, row=8, pady=(15,0))
        lbl = Label(text='78%')
        lbl.grid(column=2, row=8, pady=(15,0))
        pbar = ttk.Progressbar(orient=HORIZONTAL, length=300, mode='determinate', value=(78))
        pbar.grid(column=1, row=9, columnspan=2, pady=(0,15))

        student_info_frame.mainloop()


        

building1 = Building('test','test','test','test','test','test','test', 'test')
obj = StudentInfo()