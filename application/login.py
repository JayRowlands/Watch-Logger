import PySimpleGUI as sg      
import sqlite3

def main():
    user_list = getUsers()
    sg.theme('DarkGrey6')

    layout = [[sg.Text('Enter Username')],
            [sg.Listbox(key='User_List', values=user_list, size=(40, 10), enable_events=True,)],   
            [sg.Input(key='Username', do_not_clear=False, enable_events=True)],      
            [sg.Button('Submit'), sg.Exit()]]      

    login = sg.Window('Watch Logger', layout)      
 
    while True:
        event, values = login.Read()
        if event is None or event == 'Exit':                # always check for closed window
            break
        if event == 'User_List' and len(values['User_List']):     # if a list item is chosen
            print(values.get("User_List"))
            login.find_element('Username').Update(values.get("User_List"))
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