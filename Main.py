import mysql.connector
import random
connection = mysql.connector.connect(user = "root", database = "Bank", password = "Batman10")
cursor = connection.cursor()
cursor.execute("SET SQL_SAFE_UPDATES = 0;")

class User():
    def __init__(self,name,surname,balance,type,ID):
        self.name=name
        self.surname=surname
        self.balance=balance
        self.type=type
        self.ID=ID
current_user=None
def cursor_execution(execution_code):
    cursor.execute(execution_code)
    return cursor
def  print_page():
    print("\n\n\n\n\n\n\n\n==============================================\n\n\n")
def  welcome():
    print("welcome to Spear banking system.")
    process=input("Please type \"s\" if  you would like to sign in. Type in \"c\" if  you do not have an account.")
    while True:
        if process=="s" or process=="c":
            break
        else:
            print("we could not understand what  you would like to do.")
            process=input("Please type \"s\" if  you would like to sign in. Type in \"c\" if  you do not have an account.")
    print_page()
    if process=="s":
        sign_in()
    elif process=="c":
        create_account()
        welcome()
def create_account():
    name=input("What is your name?")
    surname=input("What is your surname?")
    authorized=input("If you are an authorized person please type the code, otherwise type \"customer\"")
    if authorized=="spearbank":
        type= True
    else:
        type=False
    ID=""
    for i in range(6):
        ID=ID+str(random.randint(1,9))
    print(ID)
    pin=input("What do you want  your pin to be")
    while True:
        try:
            pin=int(pin)
            break
        except:
            pin=input("please enter one more time. What you put in was invalid.")
    cursor.execute(f"insert into Users (ID,Type,Name,Surname,Pin,balance) values ({int(ID)},{type},\"{name}\",\"{surname}\",{pin},0);")
    print_page()
    
def sign_in():
    ID=input("please enter your ID")
    while True:
        try:
            ID=int(ID)
            break
        except:
            ID=input("please enter one more time. What you put in was invalid.")
    PIN=input("please enter your PIN")
    while True:
        try:
            PIN=int(PIN)
            break
        except:
            PIN=input("please enter one more time. What you put in was invalid.")
    users_info= cursor.execute("SELECT * FROM Users")
    for item in users_info:
        if item[0]==ID and item[4]==PIN:
            current_user=User(item[2],item[3],item[5],item[1],item[0])
            main_menu(current_user)
    print_page()
def main_menu(user):
    process=input("What would you like to do. To check balance enter \"c\".To deposit money enter \"d\".To withdraw money enter \"w\".To close your account enter \"CLOSE\". To modify information enter \"m\".")
    while True:
        if process=="c" or process=="d" or process=="w" or process=="m" or process=="CLOSE":
            break
        else:
            print("we could not understand what  you would like to do.")
            process=input("What would you like to do. To check balance enter \"c\".To deposit money enter \"d\".To withdraw money enter \"w\".To close your account enter \"CLOSE\". To modify information enter \"m\".")
    print_page()
    if process=="c":
        check_balance(user)
        main_menu(user)
    elif process=="w":
        withdraw_money(user)
        main_menu(user)
    elif process=="d":
        deposit_money(user)
        main_menu(user)
    elif process=="CLOSE":
        if user.type==False:
            close_account()

        else:
            close_account_authorized()
            main_menu(user)
    elif process=="m":
        modify_account(user)


def check_balance(user):
    print("Total:"+str(user.balance))
    print_page()
def withdraw_money(user):
    print("Total:"+str(user.balance))
    money_withdrawn=input("please enter the amount of money you want to withdraw:")
    while True:
        try:
            money_withdrawn=int(money_withdrawn)
            if user.balance-money_withdrawn>=0:
                break
            else:
                money_withdrawn=input("The amount that you want to withdraw is more than what you have. Please enter one more time.")
        except:
            money_withdrawn=input("please enter one more time. What you put in was invalid.")
    cursor.execute(f"UPDATE Users SET balance={str(user.balance-withdraw_money)} WHERE ID={user.ID};")
    balance=cursor.execute(f"select balance from Users where ID={user.ID};")
    for banker in balance:
        print("Your new balance is :"+str(banker[0]))
        user.balance=banker[0]
    print_page()

def deposit_money(user):
    print("Total:"+str(user.balance))
    money_deposit=input("please enter the amount of money you want to deposit:")
    while True:
        try:
            money_deposit=int(money_deposit)
            break
        except:
            money_deposit=input("please enter one more time. What you put in was invalid.")
    cursor.execute(f"UPDATE Users SET balance={str(user.balance+money_deposit)} WHERE ID={user.ID};")
    balance=cursor.execute(f"select balance from Users where ID={user.ID};")
    for banker in balance:
        print("Your new balance is :"+str(banker[0]))
        user.balance=banker[0]
    print_page()
def close_account(user):
    answer=input("Are you sure you want to delete the account. \"yes\" or \"no\"")
    while answer !="yes" or answer !="no":
        answer=input("What you tried to input was not understood. Please enter one more time. Are you sure you want to delete the account. \"yes\" or \"no\"")
    if  answer=="yes":
        cursor.execute(f"DELETE FROM Users WHERE ID={user.ID};") 
        welcome()
    elif answer=="no":
        print("Okay we are not deleting your account")
        main_menu(user)
    print_page()
def close_account_authorized(user):
    user_id= input("What is the ID number of the customer whose account you would like to close?")
    exist=False
    while True:
        try:
            user_id=int(user_id)
            users_info= cursor.execute("SELECT * FROM Users")
            for item in users_info:
                if item[0]==user_id:
                    exist=True
                    break
            if exist==True:
                break
            else:
                user_id=input("There is no customer with that ID.")
        except:
            user_id=input("You entered a wrong character")
    answer=input("Are you sure you want to delete the account. \"yes\" or \"no\"")
    while answer !="yes" or answer !="no":
        answer=input("What you tried to input was not understood. Please enter one more time. Are you sure you want to delete the account. \"yes\" or \"no\"")
    if  answer=="yes":
        cursor.execute(f"DELETE FROM Users WHERE ID={user_id};") 

    elif answer=="no":
        print("Okay we are not deleting your account")
    print_page()
def modify_account(user):
    modified= input("Please enter what would you like to modify in your account.To change name enter \"n\".To change surname enter \"s\". To change pin enter \"p\".")
    while True:
        if modified=="n" or modified=="s" or modified=="p":
            break
        else:
            print("we could not understand what  you would like to do.")
            modified=input("What would you like to do. Please enter what would you like to modify in your account.To change name enter \"n\".To change surname enter \"s\". To change pin enter \"p\".")
    if modified=="n":
        print("Your current name is "+ str(user.name)+".")
        new_name=input("What would you like to change it to?")
        cursor.execute(f"UPDATE Users SET Name={new_name} WHERE ID={user.ID};")
        name=cursor.execute(f"select Name from Users where ID={user.ID};")
        for banker in name:
            print("Your new name is :"+str(banker[2]))
            user.name=banker[2]
    elif modified=="s":
        print("Your current surname is "+ str(user.surname)+".")
        new_surname=input("What would you like to change it to?")
        cursor.execute(f"UPDATE Users SET Surname={new_surname} WHERE ID={user.ID};")
        surname=cursor.execute(f"select Surname from Users where ID={user.ID};")
        for banker in surname:
            print("Your new surname is :"+str(banker[3]))
            user.surname=banker[3]
    elif modified=="p":
        new_pin=input("What would you like to change it to?")
        while True:
            try:
                new_pin=int(new_pin)
                if len(new_pin)==4:
                    break
                else:
                    new_pin=input("You entered other than four digits. Please enter a four digit pin.")
            except:
                new_pin=input("please enter one more time. What you put in was invalid.")
        cursor.execute(f"UPDATE Users SET Pin={new_pin} WHERE ID={user.ID};")
        print("Your new pin is set.")
    print_page()

welcome()



cursor.close()
connection.close()