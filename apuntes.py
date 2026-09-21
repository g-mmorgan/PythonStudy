
def comenatarios():
    print("#Los comentarios van con # no //)")
    print("Podemo comentar con \"\"\" ")

"""
 Esto técnicamente no es un comentario
 Es un string pero como no esta dentro de una variable
 Pues python lo ignora
 Y se usa como comentarios de varias lineas
 """

print ("Hola mundo")

#Los comentarios van con # no //
def indentacion():
    if 2>1:
        print("En python es muy importante la indentacion")

        print("Print es una sentencia"); print('Puedes apilar sentencias así, también usar comilla simple')

        print("Toda esta frase",end=" "); print("está en diferentes print pero misma linea")

        print("Podemos imprimir numeros", 4092380, "\nY sumas", 3+4)


def variables():

    print("Podemos declarar variables sin tipos")

    var1 = "Hola"
    var2  = 33

    print(var1,var2)
    #Tambien podemos asignarles un tipo mediante casting

    var3 = str(3)       # "3"
    var4= int(3)        # 3
    var5 = float(3)     # 3.0
    
    #Podemos obtener el tipo de variable que es
    var6 = type(var5)
    print("Y podemos ver obtener el tipo de una variable")
    print(var6) #<class 'float'>

def variables2():
    print ("Las varibles son case-sensitive")
    var = 23
    Var = 22
    print(var,Var)


def variables3():
    i1 = i2 = i3 = 2
    print("Podemos declarar e incializar variables a la vez y al mismo valor",i1,i2,i3)

    print("Podemos declarar e incializar tres variables a los elementos de una lista")
    lista = [1,2,3]
    l1,l2,l3 = lista
    print(l1,l2,l3); print(lista)


#VARIABLES GLOBALES
x = "Hola soy una variable global"
#si estan definidas fuera de una funcion son globales

def vGlobal1():
    print("Primera funcion usando una variable global", x)


def vGlobal2():
    var1 = "Se puede crear variables locales a función con nombres de otra variables"
    print(var1)

def vGlobal3():
    print("También podemos modificar variables globales desde funcion si usamos global")
    global x
    x = "Nueva variable x"
    print(x)

def dataTypes():
    print("Las variables pueden contener datos de diferente tipo")
    print("de texto, numericas, listas, mapas, boolean, binarios, y NoneType")
    print("Podemos usar \"type(x)\" ")

"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""



def main():
    comenatarios()
    indentacion()
    variables()
    variables2()
    variables3()
    vGlobal1()
    vGlobal2()
    vGlobal3()
    dataTypes()

main()