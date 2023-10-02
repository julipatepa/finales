'''
a) Definir y documentar una función, denominada “posible_ipv4”, que reciba como parámetro una cadena de
caracteres integrada por números y puntos, que debe ser validada. Debe devolver como resultado un valor
booleano que indique si es, o no, una posible dirección IP. El criterio de validez es que contenga exactamente
tres puntos, que ninguno de éstos esté en la primera ni en la última posición de la cadena de caracteres, y que
el resto de los caracteres sean dígitos decimales, en una cantidad total que no supere los 12 caracteres ni sea
inferior a 4 caracteres numéricos.
Ejemplos: Si la cadena de caracteres fuera “255.255.255.255”, la función debería devolver True
Si la cadena de caracteres fuera “0.0.0.0”, la función debería devolver True
Si la cadena de caracteres fuera “1.2.34.”, la función debería devolver False
Si la cadena de caracteres fuera “.1.2.34”, la función debería devolver False
Si la cadena de caracteres fuera “1..2.3”, la función debería devolver False
Si la cadena de caracteres fuera “123.4567.890.123”, la función debería devolver False
Si la cadena de caracteres fuera “”, la función debería devolver False
b) Definir una función pba() que pruebe el funcionamiento de posible_ipv4() con los datos de ejemplo.
2- Escribir un programa que le pida al usuario que ingrese (de “una por vez”) una serie de cadenas de caracteres,
preguntando a cada paso si desea ingresar más cadenas. Con cada cadena que haya ingresado, debe invocar a
la función posible_ipv4(), para verificar que sea una posible dirección IP, exigiendo el reingreso las veces que
sea necesario hasta que sea una cadena válida. Las cadenas válidas deben agregarse en una lista sin repetirlas.
Finalmente, debe mostrar en pantalla, con descripciones expresivas, la cantidad de cadenas de caracteres "no
válidas" ingresadas, la cantidad de repeticiones de cadenas válidas y el detalle, una debajo de otra, de las
cadenas de caracteres válidas ingresadas, sin repetición.
Ejemplo:
Si el usuario ingresó las cadenas: “1.2.34.” “1.2.3.4” “0.0.0.0” “.1.2.34” “1.2.3.4”
“1..2.3” “0” “1.2.3.4” “255.255.255.255” y “2.2.2.2”
el programa deberá mostrar que la cantidad de cadenas de caracteres “no válidas” fue: 4,
que la cantidad de posibles direcciones IP repetidas ingresadas fue: 2,
y, una debajo de otra, las siguientes cadenas de caracteres:
“1.2.3.4”
“0.0.0.0”
“255.255.255.255”
“2.2.2.2”
'''

'''
a) Definir y documentar una función, denominada “posible_ipv4”, que reciba como parámetro una cadena de
caracteres integrada por números y puntos, que debe ser validada. Debe devolver como resultado un valor
booleano que indique si es, o no, una posible dirección IP. El criterio de validez es que contenga exactamente
tres puntos, que ninguno de éstos esté en la primera ni en la última posición de la cadena de caracteres, y que
el resto de los caracteres sean dígitos decimales, en una cantidad total que no supere los 12 caracteres ni sea
inferior a 4 caracteres numéricos.
Ejemplos: Si la cadena de caracteres fuera “255.255.255.255”, la función debería devolver True
Si la cadena de caracteres fuera “0.0.0.0”, la función debería devolver True
Si la cadena de caracteres fuera “1.2.34.”, la función debería devolver False
Si la cadena de caracteres fuera “.1.2.34”, la función debería devolver False
Si la cadena de caracteres fuera “1..2.3”, la función debería devolver False
Si la cadena de caracteres fuera “123.4567.890.123”, la función debería devolver False
Si la cadena de caracteres fuera “”, la función debería devolver False
'''

'''
def posible_ipv4(cadena):
    acumulador=0
    for i in range(len(cadena)):
        
        if cadena[i]=='.':
            acumulador+=1
    if acumulador>3 or cadena[-1]=='.' or cadena[0]=='.' or len(cadena)>15 or cadena[1]=='.' and cadena[2]=='.':
        print(False)
            
    else:
        print(True)
            

def main():
    #a='255.255.255.255'
    #a='0.0.0.0'
    #a='1.2.34.'
    #a='1..2.3'
    a='123.4567.890.123'
    posible_ipv4(a)
main()            
'''