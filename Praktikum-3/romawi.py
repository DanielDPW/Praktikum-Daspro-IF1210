x = input()
hasil = 0
y = ["" for i in range(len(x))]
previous_value = 0
angka = 0
for i in range(len(x)):
    y[i] = x[len(x) - 1 - i]

for j in y:
    current_value = 0
    if j == "I":
        current_value = 1
    elif j == "V":
        current_value = 5
    elif j == "X":
        current_value = 10
    elif j == "L":
        current_value = 50
    elif j == "C":
        current_value = 100
    elif j == "D":
        current_value = 500
    elif j == "M":
        current_value = 1000
    
    if current_value < previous_value:
        angka = angka - current_value
    else:
        angka = angka + current_value
    previous_value = current_value
print(angka)