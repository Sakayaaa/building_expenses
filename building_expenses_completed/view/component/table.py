from tkinter import ttk, END

class Table:
    def __init__(self, master, headers, widths, table_height, x, y, select_function=None):
        self.master = master
        self.x = x
        self.y = y
        self.headers = headers
        self.widths = widths
        self.table_height = table_height
        self.select_function = select_function
        self.columns = list(range(len(headers)))

        self.table = ttk.Treeview(self.master, columns=self.columns, show="headings")
        for col in self.columns:
            self.table.column(col, width=self.widths[col])
            self.table.heading(col, text=self.headers[col])

        self.table.bind("<ButtonRelease>", self.select_table)
        self.table.bind("<KeyRelease>", self.select_table)
        self.table.place(x=x, y=y, height=table_height)

    def refresh_table(self, data_list):
        # ۱. پاک کردن داده‌های قبلی
        for item in self.table.get_children():
            self.table.delete(item)

        # ۲. اگر داده‌ای هست، تک‌تک در جدول درج کن
        if data_list:
            for data in data_list:
                # اگر شیء entity است و متد to_tuple دارد
                if hasattr(data, "to_tuple"):
                    values = tuple(data.to_tuple())
                # وگرنه فرض کن خود data یک tuple است
                else:
                    values = tuple(data)
                self.table.insert("", END, values=values)

    def select_table(self, event):
        data = self.table.item(self.table.focus())["values"]
        if self.select_function:
            self.select_function(data)
