try:  
            with open("Documents/pass_a_user.csv", mode="r") as file:  
                reader = csv.reader(file, delimiter=',')                               
                users = {}                                      
                for line in reader:                             
                    users[line[0]] = line[1]                    
        except:                                                 
            sprint("\033[38;2;0;125;1mcant find csv\n")                              
            continue                                            
        if option in users: 
            processing()
            password = input("\033[38;2;0;125;1mEnter your password:\n").strip()
            if password == "exit" or password == "Exit":
                clearr()
                return password
            encripted_pass = hash(password, option)
            if encripted_pass == users[option]:
                    
define budgeting function (username,income)
    try:
        open csv with budget information
            for every line in the reader:
                budget_info[make the first line a key, the second line the % of budget]
    eccept:
        print(there is no csv for you)
        pass
    print(categories and budget percentage)
    ask user if the want to make changes
    if no:  
        currency_op = input(" what currency do you want 1.Yen 2.Usa 3. Pound,")
        for % in category
            should =currency(income / % of the first category, currency_op)
            print(f"money you should spend for {category}: {should}"):
        save csv using write writting over everything
        return
    if yes:
        while universe == True:
            menu = print("menu")
            if menu == change categories names
                cat_change = print: what categorie whoudl you like to change?
                new_name = what would be the new name?
                for keys in budget_info
                    if key == cat_change
                        key = new_name
            if menu == add categories
                cat = ask user for category name
                percent = ask user for percent of budget allocated
                if :100 == percent + budget_info:
                    pass
                budget_info.append(cat[percent])
            
            if menu == remove categories
                cat = ask user for category name
                try:
                        budget_info.pop(cat)
                    ecpet:
                        print("did not work")
            if menu == change %
                cat_change = print: what categorie whoudl you like to change?
                new_% = what would be the new %?
                for keys in budget_info
                    if cat_change == keys
                        for % in key
                            % = new_%
                if menu == exit
                    save csv using write writting over everything
                    universe = False
                    return
                    
        





