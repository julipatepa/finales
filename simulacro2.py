'''
1- Definir una función, denominada “verifica_arroba”, que reciba como parámetro una cadena de caracteres,
que representa una supuesta dirección de correo electrónico, y devuelva como resultado un valor booleano
que indique si la cadena, cumple el siguiente criterio de validación: que contenga un único carácter “@” y que
esté en una posición que no sea la primera de la cadena, ni la última. [No es necesario validar más datos]
Ejemplos: Dadas las cadenas la función debería devolver el valor
 “informatica@undav.edu.ar” True
“informática.undav.edu.ar” False
“@informática.undav.edu.ar” False
“informática@undav@edu.ar” False
“informática.undav.edu.ar@” False
2- Escribir un programa que pida al usuario que ingrese (“uno por vez”) datos de entradas de teatro vendidas,
hasta ingresar el valor 0 (cero) como condición de finalización. Los datos son: número de fila, número de
asiento y una letra que representa su precio (“V”: $800, “P”: $500, “C”: $300). El programa debe mostrar los
datos de cada entrada (ubicación y precio) y acumular la suma de importes. Además deberá actualizar un
diccionario que contenga como clave cada número de fila ingresado, y como valor, la cantidad respectiva de
asientos vendidos. Finalmente, deberá mostrar, con descripciones expresivas, la suma total de importes y el
contenido del diccionario, presentando cada ítem en una línea distinta. [No es necesario validar los datos]
Ejemplo: Si el usuario ingresó 3, 3, ’V’/ 3, 4, ‘V’/ 22, 5, ‘C’/ 8, 6, ‘P’/ 22, 4, ‘C’/ 0
el programa debe calcular el total: $ 2.700 y generar el diccionario: { 8 : 1 , 3 : 2 , 22 : 2 }
3- a) Definir una función, denominada “valida_butaca”, que reciba como parámetros una tupla de la forma
(nro_fila, nro_asiento) y una lista de tuplas de la misma forma, sin repeticiones. La función debe remover la
tupla (nro_fila, nro_asiento) de la lista, si es que existía previamente, y debe devolver un resultado booleano
que indique si fue quitada exitosamente, o no, de la lista. [No es necesario validar más datos]
Ejemplo: Dada la lista [ (3,3),(3,4),(3,7),(8,3),(8,7),(22,4),(22,5) ]
 - si la tupla fuera (2,10) la función debería devolver el valor False
 - si la tupla fuera (3,4) la función debería devolver el valor True
 y la lista debiera quedar así: [ (3,3),(3,7),(8,3),(8,7),(22,4),(22,5) ]
b) Definir una función main() que pruebe el funcionamiento de valida_butaca () con datos de ejemplo.
4- ¿Qué entiende por secuencias “inmutables” y “mutables” en el lenguaje Python? ¿Cuáles son inmutables?
Ejemplifique sobre los ejercicios anteriores
'''
'''
def verifica_arroba(cadena):
    contador=0
    for i in range(len(cadena)):
        if cadena[i]=='@':
            contador+=1
        elif contador>1:
            return False
    if contador==1 and cadena[0]!='@' and cadena[-1]!='@':
        return True
    else:
        return False        
   
        
        
def main():
    cadena='informatica@undav.edu.ar'
    cadena1='@informática.undav.edu.ar'
    cadena2='informática.undav.edu.ar'
    cadena3='informática.undav.edu.ar@'
    cadena4='informática@undav@edu.ar'
    print(verifica_arroba(cadena))
    print(verifica_arroba(cadena1))
    print(verifica_arroba(cadena2))
    print(verifica_arroba(cadena3))
    print(verifica_arroba(cadena4))


main()            
'''            
'''
2- Escribir un programa que pida al usuario que ingrese (“uno por vez”) datos de entradas de teatro vendidas,
hasta ingresar el valor 0 (cero) como condición de finalización. Los datos son: número de fila, número de
asiento y una letra que representa su precio (“V”: $800, “P”: $500, “C”: $300). El programa debe mostrar los
datos de cada entrada (ubicación y precio) y acumular la suma de importes. Además deberá actualizar un
diccionario que contenga como clave cada número de fila ingresado, y como valor, la cantidad respectiva de
asientos vendidos. Finalmente, deberá mostrar, con descripciones expresivas, la suma total de importes y el
contenido del diccionario, presentando cada ítem en una línea distinta. [No es necesario validar los datos]
Ejemplo: Si el usuario ingresó 3, 3, ’V’/ 3, 4, ‘V’/ 22, 5, ‘C’/ 8, 6, ‘P’/ 22, 4, ‘C’/ 0
el programa debe calcular el total: $ 2.700 y generar el diccionario: { 8 : 1 , 3 : 2 , 22 : 2 }

'''
'''
venta_de_asientos={}
acum=0
centinela=True
while centinela==True:
    num_asiento=int(input(' numero de asiento  '))
    num_fila=int(input('ingrese numero de fila'))
    letra_precio=str(input('ingrese letra del precio'))
    
    if letra_precio == 'v':
        precio = 800
        
    elif letra_precio == 'p':
        precio = 500
        
    elif letra_precio == 'c':
        precio = 300   
    centinela=int(input('para ternminar ingrese el nro 0 '))
    if centinela==0:
        centinela=False
    acum+=precio
    if num_fila in venta_de_asientos:
        venta_de_asientos[num_fila]+=1
    else:
        venta_de_asientos[num_fila]=1
    for i in(venta_de_asientos):
        ventas=venta_de_asientos[i]
    print((venta_de_asientos))   
    print('el precio es: ',acum)                         
    '''  
    
'''
    3- a) Definir una función, denominada “valida_butaca”, que reciba como parámetros una tupla de la forma
(nro_fila, nro_asiento) y una lista de tuplas de la misma forma, sin repeticiones. La función debe remover la
tupla (nro_fila, nro_asiento) de la lista, si es que existía previamente, y debe devolver un resultado booleano
que indique si fue quitada exitosamente, o no, de la lista. [No es necesario validar más datos]
Ejemplo: Dada la lista [ (3,3),(3,4),(3,7),(8,3),(8,7),(22,4),(22,5) ]
 - si la tupla fuera (2,10) la función debería devolver el valor False
 - si la tupla fuera (3,4) la función debería devolver el valor True
 y la lista debiera quedar así: [ (3,3),(3,7),(8,3),(8,7),(22,4),(22,5) ]
b) Definir una función main() que pruebe el funcionamiento de valida_butaca () con datos de ejemplo.

''' 
lista=[]
def valida_butaca(nro_fila, nro_asiento,tupla):
    for i in (tupla):
        if  (nro_asiento,nro_fila)==i:
            tupla.remove(i)
            (lista.append(tupla)) 
            print(lista)
            return True
            
        else:
            print (tupla)
            return False    
            
        
def main():
    nro_fila=int(input('ingrese nro de fila'))
    nro_asiento=int(input('ingrese nro de asiento'))
    tupla= [ (3,3),(3,4),(3,7),(8,3),(8,7),(22,4),(22,5) ]
    valida_butaca(nro_fila,nro_asiento,tupla)  
main()    
            
    
            
   
        
    
   
    
    
            