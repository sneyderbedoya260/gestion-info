import string

def es_palindromo(texto):
    texto = texto.lower()
    texto = texto.translate(str.maketrans('', '', string.punctuation))
    texto = texto.replace(" ", "")
    return texto == texto[::-1]

frase = input("Ingrese un texto: ")

if es_palindromo(frase):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")