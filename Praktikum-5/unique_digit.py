def check(x):
    valid = True
    for i in range(len(a)):
        if a[i] == x:
            valid = False
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] + a[j] == x:
                valid = False
    return valid
            
n = 0
a = []
while True:
    n = int(input())
    if n == -9999:
        break
    else:
        a.append(n)

num = 1
if len(a) > 0:
    while not check(num):
        num = num + 1
print(num)