import csv

def get_books(filename: str, name: str):
    with open(filename, 'r') as file:
        read = csv.reader(file, delimiter='|')
        res = list
        for row in read:
            if row.__contains__(name):
                res.append(row)
        return res
books = get_books("books.csv", "python")