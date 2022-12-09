a = input().split()
words = {}

for i in range(len(a)):
    line = input().split()

    if not a[i] in words:
        words[a[i]] = 0
    print(words[a[i]])
    words[a[i]] += 1