import PySimpleGUI as sg
import os

from Practika2.Pr_16.Pr_16_Task_1 import change_dir
from Practika2.Pr_16.Pr_16_Task_2 import change
from Practika2.Pr_16.Pr_16_Task_3 import delete

layout = [
    [sg.Text('Choose an action:')],
    [sg.Radio('Change working directory', "action", default=True, key='change_dir')],
    [sg.Radio('Convert PDF to Docx', "action", key='pdf_to_docx')],
    [sg.Radio('Convert Doc, Docx to PDF', "action", key='doc_to_pdf')],
    [sg.Radio('Compress Image', "action", key='compress_image')],
    [sg.Radio('Delete group of files', "action", key='delete_files')],
    [sg.Button('Run', key='execute'), sg.Button(key='exit')]
]

window = sg.Window('File manager').Layout(layout)

catalog = os.getcwd()

while True:
    event, values = window.Read()
    if event is None or event == 'exit':
        break
    if event == 'execute':
        if values['change_dir']:
            catalog = change_dir()
            pass

        elif values['pdf_to_docx']:
            change(catalog, ['pdf'])
            pass

        elif values['doc_to_pdf']:
            change(catalog, ['doc', 'docx'])
            pass

        elif values['compress_image']:
            change(catalog, ['img', 'png', 'jpg', 'jpeg', 'bmp'])
            pass

        elif values['delete_files']:
            delete(catalog)
            pass

window.Close()