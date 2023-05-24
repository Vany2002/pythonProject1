import os
import PySimpleGUI as sg
from docx2pdf import convert
from pdf2docx import parse
from PIL import Image

def find_files(dir, format):
    files = []
    for file in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, file)):
            if format.__contains__(file.split('.')[-1]):
                files.append(file)

    return files


def convert_file(file):
    format_file = file.split('.')[-1]

    if format_file == 'pdf':
        new_file = file.replace(format_file, 'docx')

        try:
            parse(file, new_file)
        except:
            sg.popup(f'Unable to convert file {file} in format docx')

    elif format_file == 'doc' or format_file == 'docx':
        new_file = file.replace(format_file, 'pdf')

        try:
            convert(file, new_file)
        except:
            sg.popup(f'Unable to convert file {file} in format pdf')

    else:
        layout = [[sg.Text('Specify the compression options in %:'),
                   sg.Input(key='quality', size=(5, 1)), sg.Button('Compress'),
                   sg.Button('Cancel')]]

        window = sg.Window('Image Compression', layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == 'Cancel':
                break

            if event == 'Compress':
                quality = values['quality']

                try:
                    image_path = file
                    image_file = Image.open(image_path)
                    image_file.save(file, quality=quality)
                    break
                except:
                    sg.popup(f'Unable to compress image {file}')

        window.close()


def change(dir, format):
    files = find_files(dir, format)
    if len(files) == 0:
        sg.popup(f'There are no format files in the folder {", ".join(format)}')
        return

    layout = [[sg.Text('Select files to convert:')],
              [sg.Listbox(values=files, select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, size=(40, 10), key='files')],
              [sg.Button('Convert'), sg.Button('Cancel')]]

    window = sg.Window('File converter', layout)

    while True:
        event, values = window.read()

        if event in (None, 'Cancel'):
            break

        if event == 'Convert':
            selected_files = values['files']
            for file in selected_files:
                convert_file(os.path.join(dir, file))

            sg.popup('Conversion completed')
            break

    window.close()