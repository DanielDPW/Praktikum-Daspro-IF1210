ip = float(input())
pot = float(input())

if ip >= 3.5:
    print(4)
elif ip < 3.5 and pot < 1:
    print(1)
elif 2 <= ip < 3.5 and 1 <= pot < 5:
    print(3)
elif ip < 2 and 1 <= pot < 5:
    print(2)
else:
    print(0)