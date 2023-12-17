#calculadora em python
import math
espaco = (20*"-")
print(espaco,"vamos calcular",espaco)

numero1 = float(input("digite o primeiro numero:  "))

print("escolha a operação")
print("1:somar")
print("2:subtrair")
print("3:dividir")
print("4:multiplicar")

operacao = int(input(f"digite a operação:\n"))
numero2 = float(input("digite o segundo numero: "))

somar = numero1 + numero2
diminuir = numero1 - numero2
multiplicar = numero1* numero2
dividir = numero1/ numero2

if operacao == 1:
	print("o resultado é:", somar)
elif operacao == 2:
	print("o resultado é:", diminuir)
elif operacao == 4:
	print("o resultado é:", multiplicar)
elif operacao == 3:
	print("o resultado é:",dividir)
else :
	print("operação invalida!")

