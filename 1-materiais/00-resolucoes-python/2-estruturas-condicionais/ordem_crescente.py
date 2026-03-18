import sys

num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
num3 = float(sys.argv[3])
ordem = []

if num1 < num2 and num1 < num3:
    ordem.append(num1)
    if num2 < num3:
        ordem.append(num2)
        ordem.append(num3)
    else:
        ordem.append(num3)
        ordem.append(num2)
elif num2 < num1 and num2 < num3:
    ordem.append(num2)
    if num1 < num3:
        ordem.append(num1)
        ordem.append(num3)
    else:
        ordem.append(num3)
        ordem.append(num1)
elif num3 < num2 and num3 < num1:
    ordem.append(num3)
    if num2 < num1:
        ordem.append(num2)
        ordem.append(num1)
    else:
        ordem.append(num1)
        ordem.append(num2)

print(ordem)