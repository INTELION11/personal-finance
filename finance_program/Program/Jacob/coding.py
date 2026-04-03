import csv  
from helper import sprint  
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
    #    try:  
    #        open csv with budget information  
    #            for every line in the reader:  
    #                budget_info[make the first line a key, the second line the % of budget]  
    try:  
        with open("finance_program/documents/budget.csv", mode="r") as file:  
            reader = csv.reader(file, delimiter=',')  
            budget_info = {}  
            for line in reader:  
                budget_info[line[0]] = float(line[1])  
    #    eccept:  
    #        display(there is no csv for you)  
    #        pass  
    except:  
        sprint("there is no csv for you")  
        budget_info = {}  
  
    # **LOGIC FIX: If no categories, force user to add them**  
    if not budget_info:  
        sprint("No categories found! You have to add some first.")  
        change = "yes"  
    else:  
        #    display(categories and budget percentage)  
        sprint("Current categories and budget percentages:")  
        for category, percent in budget_info.items():  
            sprint(f"{category}: {percent}%")  
        #    ask user if the want to make changes  
        change = input("Do you want to make changes? (yes/no): ").strip().lower()  
  
    #   if there are categories and they say no:  
    if change == "no":  
        currency_op = input("what currency do you want? 1.Yen 2.Usa 3.Pound: ").strip().lower()  
        for category in budget_info:  
            should = currency(income * (budget_info[category]/100), currency_op)  
            sprint(f"money you should spend for {category} is {should}")  
        with open("finance_program/documents/budget.csv", mode="w", newline='') as file:  
            writer = csv.writer(file)  
            for cat, pct in budget_info.items():  
                writer.writerow([cat, pct])  
        return  
  
    #    if user says yes or was forced:  
    if change == "yes":  
        universe = True  
        while universe:  
            sprint("menu: change name / add / remove / change percent / exit / back")  
            menu = input("what do you want to do? ").strip().lower()  
            if menu == "change name":  
                cat_change = input("what category would you like to change? ").strip()  
                new_name = input("what would be the new name? ").strip()  
                if cat_change in budget_info:  
                    budget_info[new_name] = budget_info.pop(cat_change)  
            elif menu == "add":  
                cat = input("new category name: ").strip()  
                percent = float(input("what percent of budget for this category? "))  
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
                with open("finance_program/documents/budget.csv", mode="w", newline='') as file:  
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
                with open("finance_program/documents/budget.csv", mode="w", newline='') as file:  
                    writer = csv.writer(file)  
                    for cat, pct in budget_info.items():  
                        writer.writerow([cat, pct])  
                return   
def currency(money, option):  
    
    # use forex to get live currency conversion  
    try:
        from forex_python.converter import CurrencyRates  
        c = CurrencyRates()  
        # option == "1": USD to JPY  
        if option == "1" or option == "usd":  
            converted = c.convert('USD', 'JPY', money)  
            return f"{converted:.2f} Yen (live)"  
        # option == "2": USD to USD (just show as is)  
        elif option == "2" or option == "yen":  
            return f"${money:.2f} USD (live)"  
        # option == "3": USD to GBP  
        elif option == "3" or option == "pound":  
            converted = c.convert('USD', 'GBP', money)  
            return f"£{converted:.2f} Pound (live)"  
        else:  
            return f"${money:.2f} USD (live)"  
    except:   
        if option == "1":  
            return f"{money * 150:.2f} Yen (backup)"  
        elif option == "2":  
            return f"${money:.2f} USD (backup)"  
        elif option == "3":  
            return f"£{money * 0.8:.2f} Pound (backup)"  
        else:  
            return f"${money:.2f} USD (backup)"  
