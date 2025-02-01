from model.entity import UnitUserConnector, Users, Units
from view.component import *
from controller.user_panel_controller import *



class UserPanelView:
    def read_data(self):
        result_list = expense_calculator(self.resident_count)
        # status, expense_list = find_all()
        #
        # for item in expense_list:
        #     item.water = int((item.water / sum_residents()) * self.resident_count),
        #     item.electricity = int((item.electricity / sum_residents()) * self.resident_count),
        #     item.gas = int((item.gas / sum_residents()) * self.resident_count),
        #     item.elevator = int((item.elevator / sum_residents()) * self.resident_count),
        #     item.cleaning = int((item.cleaning / sum_residents()) * self.resident_count),
        #     item.engine_room = int((item.engine_room / sum_residents()) * self.resident_count),
        #     item.other = int((item.other / sum_residents()) * self.resident_count)

        self.table.refresh_table(result_list)

    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.win = Tk()
        self.win.title("User Panel")
        self.win.geometry("792x500")
        self.win.resizable(False, False)
        # ----------------------------------------------------
        # dar table users be donbale useri migarde ke username va password vared shode dar safhe login ro shamel bashe
        user_da = DataAccess(Users)
        user = user_da.find_by((Users._username == self.username) &
                               (Users._password == self.password))
        # id user peyda shode ro barmidare va dar user_id mirize
        user_id = user[0].id

        # dar table unit_user_connector be donbale satri migarde ke shamel user_id peyda shode bashe
        connector_da = DataAccess(UnitUserConnector)
        unit_user_item = connector_da.find_by(UnitUserConnector.user_id == user_id)
        # dar satre peyda shode id unit marbote ro bar midare va dar unit_id mirize
        unit_id = unit_user_item[0].unit_id

        # dar table units be donbale uniti migarde ke shamel unit_id peyda shode bashe
        unit_da = DataAccess(Units)
        unit = unit_da.find_by_id(unit_id)
        # ba tavajoh be unit peyda shode, ajzaye on unit(mesle shomare vahed, esm, famil, tedad afrad saken) ro dar motaghayer haye jodagone mirize baraye estefade dar ayande...
        self.unit_no = unit.unit_no
        self.first_name = unit.name
        self.family_name = unit.family
        self.resident_count = unit.no_people
        # ----------------------------------------------------

        Label(self.win, text=f"Welcome {self.first_name} {self.family_name}!", font=("Arial, 18"), bg="lightgray", border="15").place(x=230, y=15)
        LabelAndEntry(self.win, "Unit Number", 80, 100, state="readonly").variable.set(self.unit_no)
        LabelAndEntry(self.win, "Residents Count", 450, 100, 100,state="readonly").variable.set(self.resident_count)

        self.table = Table(self.win,
              ["Id","month", "water", "electricity", "gas", "elevator", "cleaning", "engine_room", "other", "total"],
              [40, 80, 80, 80, 80, 80, 80, 80, 80, 80],
              300, 15, 130)


        self.read_data()


        self.win.mainloop()



# a = UserPanelView("username1", "password1")
