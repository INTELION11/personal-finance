import tkinter as tk
from tkinter import ttk
import csv
from piechart import piechart
LARGEFONT = ("Verdana", 35)
 
 
def _currency(money, option):
    try:
        from forex_python.converter import CurrencyRates
        c = CurrencyRates()
        if option in ("1", "yen"):
            return f"{c.convert('USD', 'JPY', money):.2f} Yen (live)"
        elif option in ("2", "usa", "usd"):
            return f"${money:.2f} USD (live)"
        elif option in ("3", "pound"):
            return f"£{c.convert('USD', 'GBP', money):.2f} Pound (live)"
        else:
            return f"${money:.2f} USD (live)"
    except :
        if option in ("1", "yen"):
            return f"{money * 150:.2f} Yen (backup)"
        elif option in ("2", "usa", "usd"):
            return f"${money:.2f} USD (backup)"
        elif option in ("3", "pound"):
            return f"£{money * 0.8:.2f} Pound (backup)"
        else:
            return f"${money:.2f} USD (backup)"
def _load_income(username):

    try:
        with open("finance_program/documents/income.csv", mode="r", newline="") as f:
            for line in csv.reader(f):
                if line and line[0] == username:
                    if len(line) >= 2 and line[1] != "":
                        try:
                            return float(line[1])
                        except ValueError:
                            return None
    except FileNotFoundError:
        pass
    return None
def _save_income(username, income):
    income_file = "finance_program/documents/income.csv"
    users = []
    found = False
    try:
        with open(income_file, mode="r", newline="") as f:
            for line in csv.reader(f):
                if line and line[0] == username:
                    users.append([username, str(income)])
                    found = True
                else:
                    users.append(line)
    except FileNotFoundError:
        pass
    if not found:
        users.append([username, str(income)])
    with open(income_file, mode="w", newline="") as f:
        csv.writer(f).writerows(users)
        
class Budgeting(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.budget_info = {}
        self.income = None
        self.currency_var = tk.StringVar(value="2")

        ttk.Label(self, text="Budgeting", font=LARGEFONT).pack(pady=(20, 10))

        self.status_label = tk.Label(self, text="", font=("Helvetica", 13),
                                     wraplength=850, justify="center")
        self.status_label.pack(pady=(0, 6))
 
        income_frame = tk.Frame(self)
        income_frame.pack(pady=4)
 
        tk.Label(income_frame, text="Yearly income ($):",
                 font=("Helvetica", 13)).grid(row=0, column=0, padx=6)
        self.income_entry = tk.Entry(income_frame, width=18,
                                     font=("Helvetica", 13), bg="white")
        self.income_entry.grid(row=0, column=1, padx=6)
        tk.Button(income_frame, text="Set Income",
                  font=("Helvetica", 12), bd=3, bg="white",
                  activebackground="grey", activeforeground="white",
                  overrelief="solid",
                  command=self._set_income).grid(row=0, column=2, padx=6)
 
    
        cur_frame = tk.Frame(self)
        cur_frame.pack(pady=4)
        tk.Label(cur_frame, text="Currency:",
                 font=("Helvetica", 13)).pack(side="left", padx=6)
        for text, val in [("USD", "2"), ("Yen", "1"), ("Pound", "3")]:
            tk.Radiobutton(cur_frame, text=text, variable=self.currency_var,
                           value=val, font=("Helvetica", 12)).pack(side="left", padx=4)
 

        list_frame = tk.Frame(self, bd=2, relief="groove")
        list_frame.pack(fill="both", expand=True, padx=40, pady=6)
 
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")
 
        self.listbox = tk.Listbox(list_frame, font=("Helvetica", 13),
                                  yscrollcommand=scrollbar.set,
                                  selectmode="single", height=8)
        self.listbox.pack(fill="both", expand=True)
        scrollbar.config(command=self.listbox.yview)
 

        edit_frame = tk.Frame(self)
        edit_frame.pack(pady=4)
 
        tk.Label(edit_frame, text="Category:",
                 font=("Helvetica", 12)).grid(row=0, column=0, padx=4)
        self.cat_entry = tk.Entry(edit_frame, width=20,
                                  font=("Helvetica", 12), bg="white")
        self.cat_entry.grid(row=0, column=1, padx=4)
 
        tk.Label(edit_frame, text="% (or new name for Rename):",
                 font=("Helvetica", 12)).grid(row=0, column=2, padx=4)
        self.pct_entry = tk.Entry(edit_frame, width=14,
                                  font=("Helvetica", 12), bg="white")
        self.pct_entry.grid(row=0, column=3, padx=4)
 
        btn_cfg = dict(font=("Helvetica", 11), bd=3, bg="white",
                       activebackground="grey", activeforeground="white",
                       overrelief="solid", width=12, height=2)
 
        tk.Button(edit_frame, text="Add",
                  command=self._add,        **btn_cfg).grid(row=1, column=0, padx=4, pady=6)
        tk.Button(edit_frame, text="Change %",
                  command=self._change_pct, **btn_cfg).grid(row=1, column=1, padx=4, pady=6)
        tk.Button(edit_frame, text="Rename",
                  command=self._rename,     **btn_cfg).grid(row=1, column=2, padx=4, pady=6)
        tk.Button(edit_frame, text="Remove",
                  command=self._remove,     **btn_cfg).grid(row=1, column=3, padx=4, pady=6)
 

        action_frame = tk.Frame(self)
        action_frame.pack(pady=6)
 
        big_btn = dict(font=("Helvetica", 13), bd=4, bg="white",
                       activebackground="grey", activeforeground="white",
                       overrelief="solid", width=22, height=3)
 
        tk.Button(action_frame, text="Show Budget",
                  command=self._show_budget,   **big_btn).grid(row=0, column=0, padx=10)
        tk.Button(action_frame, text="Save & Back",
                  command=self._save_and_back, **big_btn).grid(row=0, column=1, padx=10)

        tk.Button(self, text="Back", width=15, height=3,
                  font=("Helvetica", 8), bd=5, bg="white",
                  activebackground="grey", activeforeground="white",
                  overrelief="solid",
                  command=lambda: controller.show_frame("MainMenu")
                  ).pack(anchor="sw", padx=30, pady=(4, 20), side="left")
    def _budget_file(self):
        return f"finance_program/documents/budget_{self.controller.current_user}.csv"
 
    def _load_csv(self):
        self.budget_info = {}
        try:
            with open(self._budget_file(), mode="r") as f:
                for line in csv.reader(f):
                    if len(line) >= 2:
                        self.budget_info[line[0]] = float(line[1])
        except FileNotFoundError:
            open(self._budget_file(), "w").close()
 
    def _save_csv(self):
        with open(self._budget_file(), mode="w", newline="") as f:
            writer = csv.writer(f)
            for cat, pct in self.budget_info.items():
                writer.writerow([cat, pct])
 
    def _refresh_listbox(self):
        self.listbox.delete(0, "end")
        total = sum(self.budget_info.values())
        for cat, pct in self.budget_info.items():
            self.listbox.insert("end", f"{cat}:  {pct}%")
        if self.budget_info:
            self.listbox.insert("end", "─────────────────────────")
            self.listbox.insert("end",
                f"Total: {total:.1f}%   |   Remaining: {100 - total:.1f}%")
 
    def _status(self, msg, color="red"):
        self.status_label.config(text=msg, fg=color)
 

 
    def tkraise(self, *args, **kwargs):
        super().tkraise(*args, **kwargs)
        self._load_csv()
        stored = _load_income(self.controller.current_user)
        if stored is not None:
            self.income = stored
            self.income_entry.delete(0, "end")
            self.income_entry.insert(0, str(stored))
        self._refresh_listbox()
        self._status("")

 
    def _set_income(self):
        try:
            val = float(self.income_entry.get().strip())
            self.income = val
            _save_income(self.controller.current_user, val)
            self._status(f"Income set to ${val:,.2f}/yr", "green")
        except ValueError:
            self._status("Enter a valid number for income.")
 
    def _add(self):
        cat = self.cat_entry.get().strip()
        if not cat:
            self._status("Enter a category name.")
            return
        try:
            pct = float(self.pct_entry.get().strip())
        except ValueError:
            self._status("Enter a valid percentage.")
            return
        if cat in self.budget_info:
            self._status(f"'{cat}' already exists. Use Change % or Rename.")
            return
        if sum(self.budget_info.values()) + pct > 100:
            self._status("Can't go over 100% total.")
            return
        self.budget_info[cat] = pct
        self._refresh_listbox()
        self._status(f"Added '{cat}' at {pct}%", "green")
 
    def _change_pct(self):
        cat = self.cat_entry.get().strip()
        if cat not in self.budget_info:
            self._status(f"'{cat}' not found.")
            return
        try:
            new_pct = float(self.pct_entry.get().strip())
        except ValueError:
            self._status("Enter a valid percentage.")
            return
        rest = sum(self.budget_info.values()) - self.budget_info[cat]
        if rest + new_pct > 100:
            self._status("Can't go over 100% total.")
            return
        self.budget_info[cat] = new_pct
        self._refresh_listbox()
        self._status(f"Updated '{cat}' to {new_pct}%", "green")
 
    def _rename(self):
        old = self.cat_entry.get().strip()
        new = self.pct_entry.get().strip()
        if not new:
            self._status("Put the new name in the % / new name field.")
            return
        if old not in self.budget_info:
            self._status(f"'{old}' not found.")
            return
        self.budget_info[new] = self.budget_info.pop(old)
        self._refresh_listbox()
        self._status(f"Renamed '{old}' → '{new}'", "green")
 
    def _remove(self):
        cat = self.cat_entry.get().strip()
        if cat in self.budget_info:
            del self.budget_info[cat]
            self._refresh_listbox()
            self._status(f"Removed '{cat}'", "green")
        else:
            self._status(f"'{cat}' not found.")
 
    def _show_budget(self):
        if self.income is None:
            self._status("Set your yearly income first.")
            return
        if not self.budget_info:
            self._status("No categories yet. Add some first.")
            return
        cur_opt = self.currency_var.get()
        lines = []
        category=[]
        data =[]
        for cat, pct in self.budget_info.items():
            amount = self.income * (pct / 100)
            lines.append(f"{cat}: {_currency(amount, cur_opt)}")
            category.append(cat)
            data.append(pct)
        piechart(category,data)
        self._status("  |  ".join(lines), "blue")
        
        self._save_csv()
 
    def _save_and_back(self):
        self._save_csv()
        self._status("Saved!", "green")
        self.controller.after(800, lambda: self.controller.show_frame("MainMenu"))
