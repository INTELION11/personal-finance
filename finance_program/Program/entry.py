import tkinter as tk
from tkinter import messagebox
import csv
import os
from datetime import datetime
 
 
def save_entry(username, row):
    entries_file = f"finance_program/documents/entries_{username}.csv"
    with open(entries_file, newline="", mode="a") as file:
        csv.writer(file).writerow(row)
def load_budget(username):
    budget = {}
    try:
        with open(f"finance_program/documents/budget_{username}.csv", mode="r") as file:
            for line in csv.reader(file):
                if len(line) >= 2:
                    budget[line[0]] = float(line[1])
    except FileNotFoundError:
        pass
    return budget
class IncomeTracking(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.budget = {}
        self.income = 0.0
        self.pending_entries = []  # logged this session, not yet flushed
        self.build_ui()
 
    def get_user(self):
        return getattr(self.controller, "current_user", "test_user")
 
    def build_ui(self):
        tk.Label(self, text="Income & Expense Tracker", font=("Helvetica", 20)).pack(pady=20)
 
        tk.Label(self, text="Date (YYYY-MM-DD)").pack(pady=5)
        self.date_entry = tk.Entry(self, width=40)
        self.date_entry.pack(pady=5)
 
        tk.Label(self, text="Income for this Entry ($)").pack(pady=5)
        self.income_entry = tk.Entry(self, width=40)
        self.income_entry.pack(pady=5)
 
        tk.Button(self, text="Load Budget Categories", width=40, height=2,
                  command=self.load_categories).pack(pady=10)
 
        tk.Label(self, text="Your Categories").pack(pady=10)
        self.goal_listbox = tk.Listbox(self, width=60, height=8)
        self.goal_listbox.pack(pady=5)
 
        tk.Label(self, text="Actually Spent ($)").pack(pady=10)
        self.add_money_entry = tk.Entry(self, width=40)
        self.add_money_entry.pack(pady=5)
 
        tk.Button(self, text="Log Spending for Selected Category", width=40, height=2,
                  command=self.log_spending).pack(pady=10)
 
        tk.Button(self, text="Back", width=20, height=2,
                  command=self.save_and_back).pack(pady=20)
 
    def tkraise(self, *args, **kwargs):
        super().tkraise(*args, **kwargs)
        self.date_entry.delete(0, tk.END)
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.income_entry.delete(0, tk.END)
        self.add_money_entry.delete(0, tk.END)
        self.pending_entries = []
        self.budget = load_budget(self.get_user())
        self._refresh_listbox()
 
    def _refresh_listbox(self):
        self.goal_listbox.delete(0, tk.END)
        if not self.budget:
            self.goal_listbox.insert(tk.END, "No budget found. Set up your budget first!")
            return
        for cat, pct in self.budget.items():
            try:
                should = self.income * (pct / 100)
                self.goal_listbox.insert(tk.END, f"{cat}: should spend ${should:.2f}")
            except Exception:
                self.goal_listbox.insert(tk.END, f"{cat}: enter income above first")
 
    def load_categories(self):
        try:
            self.income = float(self.income_entry.get().strip())
            if self.income <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Enter a valid income amount first.")
            return
        self.budget = load_budget(self.get_user())
        if not self.budget:
            messagebox.showerror("Error", "No budget found. Set up your budget first!")
            return
        self._refresh_listbox()
 
    def log_spending(self):
        selection = self.goal_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Select a category first.")
            return
        try:
            spent = float(self.add_money_entry.get())
            if spent < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Enter a valid amount.")
            return
        if not self.income:
            messagebox.showerror("Error", "Load categories with an income first.")
            return
 
        cat = list(self.budget.keys())[selection[0]]
        should = self.income * (self.budget[cat] / 100)
        date = self.date_entry.get().strip()
        row = [date, self.income, cat, f"{should:.2f}", f"{spent:.2f}"]
 
        self.pending_entries.append(row)
        messagebox.showinfo("Logged", f"Logged ${spent:.2f} for '{cat}' — will save when you go Back.")
        self.add_money_entry.delete(0, tk.END)
 
    def save_and_back(self):
        # flush all pending entries to csv then navigate away
        for row in self.pending_entries:
            save_entry(self.get_user(), row)
        self.pending_entries = []
        self.controller.show_frame("MainMenu")