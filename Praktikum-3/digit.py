arr = [0 for i in range(10)]
c = 0

while c < 100:
    x = int(input())
    if x < 0:
        break
    elif x == 0:
        arr[0] = arr[0] + 1
    else:
        while x != 0:
            arr[x % 10] = arr[x % 10] + 1
            x = x // 10
    c = c + 1

print(c)
for i in range(10):
    if arr[i] != 0:
        print("%d :" % i + " %d" % arr[i])