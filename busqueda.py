mensaje = "Este es un texto un poco grande en cuento a longitud se refiere"

res = mensaje.count('texto')#cuenta las veces que aparece el texto en el string
print(res)
res = "text" in mensaje#devuelve boolean
print(res)
res = mensaje.find("text")#devuelve el indice del inicio de la paralabra buscada sino encuentra devuelve -1
print(res)
res=mensaje.startswith('Este')# muestra si empieza con el texto pasado por parametro
print(res)
res=mensaje.endswith('e')
print(res)