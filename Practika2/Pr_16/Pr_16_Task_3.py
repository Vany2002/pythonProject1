import os
import PySimpleGUI as sg


def menu_delete():
    layout = [
        [sg.Text('Choose the type of remova')],
        [sg.Radio('Delete files starting with a substring', "RADIO1", default=True, key='option1')],
        [sg.Radio('Delete files ending with a substring', "RADIO1", key='option2')],
        [sg.Radio('Delete files containing a substring in their name', "RADIO1", key='option3')],
        [sg.Radio('Delete files with substring extension', "RADIO1", key='option4')],
        [sg.Button('Delete'), sg.Button('Cancel')]
    ]

    window = sg.Window('Deleting files', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Cancel':
            window.close()
            return None

        if event == 'Delete':
            if values['option1']:
                window.close()
                return 1
            elif values['option2']:
                window.close()
                return 2
            elif values['option3']:
                window.close()
                return 3
            elif values['option4']:
                window.close()
                return 4


def delete(catalog):
    delete_option = menu_delete()

    if delete_option is None:
        return

    sub_string = sg.popup_get_text('Enter a substring:')

    files = []
    for file in os.listdir(catalog):
        if os.path.isfile(file):
            files.append(file)

    delete_files = []

    if delete_option == 1:
        for file in files:
            if file[0:len(sub_string)] == sub_string:
                delete_files.append(file)

    if delete_option == 2:
        for file in files:
            filename = file.split('.')[0]
            if filename[-len(sub_string):] == sub_string:
                delete_files.append(file)

    if delete_option == 3:
        for file in files:
            filename = file.split('.')[0]
            if filename.__contains__(sub_string):
                delete_files.append(file)

    if delete_option == 4:
        for file in files:
            format = file.split('.')[1]
            if format == sub_string:
                delete_files.append(file)

    if len(delete_files) == 0:
        sg.popup('Files to delete not found')
        return

    layout = [
        [sg.Text('Do you really want to delete files?')],
        [sg.Listbox(delete_files, size=(50, len(delete_files)))],
        [sg.Button('Yes'), sg.Button('No')]
    ]

    window = sg.Window('Deleting files', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'No':
            window.close()
            break

        if event == 'Yes':
            for file in delete_files:
                os.remove(file)
            sg.popup('Files deleted successfully')
            window.close()
            break