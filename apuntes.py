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
    print("True y 1 son lo mismo al igual que False y 0")



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

def losArrays():
    print("Los arrays se usan para conteners varios valores en una sola variable")

    coche = ["volvo","audio","seat","bmw","mercedes"]

    print("Se puede acceder a ellos mediante llaves [0]")

    print("De la estructura array salen otros tipos de variables que son: listas, tuplas, sets, dictionaries")
    print("Metodos array:"
    "\nmiArray.append(elemento)   añade elemento al final"
    "\nmiArray.clear()            vacia el array"
    "\nx = miArray.copy()         devuelve una copia del array"
    "\nmiArray.count(elemento)    cuenta cuantas instancias de ese elemento existen en el array"
    "\nmiArray.index(elemento)    devuelve el indice si no esta salta fallo"
    "\nmiArray.extend(otrlista)   añade los elementos de una lista o iterable al final"
    "\nmiArray.insert(i,elemento) añade un elemento en la posicion i"
    "\nmiArray.pop(i)             borra el elemento en la posicion i"
    "\nmiArray.pop                borra el último elemento osea indice mayor"    
    "\nmiArray.remove(elemento)   borra elemento del lista si no esta salta error"
    "\nmiArray.reverse()          invierte el orden de la array"
    "\nmiArray.sort()             ordena de mayor a menor o alfabeticamente")



    

def listas():

    #DECLARACION E INICIALIZACION
    lista = [1,2,3,"hola",4.5,5,6]     #normal
    lista2 = list(["adios","barco","casa","dado","perro","suelo"])    #constructor list() tambien con () en vez de []
    lista3 =list ("hola")               #desde string -> ['h','o','l','a']
    lista4 = list(range(5))             #desde rango ->[1,2,3,4,5]
    lista5 = [x for x in lista2 if "a" in x]    #comprension de lista, construimos a partir de otra
    lista6= lista.copy()                #mediante copia (no son el mismo objeto)
    lista7 = list(lista6)               #con constructor (no son el mismo objeto)
    lista8 = list(lista7[3:])           #con indice de otra lista


    #Las listas son ORDENADAS, MODIFICABLES, PERMITEN DUPLICADOS, SON INDEXADAS

    #METODOS lista
    print("Metodos para Listas:"
    "\nmiLista.append(elemento)     añade elemento al final"
    "\nmiLista.clear()              vacia la lista"
    "\nx = miLista.copy()           devuelve una copia del lista"
    "\nmiLista.count(elemento)      cuenta cuantas instancias de ese elemento existen en la lista"
    "\nmiLista.index(elemento)      devuelve el indice si no esta salta fallo"
    "\nmiLista.extend(otrlista)     añade los elementos de una lista o iterable al final"
    "\nmiLista.insert(i,elemento)   añade un elemento en la posicion i"
    "\nmiLista.pop(i)               borra el elemento en la posicion i"
    "\nmiLista.pop                  borra el último elemento osea indice mayor" 
    "\nmiLista.remove(elemento)     borra elemento del lista"
    "\nmiLista.reverse()            invierte el orden de la lista"
    "\nmiLista.sort()               ordena de mayor a menor o alfabeticamente")




def bucleEnListas():
    #RECORRER UNA LISTA USANDO BUCLES
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

    
def ordenarLista():
    lista1 = [3,43534,1,-76,7,73926780348,-12,21,56,63]
    lista2=["e","c","d","a","b",]
    lista3=[3,"c",1,"b","a",2]

    #sort a secas ordena de forma alfabetica y de menor a mayor
    print("Ordenamos con sort(), se ordena de mayor a menor o alfabeticamente")
    lista1.sort() # solo podemos sort con listas que tengan todos los elementos mismo tipo todo int o todo str
    print(lista1)

    #sort con reverse= true ordena de la Z a A y de mayor a menor
    print("Si ponemos en sort(reverse=true) se ordena al rever de mayor a menor y de Z a A")
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
    tupla= ("hola","esto","es","una","tupla")   #la formas mas común
    tupla2= "esto", "tambien", "es", "una", "tupla" #sin parentesis se puede
    tupla3 = (1,)   #un solo elemento
    tupla4=tuple([1,2,3,4,5])   #constrcutor tuple con lista
    tupla5=tuple("abcdef")      #contructor con string
    tupla6= tuple(range(5))     #con rango


    #Las tuplas son:
        #ORDENADAS, NO MODIFICABLES, SI DUPLICADOS, INDEXADAS
    print(tupla)

    #acceso a tuplas
    print("Se accede a tupla igual que a listas tupla[1], tupla[2:4], tupla[-1], tupla[:3]")

    print("se puede comprobar si contiene elementos con in: \"hola\" in tupla")
    print("hola" in tupla) #True

    print("Las tuplas como tal son inmutables pero si queremos modificarlas las hacemos listas modificamos y las volvemos a hacer tuplas")
    x = ("apple", "banana", "cherry")
    y = list(x)
    y[1] = "kiwi"
    x = tuple(y)

    print(x)

    print("Tambien podemos sumar tuplas de tal forma que se añaden elementos")

    z=tuple(range(5))
    w= ("naranja",)
    z +=w
    print(z)

    print("Podemos desempaquetar tuplas cada elemento de la tupla lo extraemos a una variable")

    t=tuple("abc")
    (a,b,c) = t
    print(f"Tupla:{t}, t[1]:{a} t[2]:{b} t[3]:{c}")

    print("Si tenemos menos variables que elementos con * la última variable se convierte en lista con el resto")
    t1=tuple(range(10))
    (n,n1,n2,*m)=t1
    print("t1=tuple(range(10))")
    print(f"n:{n} n1:{n1} n2:{n2} m:{m}")

    print("Podemos duplicar tuplas")
    t3=tuple("abcd")
    t4 = t3 * 3
    print(t4) #('a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b', 'c', 'd')

    #METODOS
        #METODOS lista
    print("Metodos para Tuplas:"
    "\nmiTupla.count(elemento)    cuenta cuantas instancias de ese elemento existen en la tupla"
    "\nmiTupla.index(elemento)    devuelve el indice si no esta salta fallo"
    )

def losSets():

    #DECLARACIÓN E INICIALIZACIÓN


    #LOS SETS SON:
        #DESORDENADOS, SIN DUPLICADOS, MODIFICABLES, NO INDEXADOS
    miSet={"hola","los","sets","van","con","corchetes"}    #normal con llaves
    set1 = set([1, 2, 3, 4])  #constructor con lista
    set2 = set((1, 2, 3))     #constructor con tupla
    set3 = set("hola")        #constructor con str
    set4 = set(range(5))      #constructor con range
    set5 = {x for x in range(10)} #por comprension

 
    
    print("Metodos para Sets:"
        "\nmiSet.add(elemento)          cuenta cuantas instancias de ese elemento existen en la tupla"
        "\nmiSet.update(elemento)       añade cualquier iterable al set"
        "\nmiSet.remove(elemento)       borra el elemento del set"
        "\nmiSet.discard(elemento)      borra el elemento del set pero si no existe no salta error como en remove"
        "\nmiSet.clear()                vacia el set"
        )

    print("Con los set podemos hacer uniones")

   #UNION
    miSet= set1.union(set2)    #mantiene todos los elementos evitando duplicar datos
    print (miSet)
    miSet = set1 | set2        #Con | solo podemos unir sets entre sets no con otros data types 
    set1.update(set2)          #se parece mucho a la union además evita duplicados

    #INTERSECCION
    miSet  = set4.intersection(set2)    #mantiene solo comunes
    print(miSet)
    mi_set = {1, 2} & {2, 3}            #con opderador, solo con sets
    miSet.intersection_update(set3)     #mantiene el original sin crear nuevo set

    #DIFERENCIA 
    miSet = set4.difference(set5)       #mantiene solo los distintos
    mi_set = {1, 2, 3} - {2}            #operador
    
    mi_set = {1, 2} ^ {2, 3}        # {1, 3}
    

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
    #loslistas()
    #listas()
    #bucleEnListas()
    #comprensionDeLista()
    #ordenarLista()
    #tuplas()
    losSets()

    #cambio sin mas

    
main()
