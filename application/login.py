import PySimpleGUI as sg      
import sqlite3

def main():
    sg.theme('DarkGrey6')

    layout = [[sg.Text('Enter Username')],      
            [sg.Input(key='Username', do_not_clear=False)],      
            [sg.Button('Submit'), sg.Exit()]]      

    login = sg.Window('Watch Logger', layout)      
    event, values = login.read() 
    createUser(values.get('Username'))

def createUser(username):
    db = sqlite3.connect('logger.sqlite3')
    cursor = db.cursor()
    cursor.execute(f"INSERT INTO Users (name) VALUES ('{username}')")

    cursor.execute("SELECT * FROM Users")
    users = cursor.fetchall()
    for i in users:
        print(i)
    db.commit()
    db.close()

if __name__ == "__main__":
    main()

# while True:
#     event, values = login.read() 
#     print(event, values)       
#     if event == sg.WIN_CLOSED or event == 'Exit':
#         break      

# login.close()