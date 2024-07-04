N = int(input())
X = int(input())
a = list(map(int, input("").split()))

equal = False
min = abs(a[0] - X)
max = abs(a[0] - X)
min_value = 0
max_value = 0
for i in range(N):
    if X == a[i]:
        equal = True
    elif abs(a[i] - X) < min:
        min = abs(a[i] - X)
        min_value = a[i]
    elif abs(a[i] - X) > max:
        max = abs(a[i] - X)
        max_value = a[i]

if equal == True:
    print(X)
else:
    print("TIDAK ADA")
print(min_value)
print(max_value)