import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Temporary in-memory storage (CSV later)
savings_data = {}

def init_user(user_id):
    if user_id not in savings_data:
        savings_data[user_id] = {
            "goal_amount": 0.0,
            "current_savings": 0.0
        }

def set_savings_goal(user_id, amount):
    savings_data[user_id]["goal_amount"] = amount

def add_to_savings(user_id, amount):
    savings_data[user_id]["current_savings"] += amount

def get_savings_progress(user_id):
    goal = savings_data[user_id]["goal_amount"]
    current = savings_data[user_id]["current_savings"]

    if goal <= 0:
        return current, goal, 0.0

    percent = min((current / goal) * 100, 100)
    return current, goal, round(percent, 2)

def create_savings_frame(parent, user_id):
    init_user(user_id)

    frame = tk.Frame(parent, padx=10, pady=10)

    #set Goal
    tk.Label(frame, text="Savings Goal ($):").pack(anchor="w")
    goal_entry = tk.Entry(frame)
    goal_entry.pack(fill="x")

    #Add savings and stuff
    tk.Label(frame, text="Add to Savings ($):").pack(anchor="w", pady=(10, 0))
    add_entry = tk.Entry(frame)
    add_entry.pack(fill="x")

    #display progress
    progress_label = tk.Label(frame, text="Saved: $0 / $0 (0%)")


"""savings_frame = create_savings_frame(root, logged_in_user)
savings_frame.pack()"""