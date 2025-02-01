from view.component import *
from view.units_info_view import UnitsInfoView
from view.expenses_view import ExpensesView

class AdminPanelView:
    def units_info_click(self):
        units_win = UnitsInfoView()


    def expenses_click(self):
        expenses_win = ExpensesView()

    def __init__(self):
        self.win = Tk()
        self.win.title("Admin Panel")
        self.win.geometry("250x260")
        self.win.resizable(width=False, height=False)


        Label(self.win, text="Welcome Admin!",bg="red",fg="white", font="Arial, 12").place(x=63, y=20)

        Button(self.win, text="Units Info", width=14, height=3,command=self.units_info_click, font="Arial, 11").place(x=56, y=65)
        Button(self.win, text="Expenses", width=14, height=3,command=self.expenses_click, font="Arial, 11").place(x=56, y=150)

        self.win.mainloop()

# a = AdminPanelView()