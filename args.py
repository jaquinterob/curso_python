def suma(*args):
    total = 0
    for valor in args:
        total+=valor
    return total
print(suma(10,20,30,40,1200))# sin importar la cantidad de los argumentos

def suma(**kwargs):
    print(kwargs)
    
suma(v=3,v2=2,v3=5)
