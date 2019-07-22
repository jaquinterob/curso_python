lenguajes = "Python; Java; Ruby; PHP; Swift; JavaScript; C#; C; C++"
resultado = lenguajes.split()#aqui toma por defecto el espacio como separador
print(resultado)
separador = "; "

resultado = lenguajes.split(separador)#se escoje el separador
print(resultado)

nuevo_string = " ".join(resultado)#se convierte de list a String
print(nuevo_string)

texto = """
string
multilinea
para
ejemplo
"""
nuevo_string = texto.splitlines()# acá se dividen los saltos de lineas en elemtos de una nueva lista
print(nuevo_string)
