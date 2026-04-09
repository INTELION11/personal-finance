#Initializw stuff
import tkinter as tk
from tkinter import messagebox
from gui import tkinterApp
import csv
import os

csv_file = "savings_goals.csv"

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
    #initialize
    def __init__(self, root, user_id, parent):
        tk.Frame.__init__(self, parent)
        self.root = root
        self.user_id = user_id
        self.root.title("Savings Goal Tracker")

        self.build_ui()
        self.refresh_goal_list()

    #make the ui
    def build_ui(self):
        # new goal
        tk.Label(self.root, text="Goal Name").grid(row=0, column=0)
        self.goal_name_entry = tk.Entry(self.root)
        self.goal_name_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Goal Amount ($)").grid(row=1, column=0)
        self.goal_amount_entry = tk.Entry(self.root)
        self.goal_amount_entry.grid(row=1, column=1)

        tk.Button(
            self.root, text="Make New Goal", command=self.make_new_goal
        ).grid(row=2, columnspan=2, pady=5)

        # list of goals
        tk.Label(self.root, text="Your Savings Goals").grid(row=3, columnspan=2)
        self.goal_listbox = tk.Listbox(self.root, width=45)
        self.goal_listbox.grid(row=4, columnspan=2)

        # adding money
        tk.Label(self.root, text="Add Money ($)").grid(row=5, column=0)
        self.add_money_entry = tk.Entry(self.root)
        self.add_money_entry.grid(row=5, column=1)

        tk.Button(
            self.root, text="Add to Selected Goal", command=self.add_money
        ).grid(row=6, columnspan=2, pady=5)

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
        goals.append([self.user_id, name, amount, 0.0])
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
            if g[0] == self.user_id:
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
        user_goals = [g for g in goals if g[0] == self.user_id]
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



def saving_main():
    user_id = "test_user"  #login system will replace this
    root = tk.Tk()
    run = Savings(root, user_id)#call
    root.mainloop()#run