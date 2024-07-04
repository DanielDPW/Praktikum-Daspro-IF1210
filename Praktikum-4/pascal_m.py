N = int(input())
M = int(input())

a = [[M] * (i + 1) for i in range(N)]

for i in range(N):
    for j in range(i + 1):
        if j != 0 and j != i:
            a[i][j] = a[i - 1][j - 1] + a [i - 1] [j]

for i in range(N):
    for j in range(i + 1):
        if j != i:
            print(a[i][j],end=' ')
        else:
            print(a[i][j])