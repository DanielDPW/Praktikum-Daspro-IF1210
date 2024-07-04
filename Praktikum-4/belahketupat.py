def GambarBelahKetupat(N):
    for i in range((N + 1) // 2):
        for j in range((N + 1) // 2 - i - 1):
            print(" ", end='')
        for j in range(2 * i + 1):
            print("*", end='')
        print()
    for i in range(N // 2, 0, -1):
        for j in range((N + 1) // 2 - i):
            print(" ", end='')
        for j in range(2 * i - 1):
            print("*", end='')
        print()
    return

def IsValid(N):
    return N > 0 and N % 2 == 1

N = int(input())

if IsValid(N):
    GambarBelahKetupat(N)
else: 
    print("Masukan tidak valid")