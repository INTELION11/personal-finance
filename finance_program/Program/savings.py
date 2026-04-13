import tkinter as tk
from tkinter import messagebox
import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)

csv_file = os.path.join(PROJECT_DIR, "documents", "savings_goals.csv")
csv_file = os.path.normpath(csv_file)

#Functon for loafing the stuff
def load_goals():
    goals = []
    if not os.path.exists(csv_file):
        return goals

    with open(csv_file, newline="", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            goals.append(row)
    return goals

#function for save goals
def save_goals(goals):
    with open(csv_file, newline="", mode="w") as file:
        writer = csv.writer(file)
        writer.writerows(goals)
        

#make a class for savings
class Savings(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        self.build_ui()
        self.refresh_goal_list()

    def get_user(self):
        return getattr(self.controller, "current_user", "test_user")
    

    #make the ui
    def build_ui(self):

        tk.Label(self, text="Savings Goal Tracker", font=("Helvetica", 20)).pack(pady=20)

        # new goal
        tk.Label(self, text="Goal Name").pack(pady=5)
        self.goal_name_entry = tk.Entry(self, width=40)
        self.goal_name_entry.pack(pady=5)

        tk.Label(self, text="Goal Amount ($)").pack(pady=5)
        self.goal_amount_entry = tk.Entry(self, width=40)
        self.goal_amount_entry.pack(pady=5)

        tk.Button(
            self,
            text="Make New Goal",
            width=40,
            height=2,
            command=self.make_new_goal
        ).pack(pady=10)

        # list of goals
        tk.Label(self, text="Your Savings Goals").pack(pady=10)

        self.goal_listbox = tk.Listbox(self, width=60, height=8)
        self.goal_listbox.pack(pady=5)

        # adding money
        tk.Label(self, text="Add Money ($)").pack(pady=10)
        self.add_money_entry = tk.Entry(self, width=40)
        self.add_money_entry.pack(pady=5)

        tk.Button(
            self,
            text="Add to Selected Goal",
            width=40,
            height=2,
            command=self.add_money
        ).pack(pady=10)

        tk.Button(
            self,
            text="Back",
            width=20,
            height=2,
            command=lambda: self.controller.show_frame("MainMenu")
        ).pack(pady=20)

    #FUnction for making new goal
    def make_new_goal(self):
        name = self.goal_name_entry.get().strip()

        try:
            amount = float(self.goal_amount_entry.get())
            if name == "" or amount <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Enter a valid goal name or amount")
            return

        goals = load_goals()
        goals.append([self.get_user(), name, amount, 0.0])
        save_goals(goals)

        self.goal_name_entry.delete(0, tk.END)
        self.goal_amount_entry.delete(0, tk.END)

        self.refresh_goal_list()

    #function for refreshing the list so it shows current guys goal
    def refresh_goal_list(self):
        self.goal_listbox.delete(0, tk.END)
        goals = load_goals()

        #g = row
        for g in goals:
            if g[0] == self.get_user():
                saved = float(g[3])
                goal = float(g[2])
                percent = min((saved / goal) * 100, 100)

                self.goal_listbox.insert(
                    tk.END,
                    f"{g[1]}: ${saved:.2f} / ${goal:.2f} ({percent:.1f}%)"
                )

    #function for adding moneu
    def add_money(self):
        selection = self.goal_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Select a goal first.")
            return

        try:
            amount = float(self.add_money_entry.get())
            if amount <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Enter a valid amount DumbButt")
            return

        goals = load_goals()
        user_goals = [g for g in goals if g[0] == self.get_user()]

        chosen_goal = user_goals[selection[0]]
        chosen_goal[3] = float(chosen_goal[3]) + amount

        if chosen_goal[3] >= float(chosen_goal[2]):
            messagebox.showinfo(
                "Congratulations",
                f"You completed the goal '{chosen_goal[1]}'!"
            )
            goals.remove(chosen_goal)
        else:
            for i, g in enumerate(goals):
                if g == chosen_goal:
                    goals[i] = chosen_goal

        save_goals(goals)
        self.add_money_entry.delete(0, tk.END)
        self.refresh_goal_list()