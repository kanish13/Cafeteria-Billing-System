
import pandas as pd
import csv
from prettytable import PrettyTable
def create_username_password():
    userr_name=input("Enter your user name that you want to create:")
    passwordd=input("Enter the strong password:")
    card_balance=int(input("Enter the amount to be stored:"))
    column_names = ["USERNAME","PASSWORD","CARD_BALANCE","PENDING_AMOUNT"]
    rows = [[userr_name,passwordd,card_balance,0]]
    try:
        with open("dataframe.csv", 'r') as file:
            first_line = file.readline()
    except:
        first_line = None
    with open("dataframe.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        if not first_line:
            writer.writerow(column_names)
        writer.writerows(rows)       
def login():
    while True:
        login.user_name=input("Enter the username:")
        login.password=input("Enter the password:")
        b=login.user_name
        d=login.password
        df=pd.read_csv("dataframe.csv")
        login.l=False
        if df['USERNAME'].isin([b]).any():   
            result = df[df['USERNAME'] == b]
            result = result['PASSWORD'].values[0]    
            if str(result)==d:
                login.l=True
                break
            else:
                print("WRONG PASSWORD")
                chh=int(input("1.RETRY\n2.EXIT\n"))
                if chh==2:
                    break 
        else:
                print("WRONG USERNAME ")
                chh=int(input("1.RETRY\n2.EXIT\n"))
                if chh==2:
                    break 
def food():
        column_names = ["FOODS","PRICE"]
        rows = [["DOSA",20],["IDLY",7],["PAROTTA",10]]
        try:
            with open("FOODITEMS.csv", 'r') as file:
                first_line = file.readline()
        except:
            first_line = None
        with open("FOODITEMS.csv", mode='a', newline='') as file:
            writer = csv.writer(file)
            if not first_line:
                writer.writerow(column_names)
                writer.writerows(rows)         
def add_item():    
    if login.l:
        add_item.cost=0
        n=int(input("Enter the no of item that you want to add:"))
        df2=pd.read_csv("FOODITEMS.csv")

        add_item.food_display=pd.DataFrame(columns=["ORDERED FOODS","PRICES"])
        for i in range(n):
            foods=input("Enter the food name:")
            add_item.cost=add_item.cost+df2.loc[df2['FOODS'] == foods, 'PRICE'].values
            t=[foods,df2.loc[df2['FOODS'] == foods, 'PRICE'].values]
            new_row=pd.DataFrame({"ORDERED FOODS":[t[0]],"PRICES":[t[1]]})
            add_item.food_display= pd.concat([add_item.food_display, new_row], ignore_index=True)

def add_items_admin():  
    add_item=input("Do you want to add items YES/NO:")
    if add_item=="YES":
        n=int(input("Enter the number of items:"))
        for i in range(n):
            add_food=input("Enter the food to be added:")
            add_food_price=int(input("Enter the price of the above food:"))
            rows=[[add_food,add_food_price]]
            column_names=["FOODS","PRICE"]
            with open('FOODITEMS.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                for row in rows:
                    writer.writerow(row)   
def display_ordered_foods():
    if login.l:
        print("-----------------------------MY CAFETERIA---------------------------------")
        print(add_item.food_display)

        print("TOTAL COST:",add_item.cost)
def pay():
    if login.l:
        ask=int(input("Do you want to pay or you wish to pay later: 1) PAY NOW 2) PAY LATER"))
        if ask==1:
            df = pd.read_csv("dataframe.csv")
            result = df[df['USERNAME'] == login.user_name]
            result = result['CARD_BALANCE'].values[0]
            if result>=add_item.cost:
                a=result-add_item.cost
                df.loc[df['USERNAME'] == login.user_name, "CARD_BALANCE"] = a  
                df.to_csv('dataframe.csv', index=False)
                print("PAID")
                print("CURENT BALANCE:",a)
            else:     
                print("YOU DONT HAVE ENOUGH MONEY TO PAY")  
        else:
            df = pd.read_csv("dataframe.csv")
            result = df[df['USERNAME'] == login.user_name]
            result = result['PENDING_AMOUNT'].values[0]
            a=result+add_item.cost
            df.loc[df['USERNAME'] == login.user_name, "PENDING_AMOUNT"] = a   
            df.to_csv("dataframe.csv", index=False)
            print("PENDING AMOUNT:",a)
def format_file():
    with open('dataframe.csv', 'w') as f:
        f.write('')
def print_register():
    with open('dataframe.csv', 'r',newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader)
        table = PrettyTable(headers)
        for row in csv_reader:
            table.add_row(row)   
    print(table)
def print_food_items_available():
    with open('FOODITEMS.csv', 'r',newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader)
        table = PrettyTable(headers)
        for row in csv_reader:
            table.add_row(row)   
    print(table)
food()
print("---------------------------------WELCOME TO MY CAFFETERIA---------------------------------")
print("\n")
print("------AVAILABLE FOOD ITEMS------")
print_food_items_available()
print("\n")
choose=int(input("1.ADMIN\n2.USER\n"))
print("\n")
if choose==1:
    admin_username=input("Enter the admin's username:")
    admin_password=input("Enter the admin password:")
    if admin_username=="MYCAFAD" and admin_password=="9270676334":
        while True:
            ch=int(input("1.ADD_ITEMS_INTO_FOOD_LIST\n2.FORMAT_CSV_FILE\n3.DISPLAY REGISTER\n4.EXIT\n"))
            if ch==1:
                print("\n")    
                add_items_admin()
                print("\n")
            elif ch==2:
                print("\n")
                format_file()
                print("\n")
            elif ch==3:
                print("\n")
                print_register()
                print("\n")
            else:
                break
elif choose==2:
    while True:
        login_or_create=int(input("1.LOGIN\n2.CREATE NEW USER\n3.EXIT\n"))
        if login_or_create==1:
            print("\n")
            login()
            print("\n")
            add_item()
            print("\n")
            pay()
            print("\n")
            display_ordered_foods()
            print("\n")    
        elif login_or_create==2:
            print("\n")   
            create_username_password()
            print("\n")
        else:
            break






            






            








    


