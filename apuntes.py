"""
 Esto técnicamente no es un comentario
 Es un string pero como no esta dentro de una variable
 Pues python lo ignora
 Y se usa como comentarios de varias lineas
 """

print ("Hola mundo")

#Los comentarios van con # no //

if 2>1:
 print("En python es muy importante la indentacion")

 print("Print es una sentencia"); print('Puedes apilar sentencias así, también usar comilla simple')

 print("Toda esta frase",end=" "); print("está en diferentes print pero misma linea")

 print("Podemos imprimir numeros", 4092380, "\nY sumas", 3+4)

"""                _       _     _           
                 (_)     | |   | |          
 __   ____ _ _ __ _  __ _| |__ | | ___  ___ 
 \ \ / / _` | '__| |/ _` | '_ \| |/ _ \/ __|
  \ V / (_| | |  | | (_| | |_) | |  __/\__ \
   \_/ \__,_|_|  |_|\__,_|_.__/|_|\___||___/
                                            
"""

#Podemos declarar variables sin tipos

var1 = "Hola"
var2  = 33
#Tambien podemos asignarles un tipo mediante casting

var3 = str(3)       # "3"
var4= int(3)        # 3
var5 = float(3)     # 3.0

#Podemos obtener el tipo de variable que es
var6 = type(var5)
print(var6) #<class 'float'>

"""
varibles son case-sensitive
var = 23
Var = 22
NOMBRES

    Tiene que empezar o por letra o por barra baja
    No puede empezar por numero, solo puede contener letras numeros y barra baja
        var Var _myVar ...
"""

i1 = i2 = i3 = 2
print("Podemos declarar e incializar variables a la vez y al mismo valor",i1,i2,i3)

#luego vamos con listas y desenpquetado

lista = [1,2,3]
l1,l2,l3 = lista
print(l1,l2,l3); print(lista)