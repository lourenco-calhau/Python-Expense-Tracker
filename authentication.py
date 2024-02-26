import csv

def select_method():
    select = int(input("""Chosse what you want to do:
[1] LOGIN
[2] SIGN UP
"""))
    if select == 1:
        login()
    elif select == 2:
        sign_up()
    else:
        print('Choose a valid operation')
        select_method()

def login(username, password):
    with open('accounts.csv', "r") as f:
        for line in f:
            items = line.split(' , ')
            items= [item.strip() for item in items]
            if username==items[0] and password==items[1]:
                return True
    return False

def sign_up(username, password):
    with open('accounts.csv', "a") as f:
        f.write(f"{str(username)} , {str(password)}\n")
    print('Successfully registered')
    
