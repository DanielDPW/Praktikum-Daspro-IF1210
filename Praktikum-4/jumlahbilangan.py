x = int(input())
y = int(input())
c = 0
for i in range(x,y + 1):
    if i % 3 == 0 or i % 4 == 0:
        c = c + 1

if c == 0:
    print("Tidak Ada")
else:
    print(c)