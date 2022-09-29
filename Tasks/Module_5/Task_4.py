a = int(input())
answer = 0
while a != 0:
    x = int(input())
    if x != 0 and a < x:
        answer += 1
    a = x
print(answer)