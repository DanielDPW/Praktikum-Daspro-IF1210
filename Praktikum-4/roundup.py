N = int(input())
if N <= 0 or N > 100:
    print("Tidak valid")
if 0 < N <= 100:
    a = list(map(int, input("").split()))
    X = int(input())
    smallest_found = False
    smallest2 = -1
    min = a[0]
    for i in range(N - 1):
        for j in range(i + 1, N):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]

    for i in a:
        if smallest_found:
            smallest2 = i
            break
        if i > X:
            smallest_found = True

    print(smallest2)
        