import os
from pdf2docx import Converter
from docx2pdf import convert
from PIL import Image

if __name__ == '__main__':
    print('PyCharm')
    act = -1
    while act != 5:
        cur_path = os.getcwd()
        act = int(input(
            f"""
Текущий каталог: {cur_path}

Выберите действие: 

0. Сменить рабочий каталог
1. Преобразовать PDF в Docx
2. Преобразовать Docx в PDF
3. Произвести сжатие изображений
4. Удалить группу файлов
5. Выход 
"""))
        print(f"Ваш выбор: {act}")
        if act == 0:
            path = input("Укажите корректный путь к рабочему каталогу: ")
            os.chdir(path)
        # pdf2docx
        if act == 1:
            files = []
            for file in os.listdir(path):
                if file.endswith(".pdf"):
                    files.append(f'{file[:-4]}')
            c = 1
            for i in files:
                print(f"{c}. {i}.pdf")
                c += 1
            num_file = int(input("Введите номер файла для преобразования (0 - выбрать все): "))
            if num_file == 0:
                for i in files:
                    pdf_file = f'{path}\{i}.pdf'
                    docx_file = f'{path}\{i}.docx'
                    cv = Converter(pdf_file)
                    cv.convert(docx_file)
                    cv.close()
            else:
                pdf_file = f"{path}\{files[num_file - 1]}.pdf"
                docx_file = f'{path}\{files[num_file - 1]}.docx'
                cv = Converter(pdf_file)
                cv.convert(docx_file)
                cv.close()

        # docx2pdf
        if act == 2:
            files = []
            for file in os.listdir(path):
                if file.endswith(".docx"):
                    files.append(f'{file}')
            c = 1
            for i in files:
                print(f"{c}. {i}")
                c += 1
            num_file = int(input("Введите номер файла для преобразования (0 - выбрать все): "))
            if num_file == 0:
                for i in files:
                    convert(f"{path}\{i}", f"{path}\{i[:-5]}.pdf")
            else:
                convert(f"{path}\{files[num_file - 1]}", f"{path}\{files[num_file - 1][:-5]}.pdf")

        # pillow
        if act == 3:
            files = []
            for file in os.listdir(path):
                if file.endswith(".jpg") or file.endswith(".jpeg"):
                    files.append(f'{file}')
            c = 1
            for i in files:
                print(f"{c}. {i}")
                c += 1
            num_file = int(input("Введите номер файла для преобразования (0 - выбрать все): "))
            scale = int(input("Введите параметры сжатия (от 1 до 100%): "))
            if num_file == 0:
                for i in files:
                    image_path = f"{path}\{i}"
                    image_file = Image.open(image_path)
                    image_file.save(f"{i}2.jpeg", quality=scale)
            else:
                image_path = f"{path}\{files[num_file - 1]}"
                image_file = Image.open(image_path)
                image_file.save(f"{files[num_file - 1]}2.jpeg", quality=scale)
        if act == 4:
            print(
                """
                1. Удалить все файлы начинающиеся на определенную строку
                2. Удалить все файлы заканчивающиеся на определенную строку
                3. Удалить все файлы содержащие определенную строку 
                4. Удалить все файлы по расширению        
                """)
            key = int(input("Введите номер действия: "))
            substr = input("Введите подстроку: ")
            lst = os.listdir(path)
            if key == 1:
                for i in lst:
                    if i.startswith(substr):
                        os.remove(f"{path}\{i}")
                        print(f"Файл: {i} успешно удалён!")
            if key == 2:
                for i in lst:
                    if i.split(".")[0].endswith(substr):
                        os.remove(f"{path}\{i}")
                        print(f"Файл: {i} успешно удалён!")
            if key == 3:
                for i in lst:
                    if i.count(substr) != 0:
                        os.remove(f"{path}\{i}")
                        print(f"Файл: {i} успешно удалён!")
            if key == 4:
                for i in lst:
                    if i.endswith(substr):
                        os.remove(f"{path}\{i}")
                        print(f"Файл: {i} успешно удалён!")
