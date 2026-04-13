import csv  
from helper import sprint
from piechart import piechart
def time_frame(username, frame):  
    # open income.csv, look for username, get income if it exists  
    income_file = "finance_program/documents/income.csv"  
    users = []  
    income = None  
    found = False  
    try:  
        with open(income_file, mode="r", newline='') as file:  
            reader = csv.reader(file)  
            for line in reader:  
                # line[0] = username, line[1] = income  
                if line[0] == username:  
                    found = True  
                    if len(line) >= 2 and line[1] != '':  
                        try:  
                            income = float(line[1])  
                        except:  
                            income = None  
                    users.append(line)  
                else:  
                    users.append(line)  
    except FileNotFoundError:  
        # if file doesn't exist, will create it below  
        pass  
  
    # if no income stored, ask for it and update the csv  
    if income is None:  
        income = float(input("how much money do you make a year? ").strip())  
        found = False  
        for line in users:  
            if line[0] == username:  
                line[1] = str(income)  
                found = True  
        if not found:  
            users.append([username, str(income)])  
        with open(income_file, mode="w", newline='') as file:  
            writer = csv.writer(file)  
            writer.writerows(users)  
  
    # math with frame argument  
    if frame == "month":  
        return income / 12  
    elif frame == "week":  
        return income / 52.1429  
    elif frame == "day":  
        return income / 365.25  
    elif frame == "year":
        return income
    else:  
        return income  
# define budgeting function to take in username and income  
def budgeting(username, income):  
    #piechart(["a", "b", "c"], [1, 2, 3])  
  
    # Use a separate budget file for each user  
    user_budget_file = f"finance_program/documents/budget_{username}.csv"  
  
    try:  
        with open(user_budget_file, mode="r") as file:  
            reader = csv.reader(file, delimiter=',')  
            budget_info = {}  
            for line in reader:  
                budget_info[line[0]] = float(line[1])  
    except:  
        sprint("there is no csv for you\n")
        with open(user_budget_file, mode="w") as file:  
            pass  
        with open(user_budget_file, mode="r") as file:  
            reader = csv.reader(file, delimiter=',')  
            budget_info = {}  
            for line in reader:  
                budget_info[line[0]] = float(line[1])   
  
    if not budget_info:  
        sprint("No categories found! You have to add some first.\n")  
        change = "yes"  
    else:  
        sprint("Current categories and budget percentages:\n")  
        for category, percent in budget_info.items():  
            sprint(f"{category}: {percent}%\n")  
        change = input("Do you want to make changes? (yes/no): \n").strip().lower()  

    if change == "no":
        categories = []
        numbers = []
        currency_op = input("what currency do you want? 1.Yen 2.Usa 3.Pound: ").strip().lower()  
        for category in budget_info:  
            should = currency(income * (budget_info[category]/100), currency_op)
            numbers.append(should)
            categories.append(category)
            
            sprint(f"money you should spend for {category} is {should}") 
        piechart(categories, numbers)
        with open(user_budget_file, mode="w", newline='') as file:  
            writer = csv.writer(file)  
            for cat, pct in budget_info.items():  
                writer.writerow([cat, pct])
        return  username
  
    elif change == "yes":  
        universe = True  
        while universe:  
            sprint("menu: change name / add / remove / change percent / exit / back\n ")  
            menu = input("what do you want to do?\n").strip().lower()  
            if menu == "change name":  
                cat_change = input("what category would you like to change? ").strip()  
                new_name = input("what would be the new name? ").strip()  
                if cat_change in budget_info:  
                    budget_info[new_name] = budget_info.pop(cat_change)  
            elif menu == "add":  
                cat = input("new category name: ").strip()
                try:  
                    percent = float(input("what percent of budget for this category? "))
                except:
                    print("thats not allowed")
                    percent = 10000  
                if sum(budget_info.values()) + percent > 100:  
                    sprint("can't go over 100%")  
                    continue  
                budget_info[cat] = percent  
            elif menu == "remove":  
                cat = input("category name to remove: ").strip()  
                try:  
                    budget_info.pop(cat)  
                except:  
                    sprint("did not work")  
            elif menu == "change percent":  
                cat_change = input("what category would you like to change? ").strip()  
                new_percent = float(input("what would be the new percentage? "))  
                if cat_change in budget_info:  
                    current_total = sum(budget_info.values()) - budget_info[cat_change]  
                    if current_total + new_percent > 100:  
                        sprint("can't go over 100%")  
                        continue  
                    budget_info[cat_change] = new_percent  
            elif menu == "exit":  
                with open(user_budget_file, mode="w", newline='') as file:  
                    writer = csv.writer(file)  
                    for cat, pct in budget_info.items():  
                        writer.writerow([cat, pct])  
                universe = False  
                return  
            elif menu == "back":  
                currency_op = input("what currency do you want? 1.Yen 2.Usa 3.Pound: ").strip()  
                for category in budget_info:  
                    should = currency(income * (budget_info[category]/100), currency_op)  
                    sprint(f"money you should spend for {category} is {should}")  
                with open(user_budget_file, mode="w", newline='') as file:  
                    writer = csv.writer(file)  
                    for cat, pct in budget_info.items():  
                        writer.writerow([cat, pct])
                universe=False  
                return 
    else:
        return 

def currency(money, option):  
    
    # use forex to get live currency conversion  
 
    try:  
        from forex_python.converter import CurrencyRates    
        c = CurrencyRates()  
        if option == "1" or option.lower() == "yen":  
            converted = c.convert('USD', 'JPY', money)  
            return f"{converted:.2f} Yen (live)"  
        elif option == "2" or option.lower() == "usa" or option.lower() == "usd":  
            return f"${money:.2f} USD (live)"  
        elif option == "3" or option.lower() == "pound":  
            converted = c.convert('USD', 'GBP', money)  
            return f"£{converted:.2f} Pound (live)"  
        else:  
            return f"${money:.2f} USD (live)"  
    except:  
        if option == "1" or option.lower() == "yen":  
            return f"{money * 150:.2f} Yen (backup)"  
        elif option == "2" or option.lower() == "usa" or option.lower() == "usd":  
            return f"${money:.2f} USD (backup)"  
        elif option == "3" or option.lower() == "pound":  
            return f"£{money * 0.8:.2f} Pound (backup)"  
        else:  
            return f"${money:.2f} USD (backup)"  

import csv  
from datetime import datetime  
from helper import sprint  
  
def entries(username):  
    budget_file = "finance_program/documents/budget.csv"  
    # Each user gets their own entries file  
    entries_file = f"finance_program/documents/entries_{username}.csv"  
    today = datetime.now().strftime("%Y-%m-%d")  
  
    # Ask how much they made (for this entry)  
    income = float(input("How much money did you make for this entry? ").strip())  
  
    # Load categories and percents from budget.csv  
    budget_info = {}  
    try:  
        with open(budget_file, mode="r") as file:  
            reader = csv.reader(file)  
            for line in reader:  
                if len(line) >= 2:  
                    budget_info[line[0]] = float(line[1])  
    except:  
        sprint("No budget file found. Set up your budget first!")  
        return  
  
    # For each category, remind and ask for actual spending  
    for category, percent in budget_info.items():  
        should_spend = income * (percent / 100)  
        sprint(f"For '{category}' you should have spent: {should_spend:.2f}")  
        actually_spent = float(input(f"How much did you actually spend on '{category}'? ").strip())  
  
        # Save to user's own entries file  
        with open(entries_file, mode="a", newline='') as file:  
            writer = csv.writer(file)  
            writer.writerow([today, income, category, should_spend, actually_spent])  
  
    sprint(f"All entries for {today} have been saved in {entries_file}.")  
  

