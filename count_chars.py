#frase = "Quantos orangotangos ?"
frase = input()

frase_split = frase.split(" ")

resultado = {}

for palavra in frase_split:
    contar_letras = 0
    for letra in palavra:
        contar_letras += 1
    resultado[palavra] = contar_letras

print(resultado)

    
# input Quantos orangotangos ? 
# output {'Quantos': 7, 'orangotangos': 12 , '?':1}