import sys

l1 = float(sys.argv[1])
l2 = float(sys.argv[2])
l3 = float(sys.argv[3])

if l3 < l1 + l2 and l2 < l1 + l3 and l1 < l3 + l2:
    print("As retas formam um triângulo")
else:
    print("As retas não formam um triângulo")