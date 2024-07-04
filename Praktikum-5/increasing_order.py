def order(x,y):
    sorted = True
    for i in range(x + 1, y + 1):
        if arr[i] <  arr [i - 1]:
            sorted = False
    return sorted
N = int(input())
a = list(map(int, input().strip().split()))
arr = []
count = 0
for i in range(2 * N):
    arr.append(a[i % N])

can = False
for i in range(N):
    if order(N - i, 2 * N - 1 - i):
        count = i
        can = True
        break

if not can:
    print("Tidak")
else:
    print(count)