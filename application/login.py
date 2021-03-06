import PySimpleGUI as sg      
import sqlite3
import app
from sqlalchemy import null

def main():
    user_list = getUsers()
    sg.theme('DarkGrey6')

    layout = [[sg.Text('Username List')],
            [sg.Listbox(key='User_List', values=user_list, size=(40, 10), enable_events=True,)],   
            [sg.Input(key='Username')],      
            [sg.Button('Login'), sg.Button('Create User'), sg.Button('Delete User'), sg.Exit()]]      

    login = sg.Window('Watch Logger', layout).Finalize()  
 
    while True:
        event, values = login.Read()
        if event is None or event == 'Exit':                # always check for closed window
            break
        if event == 'Login':
            if log(values.get('Username')) == False:
                print("Error")
            else:
                login.close()

        if event == 'User_List' and len(values['User_List']):     # if a list item is chosen
            login.find_element('Username').Update(values.get("User_List"))
        if event == 'Create User':
            createUser(values.get('Username'))
            login.find_element('User_List').Update(values=getUsers())
            login.find_element('Username').Update("")
        if event == 'Delete User':
            if (values.get('Username') != ""):
                deleteUser(values.get('Username'))
                login.find_element('User_List').Update(values=getUsers())
                login.find_element('Username').Update("")
    login.Close()

def log(username):
    db = sqlite3.connect('logger.sqlite3')
    cursor = db.cursor()

    list_of_chars = ['(', ',', ')']
    for c in list_of_chars:
        username = username.replace(c, '')
    username= username.strip(" ' ")

    exists = False
    for i in range(len(getUsers())):
        if getUsers()[i] == username:
            exists = True
        if (exists == False): 
            if exists != True:
                exists = False

    db.close()

    if exists == True: 
        app.app(username)
    else:
        return False


def createUser(username):
    db = sqlite3.connect('logger.sqlite3')
    cursor = db.cursor()

    list_of_chars = ['(', ',', ')']
    for c in list_of_chars:
        username = username.replace(c, '')
    username= username.strip(" ' ")

    exists = False
    
    if not getUsers():
        cursor.execute(f"INSERT INTO Users (name) VALUES ('{username}')")
        db.commit()
    else:
        for i in range(len(getUsers())):
            if getUsers()[i] == username:
                exists = True
        if (exists == False): 
            cursor.execute(f"INSERT INTO Users (name) VALUES ('{username}')")
            db.commit()
    
    db.close()

def deleteUser(username):
    db = sqlite3.connect('logger.sqlite3')
    cursor = db.cursor()

    list_of_chars = ['(', ',', ')']
    for c in list_of_chars:
        username = username.replace(c, '')
    username= username.strip(" ' ")

    cursor.execute(f"DELETE FROM Users WHERE name = '{username}'")
    db.commit()
    db.close()

def getUsers():
    db = sqlite3.connect('logger.sqlite3')
    cursor = db.cursor()
    cursor.execute("SELECT name FROM Users")
    users = [item[0] for item in cursor.fetchall()]
    user_list = list()
    for i in users:
        user_list.append(i)
    db.close()
    return user_list

if __name__ == "__main__":
    main()
