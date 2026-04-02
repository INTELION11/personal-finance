
# define budgeting function to take in username and income
#    try:
#        open csv with budget information
#            for every line in the reader:
#                budget_info[make the first line a key, the second line the % of budget]
#    eccept:
#        display(there is no csv for you)
#        pass
#    display(categories and budget percentage)
#    ask user if the want to make changes
#   if there is no csv or they say no: 
#        currency_op is equal to asking the user  what currency do you want 1.Yen 2.Usa 3. Pound,
#        for % of money in the category dictionary
#            display money you should spend for {category} is {should}
#        save csv using write writting over everything
#        exit out of function
#    if user says yes:
#        while universe is True:
#            ask user what they want to edit by displaying menu
#            if they want to change categories names:
#                ask what category whould you like to change?
#                ask what would be the new name?
#                if key is the old name key becomes the new_name       
#            if they want to add categories
#                cat is ask user for category name
#                percent is ask user for percent of budget allocated
#                if 100 is percent plus all budget categories:
#                    append new category to budget info
#                    pass
#            if they want to remove categories
#                ask user for category name
#                try:
#                        use pop to remove old category
#                if there is none names like that display("did not work")
#                        
#            if they want to change category percentage
#                ask what categorie whould you like to change?
#                ask what would be the new percentage?
#                for keys in budget_info
#                    if the category chosen is a key
#                        change value of information in keys
#            if they want to exit
#                save csv using write writting over everything
#                universe is False
#                return
#            if they want to go back
#                follow option No next
#            
#
#define currency using money and option
#    use ferrex to turn money into option of currency using money and option of currency
#
#
#
#define income using time frame
#    ask user how much money they make a year,
#    if time frame is month
#        divide income by 12
#    if timeframe is week
#        divide income by 52.1429
#    if time frame is day
#        divide income by 365.25
#    save csv using write writting over everything
#        return income
#
#define income and expenses









