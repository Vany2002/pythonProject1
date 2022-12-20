import csv


def get_books(filename: str, name: str):
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter='|')

        result = [[]]
        result.clear()

        for row in reader:
            if ''.join(row).__contains__(name):
                result.append(row)

        return result

def get_totals(data: [[]], sum = 0, add = 0):
    result = [[]]
    result.clear()

    for row in data:
        count = int(row[3]) * float(row[4])
        if count < sum:
            sum += add
        result.append([row[0], count])

    return result


books = get_books("books.csv", "Python")
result = get_totals(books)

for i in result:
    print(i)