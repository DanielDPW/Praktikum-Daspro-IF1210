import tester

tester.start("output.txt")
file = open("output.txt", 'w')
vokal = ['a','i','u','e','o','A','I','U','E','O']


tab_freq = [0,0,0,0,0]
string = input()
cnt = 0
x = ''
for char in string:
    if char != '.':
        if char == 'A' or char == 'a':
            tab_freq[0] = tab_freq[0] + 1
            cnt = cnt + 1
        elif char == 'I' or char == 'i':
            tab_freq[1] = tab_freq[1] + 1
            cnt = cnt + 1
        elif char == 'U' or char == 'u':
            tab_freq[2] = tab_freq[2] + 1
            cnt = cnt + 1
        elif char == 'E' or char == 'e':
            tab_freq[3] = tab_freq[3] + 1
            cnt = cnt + 1
        elif char == 'O' or char == 'o':
            tab_freq[4] = tab_freq[4] + 1
            cnt = cnt + 1
        x = x + char
    else:
        break

def arr_to_str(arr):
    a = ''
    for char in arr:
        a = a + str(char)
    return a

file.write(arr_to_str(tab_freq) + '\n')
file.write(str(cnt) + '\n')
if cnt != 0:
    file.write(x)
else:
    file.write("Tidak ada huruf")

file.close()

tester.end("output.txt")
