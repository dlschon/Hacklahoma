from tkinter import *
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
        self.buttons = [

        ]

    def makeform(self, root):
        entries = []
        for label, value in zip(self.labels, self.values):
            row = Frame(root)
            lab = Label(row, width=15, text=label)
            val = Label(row, text=value)
            row.pack(side=TOP, fill=X, padx=5, pady=5)
            lab.pack(side=LEFT)
            val.pack(side=RIGHT, expand=YES, fill=X)
            entries.append((lab, val))
        row = Frame(root)
        lab = Label(row, width=15, text='Effects', anchor='w')
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        for effect in self.effects:
            row = Frame(root)
            lab = Label(row, width=15, text=effect, anchor='w')
            row.pack(side=TOP, fill=X, padx=5, pady=1)
            lab.pack(side=LEFT, padx=15)
        return entries


building1 = Building('test','test','test','test','test','test','test','test')
obj = BuildingInfo(building1)




root = Tk()
obj.makeform(root)
b1 = Button(root, text='Upgrade!', command=())
b1.pack(side=BOTTOM, padx=5, pady=10)
b2 = Button(root, text='Destroy', command=())
b2.pack(side=BOTTOM, padx=5, pady=5)

root.mainloop()
