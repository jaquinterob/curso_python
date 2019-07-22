tupla = (1,2,3,4,5,6,7,8,9,0)
elemento = tupla[3]
subtupla = tupla[0:9:2]
print(elemento)
print(subtupla)

#las tuplas se declaran pero no se puede modificar es mas rápida

uno,dos,tres,*cuatro = tupla # se asignan las variables de la lista a cada variable en caso de poner * a una variable se comvierte en una lista

print(uno,dos,tres,cuatro)

#convertir de tupla a list

nueva_lista=list(tupla)
print(nueva_lista)

#convertir de string a arreglo
mensaje = 'Esto es un string que pronto se convertrirá en lista y tupla'
nueva_lista = list(mensaje)
nueva_tupla = tuple(mensaje)

print(nueva_lista)
print(nueva_tupla)