texto = input("Digite uma frase: ")

capitalize = " ".join([palavra.capitalize() for palavra in texto.split()])
lowercase = texto.lower()
uppercase = texto.upper()
title = texto.title()

print(f"• Capitalize: {capitalize}")
print(f"• Lowercase: {lowercase}")
print(f"• Uppercase: {uppercase}")
print(f"• Title: {title}")
