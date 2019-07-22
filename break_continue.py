titulo = "Curso de Python"

for caracter in titulo:
    if caracter == 'P':
        break#interrumpe el ciclo
print(caracter)

for caracter in titulo:
    if caracter == 'P':
        continue#interrumpe el ciclo
print(caracter)