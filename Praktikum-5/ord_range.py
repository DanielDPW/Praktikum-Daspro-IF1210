c1 = input()
c2 = input()

if not 65 <= ord(c1) <= 90 or not 65 <= ord(c2) <= 90:
    print("Tidak valid")
else:
    print(min(abs(ord(c2) - ord(c1)), 26 - (abs(ord(c2) - ord(c1)))))