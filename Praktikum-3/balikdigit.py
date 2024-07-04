x = int(input())
y = 0
isNeg = x < 0
if x < 0:
    x = -1 * x

while x != 0:
    y = y * 10
    y = y + (x % 10)
    x = x // 10

if isNeg:
    print(-1 * y)
else:
    print(y)
