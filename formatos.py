texto = '   Curso de Python 3 Python    '
resultado = texto.capitalize()
print(resultado)
resultado = texto.swapcase()#cambia las mayusculas a minusculas y al reves
print(resultado)
resultado = texto.upper()
print(resultado)
resultado = texto.lower()
print(resultado)
resultado = texto.isupper()
print(resultado)
resultado = texto.islower()
print(resultado)
resultado = texto.title()
print(resultado)
resultado = texto.replace("Python", "Ruby", 1)#reemplaza el numero de veces que le indiquemos
print(resultado)
resultado = texto.strip()#borra los espacios en blanco al inicio y al final
print(resultado)
resultado = "Curso de %s %s" %('tal','cosa')#es una forma de poner variables dentro de un string
print(resultado)
resultado = "Curso de {b} {a}".format(a="Python",b='3')# otra forma de formatear.
print(resultado)
