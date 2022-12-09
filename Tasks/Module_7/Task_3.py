n = int(input())
words = {}

for i in range(n):
    line = input().split()
    if not line[0] in words:
        words[line[0]] = 0
    words[line[0]] += int(line[1])
print(dict(sorted(words.items())))