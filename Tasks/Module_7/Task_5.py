countFiles = int(input())
files = {}

for i in range(countFiles):
    line = input().split()
    files[line[0]] = line[1:]

countOperations = int(input())
result = []

for i in range(countOperations):
    line = input().split()
    given = str(files[line[1]]).replace('R', 'read').replace('W', 'write').replace('X', 'execute')

    if given.__contains__(line[0]):
        result.append('OK')
    else:
        result.append('Denied')

print(*result, sep='\n')