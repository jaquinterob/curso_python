def saluda():
    print('hola mundo')
    
saluda()

# def crear_mensaje(nombre):
#     return "Hola {}, bienvenido al curso de Python".format(nombre)

# print(crear_mensaje("John"))


def suma(v1,v2,v3):
    return v1+v2+v3

print(suma(1,2,3))

def obtener_curso():
    return "Curso " , "Python " , 3.56#puede devolver arreglos con varios returns

respuesta = obtener_curso()

for item in respuesta:
    print(item)

print(obtener_curso())

# valores por default

def crear_usuario(nombre, apellido, edad=10):#se puede poner valores por defecto y este valor no se necesita en el llamado
    return{
        'nombre' : nombre,
        'apellido' : apellido,
        'nombre_completo' : "{} {}".format(nombre,apellido),
        'edad' : edad
    }
    
print(crear_usuario('John','Quintero',33))

print(crear_usuario(edad=77,nombre='John',apellido='Quintero'))

