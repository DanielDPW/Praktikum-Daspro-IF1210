N = int(input())
a = list(map(int, input("").split()))

c = 0
sumofdigits = 0
for i in range(N):
    while a[i] >= 10:
        while a[i] > 0:
            sumofdigits = sumofdigits + a[i] % 10
            a[i] = a[i] // 10
        a[i] = sumofdigits
        sumofdigits = 0
        c = c + 1
print(c)