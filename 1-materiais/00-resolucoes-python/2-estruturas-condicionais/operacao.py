num_1 = float(input("Informe um núemero: "))
num_2 = float(input("Informe um núemero: "))

print("Operações disponíveis:")
print("Soma -> digite '+'")
print("Subtração -> digite '-'")
print("Divisão -> digite '/'")
print("Multiplicação -> digite '*")
operacao = input("Digite sua escolha: ")

if operacao == "+":
    resultado = num_1 + num_2
elif operacao == "-":
    resultado = num_1 - num_2
elif operacao == "*":
    resultado = num_1 * num_2
elif operacao == "/":
    if num_2 == 0:
        resultado ="Não é possível realizar divisões por zero"
    else:
        resultado = num_1 * num_2

print(f"Operação: {num_1}{operacao}{num_2}")
print(f"Resultado: {resultado}")