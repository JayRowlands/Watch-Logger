import PySimpleGUI as sg      
import sqlite3

def app(username):
    sg.theme('DarkGrey6')
    
    layout = [[sg.Text('Movie List')],
            [sg.Listbox(key='Content_List', values="", size=(40, 10), enable_events=True,)],   
            [sg.Input(key='Movie List')],
            [sg.Button('Movies'), sg.Button('TV Shows'), sg.Button('Home'), sg.Exit()]]      

    app = sg.Window('Watch Logger', layout).Finalize()   

    while True:
        event, values = app.Read()
        if event is None or event == 'Exit':                # always check for closed window
            break