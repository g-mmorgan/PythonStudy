import random
print ("Hola mundo!\n")

def printFun():
    
    print("En python es muy importante la indentacion")

    print("Print es una sentencia"); print('Puedes apilar sentencias así y con comillas simples el str')

    print("Puedes separar el string " \
    "en lineas distintas")

    print("Toda esta frase",end=" "); print("está en diferentes print pero misma linea")

    print("Podemos imprimir muchas cosas en un mismo print, numeros:", 40, "sumas:", 3+4)

    print("También podemos" + "\nusar salto de línea")

def comenatarios():

    print("#Los comentarios van con # no //)")
    print("Los comentarios multilinea no son con /* son con \"\"\" al principio y al final")

    """
    Esto técnicamente no es un comentario
    Es un string pero como no esta dentro de una variable
    Pues python lo ignora
    Y se usa como comentarios de varias lineas
    """


def variables():
    #DECLARACIÓN E INICIALIZACIÓN
    
    #podemos declarar sin indicar el tipo
    print("Podemos declarar sin indicar el tipo")
    var1 = "Hola"   #python asume str
    var2  = 33      #int

    #podemos declarar e inicializar varias a la vez y al mismo valor
    i1 = i2 = i3 = 2
    print("Podemos declarar e inicializar varias a la vez y al mismo valor",i1,i2,i3)

    #Las variables son case sensitive
    print("Las variables son case sensitive")
    var = 23
    Var = 22    #var != Var

    #Tambien podemos asignarles un tipo mediante casting
    var3 = str(3)       # "3"
    var4 = float(3)     # 3.0

    #TIPOS
    x = str("Hello")    #string
    y= int(22)          #entero
    z= float(1e-9)      #float
    b= bool(True)       #booleano
    c= complex(4j)      #complejo
    

    #Podemos obtener el tipo de variable que es
    print("Y podemos ver obtener el tipo de una variable con type(var)")
    print(type(z)) #<class 'float'>

    #tambien tenemos para comprobar si son instacias de tipos
    print("Podemos saber si son instancias de tipos con isinstance(var,tipo)")
    print(isinstance(var1,str)) #True


#VARIABLES GLOBALES
x = "Hola soy una variable global"
y = "Variable global sin modificar"
#si estan definidas fuera de una funcion son globales

def varGlobal():
    
    x = "Variable local"
    print("Se pueden crear variables locales a función con nombres de otra variables", x)
    print("También podemos modificar variables globales desde funcion si usamos global")
    global y
    y = "Nueva variable y"
    print(y)

def varNumericas():

    print("Los numero complejos usan j como la parte imaginaria")
    x = 5j
    y = 3+6j
    z= -5j

    print(type(x),y,z)

    print("Podemos cambiar el tipo de una variable numerica con un cast")
    e = 1    # int
    f = 2.8  # float

    #convert from int to float:
    a = float(e)

    #convert from float to int:
    b = int(f)

    #convert from int to complex:
    c = complex(e)

    print(a,type(a))
    print(b,type(b))
    print(c,type(c))


def numRandom():
    print("Pyhton no tiene una funcion random " \
    " pero podemos importar el modulo random")
    #arribla import random
    print(random.randrange(1,10))


def cadenas():
    #DECLARACIÓN E INICIALIZACION
    txt = "Hola qué tal estas amigo?"
    a = """
            String de varias lineas
            se puede hacer asi
        """
        

    print("\"Podemos usar 'comilla simple' dentro de comillas doble\"")
    
    print("Usamos len para calcular tamaño de string:",len(a))

    #también podemos comprobar si una palabra esta dentro del string
    print("Comprobamos si hola esta en txt con: '\"Hola\" in txt':")
    print("Hola" in txt)

    #comprobamos si no esta
    print("'not in' para comprobar si no esta en la cadena:")
    print("Adios" not in txt)

    #RANGOS DENTRO DE STRING
    b = "Hola Mundo"
    print("Imprimimos un rango dentro de un string: '",b[2:6],"'")

    #no se incluye la ultima posicion 
    #podemos poner de principio hasta una pos o de pos a final
        # print(b[:5]) o print(b[5:])

    #podemos hacer indexacion negativa
    # H O L A Q U E T A  L
    #-x              -2 -1
    #sirve para imprimir el final si no sabemos la longitud del string
    print("Indexación negativa: '",b[-3:],"'")

    print("Podemos cambiar texto a lower o upper case")
    a = "Hola mundo"
    print(a.upper())
    print(a.lower())
    a = "       Hola Mundo       "
    print("'strip()' borra espacios del principio y final:",a,"pasa a:",a.strip())

    print("'replace()' para sustituir dentro de strings")
    a = "A B C D E F G"
    a= a.replace("A","Z")
    print(a)
    a = "28-09-2026"
    print("'a.split('-')', se usa para dividir desde un char concreto")
    print(a,a.split('-'))
    print("Tambien podemos limitar los split", a.split('-',1))


def formatoStr():
    print("Para concatenar str con int de forma sencilla existe el string con formato")
    edad = 22
    print(f"Hola mi edad es {edad}")

    pi = 3.141592
    txt = f"Tengo {edad} años y Pi es {pi:.2f}"
    print(txt)
    #tambien podemos hacer mates directamente
    mates = f"La suma de 3+4 es {4+3}"
    print(mates)

def booleanos():
    #DECLARACIÓN E INICIALIZACIÓN
    a = True
    b = False

    print("En python los booleanos empiezan con mayúsucla: True, False")


    d = 1
    c = 9
    print("En python para comparar booleanos en vez de && o || como en java usamos and y or")
    print("True and True =", a and a)
    print("False or False =", b or b)

    print("Podemos evaulauar cualquier variable con bool(var)")

    #TODAS LAS VARIABLES DEVUELVEN 1
        #excepto:
        #bool(False)
        #bool(None)
        #bool(0)
        #bool("")
        #bool(())
        #bool([])
        #bool({})
    

def listas():

    #DECLARACION E INICIALIZACION
    lista = [1,2,3,"hola",4.5, 5,6]     #normal
    lista2 = list(["a","b","c","d"])    #constructor list()
    lista3 = list((1,2,3,4,5))

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

def tuplas():
    #DECLARACION E INICIALIZACIÓN
    tupla= ("hola","esto","es","una","tupla")
    tupla2= "esto", "tambien", "es", "una", "tupla"
        #Las tuplas son:
            #ORDENADAS
            #NO MODIFICABLES,   no se pueden borrar, añadir o mover elementos
    print(tupla)
    



def main():

    print("Main:\n")
    #printFun()
    #comenatarios()
    #variables()
    #varGlobal()
    #varNumericas()
    #numRandom()
    #cadenas()
    #formatoStr()
    #booleanos()
    #listas()
    #bucleEnListas()
    #comprensionDeLista()
    #ordenarLista()
    

    
    

main()
