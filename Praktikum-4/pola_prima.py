N = int(input())
prima = []

angka = 2
def cek_prima(x):
    if x <= 1:
        return False
    elif 1 < x <= 3:
        return True
    else:
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True
while len(prima) < N:
    if cek_prima(angka):
        prima.append(angka)
    angka = angka + 1

if N < 1:
    print("Tidak valid")
else:
    for i in range(N):
        for j in range(i, 0, -1):
            print(prima[j], end = ' ')
        for j in range(N - i):
            if j != N - i - 1:
                print(prima[j], end = ' ')
            else:
                print(prima[j])

