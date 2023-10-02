'''
- a) Definir una función, denominada “mas_breves”, que reciba como parámetros una cadena (cad) de
caracteres y una tupla (tup) integrada por cadenas de caracteres, y devuelva como resultado una cadena
compuesta con la concatenación de las cadenas de la tupla tup cuya longitud sea inferior a la de la cadena
cad. [No es necesario validar los datos]
Ejemplo: Dados la cadena ” empleo”
y la tupla ('ver','cerveza','artesanal','tambien','piloto','de','drones')
la función debería devolver la cadena ”verde”
//////////////////
b) Definir una función main() que pruebe el funcionamiento de mas_breves () con los datos del ejemplo.
//////////////////
2- Escribir un programa que le pida al usuario que ingrese (de “uno por vez”) una serie de números enteros
positivos, hasta que ingrese el valor -1 como condición de salida. El programa deberá totalizar la suma de
esos números (excluido el “centinela”), calcular el valor máximo ingresado y generar una lista sin repeticiones,
integrada por los distintos números que fueron ingresados en la serie. Incluir instrucciones que permitan ver
la evolución de los cambios de estado de la lista. Finalmente, deberá mostrar en pantalla, con descripciones
expresivas, la suma, el máximo y el contenido de la lista. [No es necesario validar los datos]
Ejemplo: Si el usuario ingresó los números 10 , 30 , 20 , 40 , 10 , 40 , 25 , 25 , 40 , 40 , -1
el programa debe obtener la suma: 280 , el máximo: 40 y generar la lista: [ 10 , 30 , 20 , 40, 25 ]
/////////////////
3- Definir una función, denominada “actualiza_prec”, que reciba como parámetros un diccionario (con artículos
como clave y su respectivo precio como valor) y una lista de tuplas (de dos componentes cada una, la primera
representa un artículo y la segunda su nuevo precio), y devuelva como resultado una lista con las tuplas cuya
actualización en el diccionario fracase. La función deberá modificar el diccionario con los precios actualizados.
[No es necesario validar los datos]
Ejemplo: Dados la lista [ ("oj", 300), ("kmisa", 700), ("kfe", 130), ("t", 20) ]
y el diccionario {'kmisa': 500, 'oj': 250, 'pan': 60, 't': 18}
la función debería actualizar el diccionario de modo que quede
{'kmisa': 700, 'oj': 300, 'pan': 60, 't': 20}
y devolver la lista [('kfe', 130)]
/////////////
4- Comente la principal diferencia entre los “ciclos definidos” y los “indefinidos”. Describa sucintamente en qué
se diferencian un “ciclo interactivo” y un “ciclo con centinel
'''
'''
def mas_breves(cad, tup):
    palabras_mas_breves =''
    for i in tup:
        if len(i) < len(cad):
            palabras_mas_breves+=i
    
    return palabras_mas_breves

def main():
    cad = "empleo"
    tup = ('ver', 'cerveza', 'artesanal', 'tambien', 'piloto', 'de', 'drones')
    mas_breves(cad, tup)
main() 
'''
'''
resultado=0
lista=[]
centinela=0
while centinela!=-1:
    centinela=int(input("para dejar de ingresar numeros escriba -1 para continuar precione cualquier digito"))
    lista.append((centinela))
    print(set(lista))
for i in range(len(lista)):
    if lista[i]==max(lista):
        print("nro mayor de la lista",lista[i])
    
    elif lista[i]<0:
        lista[i]=0        
    resultado+=lista[i]
print("resultado",resultado)
print("lista comleta",set(lista))
'''        
'''
 3- Definir una función, denominada “actualiza_prec”, que reciba como parámetros un diccionario 
 y una lista de tuplas 
, y devuelva como resultado una lista con las tuplas cuya
actualización en el diccionario fracase. La función deberá modificar el diccionario con los precios actualizados.
[No es necesario validar los datos]
Ejemplo: Dados la lista [ ("oj", 300), ("kmisa", 700), ("kfe", 130), ("t", 20) ]
y el diccionario {'kmisa': 500, 'oj': 250, 'pan': 60, 't': 18}
la función debería actualizar el diccionario de modo que quede
{'kmisa': 700, 'oj': 300, 'pan': 60, 't': 20}
y devolver la lista [('kfe', 130)]   

'''
'''
def actualiza_precio(dicc,listup):
    lista=[]
    for i in (listup):
        producto,precio=i
        if i not in dicc:
            lista.append(i)
        else:
            dicc[producto]=precio
        
        
        
    
        

def main():
    dicc={'kmisa': 500, 'oj': 250, 'pan': 60, 't': 18}
    listup=[ ("oj", 300), ("kmisa", 700), ("kfe", 130), ("t", 20) ]
    
main()
'''