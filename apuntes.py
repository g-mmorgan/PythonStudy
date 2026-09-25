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

print ("Hola mundo!\n")

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
    #como modificar listas
    #append añade un elemento nuevo al final
    list1 = [1,"adios",4.7987, "hola"]
    list1.append("nuevo")
    

    print(list1)#[1, 'adios', 4.7987, 'hola', 'nuevo']
    #podemos insertar en una posicion concreta no elimina elementos se mete en medio
    list1.insert(1,"hasta luego")
    print(list1) #[1, 'hasta luego', 'adios', 4.7987, 'hola', 'nuevo']


    list2 = ["nueva lista", "final"]
    #añade variables o listas o tuplas al final de la lista
    list1.extend(list2)
    print(list1)#[1, 'hasta luego', 'adios', 4.7987, 'hola', 'nuevo', 'nueva lista', 'final']


    #podemos borrar elementos de la lista
    list1.remove(1)
    print(list1)#['hasta luego', 'adios', 4.7987, 'hola', 'nuevo', 'nueva lista', 'final']


    #podemos borrar por indice
    list1.pop(3)# indice 3 hola
    print(list1)#['hasta luego', 'adios', 4.7987, 'nuevo', 'nueva lista', 'final']


    list1.pop()#borramos ultimo elemento 
    print(list1)#['hasta luego', 'adios', 4.7987, 'nuevo', 'nueva lista']


    del list2 # borramos toda la lista sirve para todas las variables
    """print(list2)""" #error 

    #tambien podemos vaciar sin borrar la variable
    list1.clear() #no se olviden los parentesis
    print("Lista1:", list1) 

    #podemos copiar listas
    #lista4 = lista1 NO SIRVE
    #lo que esta haciendo es igualar punteros lo que le pase a lista1 le afecta a lista4
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    lista4 = fruits.copy()
        #otra formas    lista4=list(fruits)
        #               lista4=fruits[:]
    fruits.pop(0)
    print(lista4) #no se ha borrado apple 

def bucleEnListas():
    lista1 = [0,2,4,6,8,10]
    lista2=["a","b","c","d","e"]
    lista3=[1,"a",2,"b",3,"c"]

    #LA FORMA MAS SENCILLA
    for x in lista1:
        print(x)
    print("\n")
    #PODEMOS USAR UN RANGO Y LA LONGITUD DE LISTA
    for i in range(len(lista2)):
        print(lista2[i])
    print("\n")
    #USANDO BUCLE WHILE
    j = 0
    while j < len(lista3):
        print(lista3[j])
        j += 1
    print("\n")
    
    #Bucle con comprension de lista
    primos=[2,3,5,7,11,13,17]
    [print(x) for x in primos]

    #RANGE  

    """
        range() en Python genera una secuencia inmutable de números y se usa comúnmente en bucles for. Acepta hasta 3 parámetros:
        1. range(stop): genera de 0 hasta stop-1
        range(5)  # 0, 1, 2, 3, 4
        2. range(inicio, stop): genera de inicio hasta stop-1
        range(2, 6)  # 2, 3, 4, 5
        3. range(inicio, stop, paso): igual al anterior pero con un salto (paso)
        range(0, 10, 2)  # 0, 2, 4, 6, 8
    """

def comprensionDeLista():
    #sirve para crear nuevas listas a base de otras ya existentes
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    lista2 = [x for x in fruits if "a" in x]
    print(lista2)

    #SYNTAXIS
    """
    newlist = [expression for item in iterable if condition == True]
    
    ej:
    newlist = [x for x in range(10)]
    newlist = [x for x in fruits]
    newlist = [x.upper() for x in fruits]
    newlist = ['hello' for x in fruits]
    newlist = [x if x != "banana" else "orange" for x in fruits]ç

    """
    
def ordenarLista():
    lista1 = [3,43534,1,-76,7,73926780348,-12,21,56,63]
    lista2=["e","c","d","a","b",]
    lista3=[3,"c",1,"b","a",2]

    #sort a secas ordena de forma alfabetica y de menor a mayor
    lista1.sort()
    print(lista1)

    #sort con reverse= true ordena de la Z a A y de mayor a menor
    lista2.sort(reverse = True)
    print(lista2)

    #lista3.sort() no se puede ordenar listas mixtas

    #ordenar usando un criterio concreto
    def myfunc(n):
        return abs(n - 50)#abs es valor absoluto -7 = 7 y 6 = 6

    thislist = [100, 50, 65, 82, 23]
    thislist.sort(key = myfunc)
    print(thislist)

    #podemos darle la vuelta a una lista
    lista3.reverse()
    print(lista3)
    



def main():
    """
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
    bucleEnListas()
    comprensionDeLista()
    ordenarLista()
    """
    
    
    

main()
