N = int(input())
a = list(map(int, input().strip().split()))

most = a[0]
most_ctr = 0

for i in range(N):
    ctr = 0
    for j in range(i, N):
        if a[j] == a[i]:
            ctr = ctr + 1
    if ctr > most_ctr:
        most_ctr = ctr
        most = a[i]
    elif ctr == most_ctr:
        most = min(a[i],most)
print(most)