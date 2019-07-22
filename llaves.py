diccionario = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}

res = diccionario.keys()#muestra las llaves
print(res)

res = diccionario.values()#muestras los valoes
print(res)

res = diccionario.items()#muestra los pares llave valor
print(res)

#eliminar llaves

res = (len(diccionario))
print(res)

del diccionario["a"]
print(diccionario)

res = diccionario.pop("b")#elimina el elemento correspondiente a la llave y devuelve el valor del elemto eliminado
print(res)


