lista=[8.17,90,1,5,44,1.32]

#lista.sort()#Ordena 
#lista.sort(reverse=True)#ordena descendente

menor = min(lista)
mayor = max(lista)
longitud_lista = len(lista)
res = 8.17 in lista #pregunta si se encuentra en la lista
res2 = lista.index(8.17)#busca el valor pasado por parametro y devuelve su indice en el arreglo
res3 = lista.count(5)#cuenta las veces que un elemento está en la lista


#print(lista)
"""print(menor)
print(mayor)
print(longitud_lista)
print(res)"""
print(res2)
print(res3)