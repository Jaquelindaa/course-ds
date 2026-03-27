import sys

n = int(sys.argv[1])

E = 0

for i in range(0, n + 1):
    fatorial = 1

    for j in range(1, i + 1):
        fatorial = fatorial * j

    E = E + (1 / fatorial)

print(f"{E:.2f}")