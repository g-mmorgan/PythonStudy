import random
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

    #tambien tenemos para comprobar si son instacias de tipos
    print(isinstance(var1,str))

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
    print("De texto, numericas, listas, mapas, boolean, binarios, y NoneType")
    print("Podemos usar \"type(x)\" ")

def complejos():
    print("Los numero complejos usan j como la parte imaginaria")
    x = 5j
    y = 3+6j
    z= -5j
    print(type(x),y,z)

def numericos():
    print("Podemos cambiar el tipo de una variable numerica con un cast")
    x = 1    # int
    y = 2.8  # float
    z = 1j   # complex

    #convert from int to float:
    a = float(x)

    #convert from float to int:
    b = int(y)

    #convert from int to complex:
    c = complex(x)

    print(type(a))
    print(type(b))
    print(type(c))


def rand():
    print("Pyhton no tiene una funcion random pero si podemos importar el modulo random" \
        "y generar un numero")
    print(random.randrange(1,10))


def cadenas():
    print("Podemos usar 'comilla simple' dentro de comillas doble")
    a = """
        string de varias lineas
        se puede hacer asi"""
    print("Usamos len para calculr tamaño de string",len(a))
    #también podemos comprobar si una palabra esta dentro del string
    txt = "Hola qué tal estas amigo?"
    b = bool("Hola" in txt) #b = true
    print(b)
    #comprobamos si no esta
    b = "Adios" not in txt
    print(b)
    c = "Hola Mundo"
    print("Imprimimos un rango dentro de un string '",c[2:6],"'")
    #no se incluye la ultima posicion 
    #podemos poner de principio hasta una pos o de pos a final
        # print(c[:5]) o print(c[5:])

    #podemos hacer indexacion negativa
    # H O L A Q U E T A  L
    #-x              -2 -1
    #sirve para imprimir el final si no sabemos la longitud del string

def mayusculas():
    print("Podemos cambiar texto a lowe o upper case")
    a = "Hola mundo"
    print(a.upper())
    print(a.lower())
    #luego tenemos el a.strip() que quita cualquier espacios del principio o el final

    #podemos sustituir strings a.replace("H","J")
    #separador print(a.split("a")) divide por

def formatoCadenas():
    #podemos 
    edad = 22
    txt = "Hola mi edad es "+ edad
    #eso es una forma o podemos
    txt2 = f"Hola mi edad es {edad}"

    pi = 3.141592
    txtpi = f"Pi es {pi:.2f} con dos decimales"
    #tambien podemos hacer mates directamente
    mates = f"La suma de 3+4 es {4+3}"

def booleanos():
    print("En python para comparar booleanos en vez de && o || como en java usamos and or y not")



def listas():
    lista1 = [1,2,3,4]
    lista2 = list((1,2,3,4))
    #si no usamos el constructor declaramos con  [] si no con ()

    #añadir elementos a la lista dos formas
    lista1.append(6)    #añade al final el elemento
    lista2.insert(2,78) #añade en un indice desplazando el resto
    print(lista2)

    lista1.extend(lista2) #añadimos al final de lista1 la lista2

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
    complejos()
    numericos()
    rand()
    cadenas()
    mayusculas()
    booleanos()
    listas()

main()