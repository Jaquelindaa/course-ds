import sys

l1 = int(sys.argv[1])
l2 = int(sys.argv[2])
l3 = int(sys.argv[3])

if not l1 + l2 + l3 == 180 or l1 == 0 or l2 == 0 or l3 == 0:
    print("Ângulos informaos não formam um triângulo!")
elif (l1 == l2 or l1 == l2 or l2 == l3) and (l1 == 90 or l2 == 90 or l3 == 90):
    print("Triângulo formado: ISÓCELES e RETÂNGULO")
elif l1 == l2 or l1 == l2 or l2 == l3:
    print("Triângulo formado: ISÓCELES")
elif l1 == 90 or l2 == 90 or l3 == 90:
    print("Triângulo formado: RETÂNGULO")
else:
    print("Outro tipo de triângulo foi formado!")