x = input()
y = []
valid = True
for i in x:
    if i == "(" or i == "[" or i == "{":
        y.append(i)
    elif i == ")" or i == "]" or i == "}":
        if len(y) == 0:
            valid = False
            break
        elif i == ")" and y[-1] == "(":
            y.pop()
        elif i == "]" and y[-1] == "[":
            y.pop()
        elif i == "}" and y[-1] == "{":
            y.pop()
        else:
            valid = False
            break

if len(y) == 0 and valid == True:
    print("valid")
else:
    print("tidak valid")