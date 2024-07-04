N = int(input())
a = list(map(int, input().strip().split()))

smallest_diff = abs(a[1] - a[0])
for i in range(N):
    for j in range(i + 1, N):
        if abs(a[j] - a[i]) < smallest_diff:
            smallest_diff = abs(a[j] - a[i])

print(smallest_diff)