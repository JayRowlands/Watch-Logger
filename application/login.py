import PySimpleGUI as sg      
import sqlite3

def main():
    user_list = getUsers()
    sg.theme('DarkGrey6')

    layout = [[sg.Text('Enter Username')],
            [sg.Listbox(key='User_List', values=user_list, size=(40, 10), enable_events=True,)],   
            [sg.Input(key='Username', do_not_clear=False, enable_events=True)],      
            [sg.Button('Login'), sg.Button('Create User'), sg.Button('Delete User'), sg.Exit()]]      

    login = sg.Window('Watch Logger', layout).Finalize()      
 
    while True:
        event, values = login.Read()
        if event is None or event == 'Exit':                # always check for closed window
            break
        if event == 'User_List' and len(values['User_List']):     # if a list item is chosen
            login.find_element('Username').Update(values.get("User_List"))
        if event == 'Create User':
            createUser(values.get('Username'))
        if event == 'Delete User':
            if (values.get('Username') != ""):
                deleteUser(values.get('Username'))
                login.find_element('User_List').Update(values=getUsers())
                event, values = login.Read()
    login.Close()
    #createUser(values.get('Username'))


def login(username):
    print("to do")

def createUser(username):
    db = sqlite3.connect('logger.sqlite3')
    cursor = db.cursor()
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
    user_list = []
    for i in users:
        user_list.append(i)
    db.close()
    return user_list

if __name__ == "__main__":
    main()

# while True:
#     event, values = login.read() 
#     print(event, values)       
#     if event == sg.WIN_CLOSED or event == 'Exit':
#         break      

# login.close()