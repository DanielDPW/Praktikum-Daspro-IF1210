import tester
def remove_whitespace(layer):
    x = ''
    for i in layer:
        if i != '\n':
            x = x + i
    return x

def turn_to_array(str):
    x = ''
    y = []
    num = ['0','1','2','3','4','5','6','7','8','9','-']
    for char in str:
        if char in num and not '':
            x = x + char
        else:
            y.append(x)
            x = ''
    if x:
        y.append(x)
    return y

def merge_array(arr1, arr2):
    for i in range(arr2):
        arr1.append(arr2[i])
    return arr1
tester.start("input.txt")
file = open("input.txt",'r')

layer = remove_whitespace(file.readline())

if int(layer) <= 0:
    print("Jumlah layer: 0")
else:
    print("Jumlah layer: " + str(layer) + '\n')
    for i in range(1, int(layer) + 1):
        print("Layer ke-" + str(i))
        print("Fungsi aktivasi: " + str(remove_whitespace(file.readline())))
        jumlah_neuron = int(remove_whitespace(file.readline()))
        print("Jumlah neuron: " + str(jumlah_neuron))
        n = []
        for j in range(jumlah_neuron):
            x = turn_to_array(file.readline())
            for k in range(len(x)):
                n.append(x[k])
        print("Weight neuron: " + str(n))
        print("Bias: " + str(turn_to_array(file.readline())))
        if i < int(layer):
            print("")
file.close()
        
tester.end("input.txt")