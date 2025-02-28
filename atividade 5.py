frase = input("Digite uma frase: ")

num_caracteres = len(frase)
print(f"Número de caracteres na frase: {num_caracteres}")

# Converter todos os caracteres para letras maiúsculas
frase_maiuscula = frase.upper()
print(f"Frase em maiúsculas: {frase_maiuscula}")

# Substituir uma palavra específica por outra fornecida pelo usuário
palavra_antiga = input("Digite a palavra que deseja substituir: ")
palavra_nova = input("Digite a nova palavra: ")
frase_modificada = frase.replace(palavra_antiga, palavra_nova)
print(f"Frase modificada: {frase_modificada}")

# Dividir a frase em uma lista de palavras e exibi-la
lista_palavras = frase.split()
print(f"Lista de palavras: {lista_palavras}")