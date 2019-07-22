lista=['python','django','flask','php','javascript','ajax']
print(lista[1])

#tambien se pueden usar indices negativos

print(lista[-1]) #ultimo
print(lista[-2]) #penultimo

#tambien se pueden hacer sublistas

sublista = lista[0:2]#desde : hasta
sublista2 = lista[:3]#python entiende que se puede que empieza desde 0
sublista3 = lista[1:]#se entiende que es desde 3 : el ultimo
sublista4 = lista[1:6:2]#desde:hasta:saltos
sublista5 = lista[::-1]#muestra el inverso de la lista
print(sublista)
print(sublista2)
print(sublista3)
print(sublista4)
print(sublista5)