"""
List Comprehension

Nós podemos adicionar estruturas condicionais l´goicas nas nossas list comprehension
"""

# Exemplos

#1

numeros = [1, 2, 3, 4, 5, 6, 7]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(f"Pares : {pares}")
print(f"Impares : {impares}")

# Refatorar

# Qualquer número par módulo de 2 é 0 e 0 em Python é False. not False = True

pares = [numero for numero in numeros if not numero % 2 ]
impares = [numero for numero in numeros if numero % 2]

print(f"Pares : {pares}")
print(f"Impares : {impares}")

resultados = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(resultados)
