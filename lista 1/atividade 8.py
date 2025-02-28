frase = input("Digite uma frase: ").lower()

vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for letra in frase:
    if letra in vogais:
        vogais[letra] += 1

for vogal, quantidade in vogais.items():
    print(f"A vogal '{vogal}' aparece {quantidade} vezes")