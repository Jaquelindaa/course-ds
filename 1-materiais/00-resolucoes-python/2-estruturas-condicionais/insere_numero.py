import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = int(sys.argv[3])
num4 = int(sys.argv[4])

# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# num4 = int(input())

if not num3 > num2 and num2 > num1:
    print("Os primeiros três arugumentos prescisam estar em ordem crescente!")
else:
    ordem = [num3, num2, num1]
    if num4 < num3:
        if num4 < num2:
            if num4 < num1:
                ordem.insert(3, num4)
            else:
                ordem.insert(2, num4)
        else:
            ordem.insert(1, num4)
    else:
        ordem.insert(0, num4)

print(ordem)