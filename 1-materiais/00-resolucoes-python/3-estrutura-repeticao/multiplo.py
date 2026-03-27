import sys

num = int(sys.argv[1])
multiplos = []

for n in range(0, 100):
    multiplos.append(num*n)

print(multiplos)
