# AC GUI

import tkinter as tk
from tkinter import ttk

LARGEFONT =("Verdana", 35)

class tkinterApp(tk.Tk):
    
    # __init__ function for class tkinterApp 
    def __init__(self, *args, **kwargs): 
        
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        
        # creating a container
        container = tk.Frame(self)  
        container.pack(side = "top", fill = "both", expand = True)
 
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
 
        # initializing frames to an empty array
        self.frames = {}  
 
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (LoginSignup, Login, Signup, SignupEnterPass, MainMenu):
 
            frame = F(container, self)
 
            # initializing frame of that object from
            # startpage, page1, page2 respectively with 
            # for loop
            self.frames[F] = frame 
 
            frame.grid(row = 0, column = 0, sticky ="nsew")
 
        self.show_frame(LoginSignup)
 
    # to display the current frame passed as
    # parameter
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
            command = lambda : controller.show_frame(Login))

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
            command = lambda : controller.show_frame(Signup))
        
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
        
        def print_user_pass():
            user_text = username_entry.get()
            pass_text = password_entry.get()
            print(user_text)
            print(pass_text)
            controller.show_frame(MainMenu)

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
            command=print_user_pass)
        
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
            command = lambda : controller.show_frame(LoginSignup))


        username_label.pack(padx=20, pady=5, anchor="center")
        username_entry.pack(padx=20, pady=10, anchor="center")
        password_label.pack(padx=20, pady=5, anchor="center")
        password_entry.pack(padx=20, pady=10, anchor="center")
        submit_button.pack(padx=20, pady=15, anchor="center")
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
        
        def print_user_pass():
            user_text = username_entry.get()
            print(user_text)
            controller.show_frame(SignupEnterPass)

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
            command= print_user_pass)
        
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
            command = lambda : controller.show_frame(LoginSignup))
        
        username_label.pack(padx=20, pady=5, anchor="center")
        username_entry.pack(padx=20, pady=10, anchor="center")
        submit_button.pack(padx=20, pady=15, anchor="center")
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
        
        def print_pass():
            pass_text = password_entry.get()
            print(pass_text)

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
            command=print_pass)
        
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
            command = lambda : controller.show_frame(Signup))
        
        password_label.pack(padx=20, pady=5, anchor="center")
        password_entry.pack(padx=20, pady=10, anchor="center")
        submit_button.pack(padx=20, pady=15, anchor="center")
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
            #command = lambda : controller.show_frame(IncomeExpenseTracking)
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
            #command = lambda : controller.show_frame(Page2)
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
            overrelief="solid")
        
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
            #command = lambda : self.root.destroy()
            )

        # 25 pixels away
        income_expense_tracking_button.pack(padx=20, pady=10, anchor="center")
        budgeting_button.pack(padx=20, pady=10, anchor="center")
        savings_goal_tracker_button.pack(padx=20, pady=10, anchor="center")
        exit.pack(padx=20, pady=10, anchor="center")
        

app = tkinterApp()
app.geometry("1000x1000")
app.mainloop()