import tester
tester.start("input.csv")

file = open("input.csv","r")

def ascending_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j], arr[i]
    return arr

data = []
for text in file:
   row = text.strip("\n")
   data.append(row.split(","))

umur = []
c = 0

for i in range(1, len(data)):
    if int(data[i][3]) > 75:
        c = c + 1
    umur.append(int(data[i][2]))

umur = ascending_sort(umur)

print(c)
print(umur[1])
file.close()

tester.end("input.csv")