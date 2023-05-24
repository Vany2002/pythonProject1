import os
import PySimpleGUI as sg


def change_dir():
    layout = [
        [sg.Text('current directory:'), sg.Text(os.getcwd(), key='dir')],
        [sg.Text('Choose a new directory:'), sg.FolderBrowse('Find')],
        [sg.Button('Go'), sg.Button('Exit')]
    ]
    window = sg.Window('Change directory', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == 'Go':
            if values['Find'] == '':
                sg.popup('Directory not changed')
            else:
                new_dir = values['Find']
                os.chdir(new_dir)
                sg.popup(f'Current directory changed to {new_dir}')
                break

    window.close()
    return os.getcwd()