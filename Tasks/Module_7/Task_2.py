a = int(input())
words = {}

for i in range(a):
    line = input().split()
    words[line[0]] = line[1]

v = input()

for i in words:
    if words[i] == v:
        print(i)
        break