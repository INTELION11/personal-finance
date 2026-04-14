# AC GUI

import tkinter as tk
from tkinter import ttk
from savings import Savings
from coding_but_Tkinter import Budgeting
from entry import IncomeTracking
import csv  
import hashlib

LARGEFONT =("Verdana", 35)
          
def hash(password, username):
    key = username[:3].encode()
    h = hashlib.blake2b(key=key, digest_size=64)
    h.update(password.encode())
    return h.hexdigest()

class tkinterApp(tk.Tk):
    
    def __init__(self, *args, **kwargs): 
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        container = tk.Frame(self)  
        container.pack(side = "top", fill = "both", expand = True)
 
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
 
        self.frames = {}  

        for F in (LoginSignup, Login, Signup, SignupEnterPass, MainMenu, Savings, Budgeting, IncomeTracking):
 
            frame = F(container, self)
 
            self.frames[F.__name__] = frame 
 
            frame.grid(row = 0, column = 0, sticky ="nsew")
 
        self.show_frame("LoginSignup")
 
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class LoginSignup(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text ="Login Or Signup", font = LARGEFONT)
        label.pack(pady=(40,40))

        login_button = tk.Button(self, 
            text="Login", 
            width=50, 
            height=4, 
            font=("Helvetica", 15), 
            bd=5, 
            bg="white", 
            activebackground="grey", 
            activeforeground="white", 
            overrelief="solid",
            command = lambda : controller.show_frame("Login"))

        signup_button = tk.Button(self, 
            text="Signup", 
            width=50, 
            height=4, 
            font=("Helvetica", 15), 
            bd=5, 
            bg="white", 
            activebackground="grey", 
            activeforeground="white", 
            overrelief="solid",
            command = lambda : controller.show_frame("Signup"))
        
        login_button.pack(pady=5)
        signup_button.pack(pady=5)


 
 
class Login(tk.Frame):
  
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text ="Login", font = LARGEFONT)
        label.pack(padx=20, pady=(40,40), anchor="center")
 
        username_label = tk.Label(self,
            text="Username",
            font=("Helvetica", 15))
        username_entry = tk.Entry(self, 
            text="Username", 
            width=50, 
            font=("Helvetica", 15), 
            bg="white")
        
        password_label = tk.Label(self,
            text="Password",
            font=("Helvetica", 15))
        password_entry = tk.Entry(self, 
            text="Password", 
            width=50, 
            font=("Helvetica", 15), 
            bg="white",
            show="*")
        
        def login_func():
            username = username_entry.get().strip().lower()
            password = password_entry.get().strip()

            if username.lower() == "exit" or password.lower() == "exit":
                login_label['text'] = "Cancelled"
                return

            try:
                with open("finance_program/documents/login_Revulet.csv", mode="r") as file:
                    reader = csv.reader(file)
                    users = {}

                    for line in reader:
                        if len(line) >= 2:
                            users[line[0].strip()] = line[1].strip()

                if username in users:
                    encrypted_input = hash(password, username)

                    if encrypted_input == users[username]:
                        controller.current_user = username
                        login_label['fg'] = ["green"]
                        login_label['text'] = "Login successful!"
                        controller.after(1500, lambda: controller.show_frame("MainMenu"))
                    else:
                        login_label['text'] = "Wrong password"
                else:
                    login_label['text'] = "User not found"

            except Exception as e:
                login_label['text'] = f"ERROR: {repr(e)}"

        submit_button = tk.Button(self, 
            text="Sign In", 
            width=50, 
            height=4, 
            font=("Helvetica", 15), 
            bd=5, 
            bg="white", 
            activebackground="grey", 
            activeforeground="white", 
            overrelief="solid",
            command=login_func)
        
        login_label = tk.Label(self,
            text="",
            font=("Helvetica", 15))
        
        back_button = tk.Button(self, 
            text="Back", 
            width=15, 
            height=3, 
            font=("Helvetica", 8), 
            bd=5, 
            bg="white", 
            activebackground="grey", 
            activeforeground="white", 
            overrelief="solid",
            command = lambda : controller.show_frame("LoginSignup"))


        username_label.pack(padx=20, pady=5, anchor="center")
        username_entry.pack(padx=20, pady=10, anchor="center")
        password_label.pack(padx=20, pady=5, anchor="center")
        password_entry.pack(padx=20, pady=10, anchor="center")
        submit_button.pack(padx=20, pady=15, anchor="center")
        login_label.pack(padx=20, pady=15, anchor="center")
        back_button.pack(padx=30, pady=(15,100), anchor="sw", side="left")

class Signup(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text ="Create Account", font = LARGEFONT)
        label.pack(padx=20, pady=(20,40), anchor="center")
 
        username_label = tk.Label(self,
            text="Create Username",
            font=("Helvetica", 15))
        username_entry = tk.Entry(self, 
            text="Username", 
            width=50, 
            font=("Helvetica", 15), 
            bg="white")
        

                
        def check_username(username):
            username=username_entry.get().strip().lower()
            try:  
                with open("finance_program/documents/login_Revulet.csv", mode="r+") as file:  
                    reader = csv.reader(file, delimiter=',')   
                    users = []  
                    for line in reader:  
                        users.append({line[0]: line[1]})  
            except:  
                cant_find_csv = "Can't find CSV" 
                check_label['text'] = str(cant_find_csv)

            found = False  
            for user in users:  
                if username in user:
                    already_in_database = "Already in data base"
                    check_label['text'] = str(already_in_database)
                    found = True 
            if not found:
                controller.current_user = username
                controller.show_frame("SignupEnterPass")

                
        def get_user():
            user_text = username_entry.get().strip().lower()
            print(user_text)
            check_username(user_text)

        submit_button = tk.Button(self, 
            text="Submit", 
            width=50, 
            height=2, 
            font=("Helvetica", 15), 
            bd=5, 
            bg="white", 
            activebackground="grey", 
            activeforeground="white", 
            overrelief="solid",
            command= get_user)
        
        check_label = tk.Label(self,
            text="",
            font=("Helvetica", 15))
        
        back_button = tk.Button(self, 
            text="Back", 
            width=15, 
            height=3, 
            font=("Helvetica", 8), 
            bd=5, 
            bg="white", 
            activebackground="grey", 
            activeforeground="white", 
            overrelief="solid",
            command = lambda : controller.show_frame("LoginSignup"))
        
        username_label.pack(padx=20, pady=5, anchor="center")
        username_entry.pack(padx=20, pady=10, anchor="center")
        submit_button.pack(padx=20, pady=15, anchor="center")
        check_label.pack(padx=20, pady=15, anchor="center")
        back_button.pack(padx=20, pady=15, anchor="sw")
        
class SignupEnterPass(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
            
        label = ttk.Label(self, text ="Create Account", font = LARGEFONT)
        label.pack(padx=20, pady=(20,40), anchor="center")

        password_label = tk.Label(self,
            text="Create Password",
            font=("Helvetica", 15))
        password_entry = tk.Entry(self, 
            text="Password", 
            width=50, 
            font=("Helvetica", 15), 
            bg="white",
            show="*")
        
        
        def pass_cheker(check_label):  
            special_characters = "!@#\\$%^&*()_+-=[]{|;:,}.><?)"  
            numbers = "1234567890"  

            password = password_entry.get().strip()

            if password.lower() == "exit":
                check_label['text'] = "Cancelled"
                return

            errors = []

            if len(password) < 8:
                errors.append("at least 8 characters")

            if not any(char in numbers for char in password):
                errors.append("a number")

            if not any(char in special_characters for char in password):
                errors.append("a special character")

            if not any(char.isupper() for char in password):
                errors.append("an uppercase letter")

            if not any(char.islower() for char in password):
                errors.append("a lowercase letter")

            if errors:
                check_label['text'] = "Missing: " + ", ".join(errors)
            else:
                username = controller.current_user

                try:
                    encripted_pass = hash(password, username)

                    with open("finance_program/documents/login_Revulet.csv", mode="a", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerow([username, encripted_pass])

                    check_label['fg'] = ["green"]
                    check_label['text'] = "Password is strong! User added successfully."
                    controller.after(2000, lambda: controller.show_frame("MainMenu"))

                except:
                    check_label['text'] = "Could not write to file"

        submit_button = tk.Button(self, 
            text="Login", 
            width=50, 
            height=2, 
            font=("Helvetica", 15), 
            bd=5, 
            bg="white", 
            activebackground="grey", 
            activeforeground="white", 
            overrelief="solid",
            command=lambda: pass_cheker(check_label))
        
        check_label = tk.Label(self,
            text="",
            font=("Helvetica", 15))
        
        back_button = tk.Button(self, 
            text="Back", 
            width=15, 
            height=3, 
            font=("Helvetica", 8), 
            bd=5, 
            bg="white", 
            activebackground="grey", 
            activeforeground="white", 
            overrelief="solid",
            command = lambda : controller.show_frame("Signup"))
        
        password_label.pack(padx=20, pady=5, anchor="center")
        password_entry.pack(padx=20, pady=10, anchor="center")
        submit_button.pack(padx=20, pady=15, anchor="center")
        check_label.pack(padx=20, pady=15, anchor="center")
        back_button.pack(padx=20, pady=(15) , anchor="sw", side="left")

class MainMenu(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text ="Finance Program", font = LARGEFONT)
        label.pack(pady=8)

        income_expense_tracking_button = tk.Button(self, 
            text="Income & Expense Tracking", 
            width=50, 
            height=4, 
            font=("Helvetica", 15), 
            bd=5, 
            bg="white", 
            activebackground="grey", 
            activeforeground="white", 
            overrelief="solid", 
            command = lambda : controller.show_frame("IncomeTracking")
            )
        
        budgeting_button = tk.Button(self, 
            text="Budgeting", 
            width=50, 
            height=4, 
            font=("Helvetica", 15), 
            bd=5, 
            bg="white", 
            activebackground="grey", 
            activeforeground="white", 
            overrelief="solid", 
            command = lambda : controller.show_frame("Budgeting")
            )
        
        savings_goal_tracker_button = tk.Button(self, 
            text="Savings Goal Tracker", 
            width=50, 
            height=4, 
            font=("Helvetica", 15), 
            bd=5, 
            bg="white", 
            activebackground="grey", 
            activeforeground="white", 
            overrelief="solid", 
            command = lambda : controller.show_frame("Savings")
            )
        
        logout_button = tk.Button(self,
            text="Logout", 
            width=50, 
            height=4, 
            font=("Helvetica", 15), 
            bd=5, 
            bg="white", 
            activebackground="grey", 
            activeforeground="white", 
            overrelief="solid", 
            command = lambda : controller.show_frame("LoginSignup")
            )
        
        exit = tk.Button(self, 
            text="Exit", 
            width=50, 
            height=4, 
            font=("Helvetica", 15), 
            bd=5, 
            bg="white", 
            activebackground="grey", 
            activeforeground="white", 
            overrelief="solid", 
            command = controller.destroy
            )

        # 25 pixels away
        income_expense_tracking_button.pack(padx=20, pady=10, anchor="center")
        budgeting_button.pack(padx=20, pady=10, anchor="center")
        savings_goal_tracker_button.pack(padx=20, pady=10, anchor="center")
        logout_button.pack(padx=20, pady=10, anchor="center")
        exit.pack(padx=20, pady=10, anchor="center")