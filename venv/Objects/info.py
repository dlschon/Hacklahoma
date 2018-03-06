import global_vars
from Objects.map import Map
import pyforms
from pyforms import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlLabel
from pyforms.controls import ControlButton
from pyforms.controls import ControlProgress
from pyforms.controls import ControlSlider
from pyforms.controls import ControlList
from pyforms.controls import ControlToolBox
import KeyStroker

university = global_vars.university

def wrap_text(string, line_width):
    str_list = []

    # Text wrap, preferring spaces
    while len(string) > line_width:
        cutoff = string.find(' ', line_width)
        if cutoff == -1:
            cutoff = 40
        str_list.append(string[:cutoff])
        string = string[cutoff:]
    # add the final section
    str_list.append(string)
    return str_list

class BuildingInfo(BaseWidget):

    pos = (200, 200)
    size = (200, 400)

    building = None

    def upgrade_click(self):
        UpgradeBuilding.building = self.building
        ub = UpgradeBuilding()
        ub.parent = self
        ub.show()

    def destroy_click(self):
        self.close()


    def __init__(self):
        super().__init__('Building Info')

        self.set_margin(10)

        self.formset = []

        self.formset.append(('Name', ' ', str(BuildingInfo.building.name)))
        self.formset.append(('Monthly Cost', ' ', '500'))
        self.formset.append(('Capacity', ' ', str(BuildingInfo.building.capacity)))
        self.formset.append('Effects:')

        effs = BuildingInfo.building.effects

        # Change a string into a list of string
        if type(effs) == str:
            if len(effs) > 40:
                effs = wrap_text(effs, 40)
            else:
                effs = [effs]

        for eff in effs:
            self.formset.append(str(eff))

        self.upgrade = ControlButton('Upgrade!')
        self.upgrade.value = self.upgrade_click
        self.formset.append('upgrade')
        self.destroy = ControlButton('Destroy')
        self.destroy.value = self.destroy_click
        self.formset.append('destroy')

class StudentInfo(BaseWidget):

    pos = (200,200)
    size = (600,400)

    def __init__(self):
        super().__init__('Student Info')

        self.set_margin(10)

        self.formset = []

        leftside = []

        leftside.append('Target GPA')
        self.slider = ControlSlider('', 2.5, 1.0, 4.0)
        leftside.append('slider')

        leftside.append('Current Enrollment: ')
        leftside.append(str(len(university.students)))

        leftside.append('Max Enrollment: ')
        leftside.append(str(university.capacity()))

        self.pbar = ControlProgress()
        self.pbar.min = 0
        self.pbar.max = university.capacity()
        self.pbar.value = len(university.students)
        leftside.append('pbar')

        leftside.append('Average GPA: ')
        # need to add grad_rate
        leftside.append('2.3')
        leftside.append('Graduation Rate: ')
        leftside.append(str(university.grad_rate))
        leftside.append('Average Morale: ')

        # need to add morale
        leftside.append('78%')

        # need to add morale to value
        self.morale_pbar = ControlProgress()
        self.morale_pbar.min = 0
        self.morale_pbar.max = 100
        self.morale_pbar.value = 78
        leftside.append('morale_pbar')


        self.mylist = ControlList('Students')
        self.mylist.horizontal_headers = ['Name', 'GPA', 'Morale']

        for student in university.students:
            self.mylist += (student.name, student.gpa, student.morale)

        self.formset.append((leftside, ' ', 'mylist'))



class MoneyInfo(BaseWidget):
    pos = (200, 200)
    size = (200, 400)

    def __init__(self):
        BaseWidget.__init__(self, "Money")

        self.set_margin(10)

        self.formset = []
        self.formset.append('Monthly Income: ')
        revenue, revenues = university.calcRevenue()
        expense, expenses = university.calcExpense()
        income = revenue + expense

        if income >= 0:
            self.formset.append((' ', '+ $'+str(income)))
        else:
            self.formset.append((' ', '- $'+str(-income)))
        self.formset.append('Revenues: ')
        self.formset.append((' ', '+$'+str(revenue)))
        r = 3
        for rev in revenues:
            self.formset.append((rev.description, ' ', '+$'+str(rev.value)))
            r+=1
        self.formset.append('Expenses: ')
        self.formset.append((' ', '-$'+str(-expense)))
        r+=1
        i = 0
        for exp in expenses:
            self.formset.append((exp.description, ' ', '-$'+str(-exp.value)))
            r+=1



class BuyBuilding(BaseWidget):

    lot = None
    pos = (200, 100)
    size = (400, 700)

    def __init__(self):
        super().__init__('Construct New Building')

        self.formset = []
        self.set_margin(10)
        lot = BuyBuilding.lot
        building_list = Map.getList()


        # Create list of functions to buy the buildings
        i = 0
        bboxes = []
        leftside = []

        self._buttons = [None]*7
        self.buyfuncs = [None]*7

        def get_buy_func(building):
            def buy():
                if global_vars.university.buy(building.constructionCost):
                    global_vars.map.construct_building(lot.pos, building)
                KeyStroker.AltF4()

            return buy

        for building in building_list:

            self.buyfuncs[i] = None
            #b1box = ControlToolBox()
            #b1box.value = []
            b1box = []
            b1box.append(building.name)
            effects = wrap_text(building.effects, 40)
            for eff in effects:
                b1box.append(eff)
            b1box.append('Price: $'+str(building.constructionCost))
            b1box.append('Build Time: '+str(building.constructionTime)+ ' months')
            buy_button = ControlButton("Begin Construction")
            buy_button.value = get_buy_func(building)
            self._buttons[i] = buy_button

            b1box.append('_button' + str(i+1))
            bboxes.append(b1box)

            if i%2 == 0:
                leftside = bboxes[i]
            else:
                self.formset.append((leftside, ' ', bboxes[i]))
            i+=1

        self._button1 = self._buttons[0]
        self._button2 = self._buttons[1]
        self._button3 = self._buttons[2]
        self._button4 = self._buttons[3]
        self._button5 = self._buttons[4]
        self._button6 = self._buttons[5]
        self._button7 = self._buttons[6]


class UpgradeBuilding(BaseWidget):

    pos = (200,200)
    size = (400, 400)

    building = None

    def __init__(self):
        super().__init__('Upgrade Building')

        self.formset = []
        prog_map = global_vars.programs
        building = UpgradeBuilding.building

        progs = prog_map[building.name]
        def buy1():
            progs[0].trigger()
            KeyStroker.AltF4()
        def buy2():
            progs[1].trigger()
            KeyStroker.AltF4()

        def buy3():
            progs[2].trigger()
            KeyStroker.AltF4()

        def buy4():
            progs[3].trigger()
            KeyStroker.AltF4()

        buycmd = [buy1, buy2, buy3, buy4]
        buttons = [None,None,None,None]

        b = ControlButton("test")
        print(b)

        def get_buy_func(index):
            return buycmd[index]

        p=0
        self.formset.append('Pick a program to implement in the '+str(building.name))
        for prog in progs:
            self.formset.append(prog.title)
            self.formset.append(prog.desc)

            if prog.unlocked:
                button = ControlButton("Implement this program")
                button.value = get_buy_func(p)
                buttons[p] = button
                self.formset.append('_button'+str(p+1))
            else:
                self.formset.append("Program already implemented")
            p+=1

        self._button1 = buttons[0]
        self._button2 = buttons[1]
        self._button3 = buttons[2]
        self._button4 = buttons[3]


class TeacherMenu(BaseWidget):

    pos = (200, 200)
    size = (400, 200)
    teacher = None

    def __init__(self):
        super().__init__('Teachers')

        self.set_margin(10)
        self.formset = []
        university = global_vars.university
        teacher = TeacherMenu.teacher

        def hire():
            university.can_hire = False
            teacher.hire()
            KeyStroker.AltF4()
        def skip():
            university.can_hire = False
            KeyStroker.AltF4()

        if not(university.can_hire and len(university.teachers) < university.max_teachers()):
            self.formset.append('Sorry, you may not hire more teachers at this time')
        else:
            self.formset.append('You may hire a new teacher!')
            self.formset.append('Name: Dr. ' + teacher.name)
            self.formset.append('Monthly Salary: $' + str(teacher.salary))
            self.formset.append('Research Rating: ' + str(teacher.research))
            self.formset.append('Teaching Rating: ' + str(teacher.teaching))
            self._hirebutton = ControlButton('Hire')
            self._hirebutton.value = hire
            self._passbutton = ControlButton('Pass')
            self._passbutton.value = skip
            self.formset.append(('_hirebutton', ' ', '_passbutton'))

class AskDialog(BaseWidget):

    title = "prompt"
    question = "question"
    answer = ""

    def OK_press(self):
        AskDialog.answer = self._answer.value
        KeyStroker.AltF4()

    def __init__(self):
        super().__init__('Prompt')
        self.set_margin(10)

        self.formset = []

        if (type(AskDialog.question) == str):
            self._question = ControlLabel(AskDialog.question)
            self.formset.append('_question')
        else:
            for string in AskDialog.question:
                self.formset.append(string)
        self._answer = ControlText('', AskDialog.answer)
        self.formset.append('_answer')
        self._button = ControlButton('OK')
        self.formset.append('_button')
        self._button.value = self.OK_press

class MessageDialog(BaseWidget):

    message = "message"
    pos = (400, 400)
    size = (0,0)

    def OK_press(self):
        KeyStroker.AltF4()

    def __init__(self):
        super().__init__('Prompt')
        self.set_margin(10)

        self.formset = []
        message = wrap_text(MessageDialog.message, 40);
        for line in message:
            self.formset.append(line)
        self._ok = ControlButton('Unpause')
        self._ok.value = self.OK_press
        self.formset.append('_ok')


class InitialMessage():
    def __init__(self):
        AskDialog.title = "Welcome!"
        AskDialog.question = ["Congratulations! You have been elected President  ",
                            "of a small land-grant University! Invest your",
                            "resources wisely and grow your University!"]
        pyforms.start_app(AskDialog, geometry=(400,400,0,0))
        self.name = AskDialog.answer
