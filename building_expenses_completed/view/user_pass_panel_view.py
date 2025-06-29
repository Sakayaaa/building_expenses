from view.component import *
from tkinter import ttk
import tkinter as tk
from controller.user_pass_panel_controller import *

class UserPassPanelView:
    def unit_no_value_setter(self):
        status, unit_number_list = get_unit_no()
        if status:
            return unit_number_list

    def save_click(self):
        status, data = save(
            self.username.variable.get(),
            self.password.variable.get(),
            self.role.get(),
            self.unit_no.get()
        )
        if status:
            msg.showinfo("Save", f"User Saved\n{data}")
            self.reset_form()
        else:
            msg.showerror("Save Error", f"Error\n{data}")

    def edit_click(self):
        status, data = edit(
            self.id.variable.get(),
            self.username.variable.get(),
            self.password.variable.get(),
            self.role.get(),
            self.unit_no.get()  # اضافه شد
        )
        if status:
            msg.showinfo("Edit", f"User Edited\n{data}")
            self.reset_form()
        else:
            msg.showerror("Edit Error", f"Error\n{data}")

    def remove_click(self):
        status, data = remove(self.id.variable.get())
        if status:
            msg.showinfo("Remove", f"User Removed\n{data}")
            self.reset_form()
        else:
            msg.showerror("Remove Error", f"Error\n{data}")

    def reset_form(self):
        # ۱. پاک‌کردن فرم
        self.username.variable.set("")
        self.password.variable.set("")
        self.role.set("")
        self.unit_no.set("")

        # ۲. بارگذاری لیست کاربران
        status_u, users = find_all_users()
        if not status_u:
            msg.showerror("Error", f"Can't load users:\n{users}")
            return

        # ۳. بارگذاری لیست شماره واحدها
        status_t, unit_no_list = table_unit_no()
        if not status_t:
            msg.showerror("Error", f"Can't load unit numbers:\n{unit_no_list}")
            return

        # ۴. قرار دادن یک عنصر خالی در ابتدای لیست برای Admin
        unit_no_list.insert(0, "")

        # ۵. ساخت لیست داده‌ها با چک کردن وجود ایندکس
        combined = []
        for i in range(len(users)):
            user = users[i]
            base = list(user.to_tuple())  # [id, username, password, role]

            # اگر unit_no_list آیتمی در اندیس i داشته باشد، اضافه کن
            if i < len(unit_no_list):
                base.append(unit_no_list[i])
            else:
                base.append("")  # در غیر این صورت خالی بگذار

            combined.append(tuple(base))

        # ۶. رفرش جدول با داده‌های جدید
        self.table.refresh_table(combined)

    def select_table(self, selected_user):
        self.id.variable.set(selected_user[0])
        self.username.variable.set(selected_user[1])
        self.password.variable.set(selected_user[2])
        self.role.set(selected_user[3])
        self.unit_no.set(selected_user[4])

    def __init__(self):
        self.win = Toplevel()
        self.win.title("User Password Panel")
        self.win.geometry("890x420")
        self.win.resizable(width=False, height=False)


        self.id = LabelAndEntry(self.win, "Id", 20, 20, state="readonly")
        self.username = LabelAndEntry(self.win, "Username", 20, 100)
        self.password = LabelAndEntry(self.win, "Password", 20, 180)

        # Role Combo Box
        tk.Label(self.win, text="Role").place(x=20, y=260)
        self.role = tk.StringVar()
        self.role_choosen = ttk.Combobox(self.win, state="readonly", textvariable=self.role, values=('admin', 'user'), width=18).place(x=100, y=260)

        # Unit No. Combo Box
        tk.Label(self.win, text="Unit No.").place(x=20, y=340)
        self.unit_no = tk.StringVar()
        self.unit_no_list = self.unit_no_value_setter()
        self.unit_no_choosen = ttk.Combobox(self.win, state="readonly", textvariable=self.unit_no, values=(self.unit_no_list),
                                         width=18).place(x=100, y=340)

        self.table_headers_list = ['Id', 'Username', 'Password', 'Role', 'Unit No']
        self.table = Table(
            self.win,
            self.table_headers_list,
            [80,140,140,140,80],
            300,
            300,20,
            self.select_table
        )

        TkButton(self.win, "Save", self.save_click, 330, 350, height=45)
        TkButton(self.win, "Edit", self.edit_click, 440, 350, height=45)
        TkButton(self.win, "Remove", self.remove_click, 550, 350, height=45)
        TkButton(self.win, "Refresh", self.reset_form, 660, 350, height=45)

        self.reset_form()

        self.win.mainloop()

# a = UserPassPanelView()