diccionario = {}

diccionario["nombre"]="codi"
print(diccionario)
valor= diccionario['nombre']
print(valor)
diccionario["nombre"]= "Juan"
print(diccionario["nombre"])

diccionario = {"a":1,"b":2,"c":3,"a":4}#si la clave se sobre escribe
print(diccionario)

res = "a" in diccionario#pregunta si ha estra
print(res)

res = diccionario.get("z","no está la llave")#busca el parametro 12 y si no esta devuelve el parametro 2 (cualquier tipo)
print(res)

res = diccionario.setdefault("z",{})#asigna por defecto una llave el segundo parametrol
print(res)

