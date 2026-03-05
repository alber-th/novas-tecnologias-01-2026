# Desafio 1 - Calculadora de IMC

nome = input("Qual o seu nome? ")
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

print()
print(f"Olá, {nome}!")
print(f"Seu IMC é: {round(imc, 2)}")
print(f"Classificação: {classificacao}")
