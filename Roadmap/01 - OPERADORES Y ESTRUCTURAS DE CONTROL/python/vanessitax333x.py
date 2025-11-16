"""
Operadores

"""

#Operadores Aritméticos y distintas formas de emplearlos

print(f"Suma: 10 + 3 = {10 + 3}")
print()

print("Resta")
print(10 - 3)
print()

multiplicacion=10*3
print(multiplicacion)
print()

numero1=12
numero2=3
print(f"División: 12 / 3 = {numero1 / numero2}")
print()

print(f"Exponente: 10 ** 3 = {10 ** 3}")
print()

print(f"Módulo: {10 % 3}")                              #Restante de la División
print()

print(f"División Entera: {10 // 3}")
print()





#Operadores de Comparación 


print(f"Igualdad   1 == 3: {10 == 3}")
print()

print(f"Desigualdad   10 != 3: {10 != 3}")
print()

print(f"Mayor que   10 > 3: {10 > 3}")
print()


print(f"Menor que   10 < 3: {10 < 3}")
print()


print(f"Mayor o igual que   10 >= 3: {10 >= 3}")
print()


print(f"Menor o igual que   10 <= 3: {10 <= 3}")
print()






#Operadores Lógicos 





print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4: {10 + 3 == 13 and 5 - 1 == 4}")  #Ejemplo AND donde se requiere que se cumplan ambas condicieones para que se indique que es verdadero
print()

print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 4: {10 + 3 == 13 or 5 - 1 == 4}")   #Ejemplo OR donde indíca que es True, esto porque ambas condiciones se cumplen
print()


print(f"OR ||: 10 + 4 == 13 or 5 - 2 == 4: {10 + 4 == 13 or 5 - 2 == 4}")   #Ejemplo OR donde indíca que es False, esto porque ninguna de las condiciones se cumple
print()

print(f"NOT !: not 10 + 3 == 14:  {not 10 + 3 == 14}")    # Ejemplo NOT donde al no cumplirse la condición indica que es False, pero con el operador NOT, niega esa Operación pasando a ser True






#Operadores de Asignación 





my_number = 11           #Asignación
print(my_number)

my_number += 11           #Suma y Asignación
print(my_number)

my_number -= 2           #Resta y Asignación
print(my_number)

my_number *= 5           #Multiplicación y Asignación
print(my_number)

my_number /= 2           #División y Asignación
print(my_number)


my_number %= 4           #Módulo y Asignación
print(my_number)


my_number **= 6           #Exponente y Asignación
print(my_number)


my_number //= 2           #División Entera y Asignación                            #La variable my_number comenzó con 11, pero se modifica su valor conforme vamos avanzando
print(my_number)






#Operadores de Identidad




print(my_number)
my_new_number = 32.0
print(f"my_new_number is my_new_number es: {my_new_number is my_number}")       #A pesar de que el el valor a comparar sea aparentemente el mismo, indíca False 
                                                                                #porque la identidad o lo que intentan comparar es su valor en memoria, es decir
                                                                                #my_new_number ocupa una direción de memoria completamente diferente a my_number
                                                                                #

my_number = my_new_number
print(f"my_new_number is my_new_number es: {my_new_number is my_number}")       #En este ejemplo lo que hicimos es cambiar el valor el memoria de ambos al mismo
                                                                                #por lo que ahora indica que es True 
                                                                                
                                                                                
print(f"my_new_number is not my_new_number es: {my_new_number is not my_number}")  #Aqui indica que es False porque ya indicaba que era True, lo que hicimos fue
                                                                                    #negarla por lo que paso a ser False 
                                                                                    





#Operadores de Pertenencia (Si algo, pertenece a algo)




print(f"'u' in 'moure' = {'u' in 'moure'}")        #Comprueba que realmente el elemento A se encuentre dentro del elemento B

print(f"'b' not in 'moure' = {'b' not in 'moure'}")  #Comprueba que realmente el elemento A no se encuentre dentro del elemento B





#Operadores de Bit 



a = 10   #1010 \
#               \
#                0010                 #Da ese resultado porque se comparan cada dígito en orden de ambas cifras, es decir: Primer dígito de la cifra superior
#               /                     #con el Primer Dígito de la cifra inferior y así sucesivamente, todo esto basandonos en los Operadores Lógicos
b = 3    #0011 /

print(f"AND: 10 & 3 = {10 & 3}")   #0010      #Se determina que es el 2 porque "0010" es 2 en Binario

print(f"OR: 10 | 3 = {10 | 3}")    #1011      #Se determina que es el 11 porque "1011" es 11 en Binario

print(f"XOR: 10 ^ 3 = {10 ^ 3}")   #1001      #Se determina que es el 9 porque "1001" es 9 en Binario
#En este caso con XOR si los bits son diferentes el resultado es 1, caso contrario, si son iguales será 0

print(f"NOT: 10 ~ 3 = {~10}")
#En este caso con NOT, lo que esta haciendo es invertir el valor bit a bit sobre la representación del 10, por ello arroja -11, va negando bit a bit 

print(f"Desplazamiento a la Derecha: 10 >> 2 = {10 >> 2}") #0010
#En este caso se comienzan a desplazar los bits del valor del 10 binario (1010), por lo que quedaría "0101" en caso fuera desplazamiento 1 bit, como son 
#dos bits resultaría "0010"  esto porque se empieza a cubrir con ceros según la dirección a la que se dezplacen los bits 

print(f"Desplazamiento a la Izquierda: 10 << 2 = {10 << 3}") #101000









#Operadores de Control



                                    #CONDICIONALES

my_string = "Brais"
if my_string == "MoureDev":
    print("my_string es 'MoureDev'")                  #En este caso no se imprime my_string es MoureDev porque no se cumple esta condición
elif my_string == "Brais":
    print("my_string es 'Brais'")                     #Se imprime my_string es Brais porque si se cumple con esta condición
else:
    print("my_string no es 'MoureDev' ni 'Brais'")    #En caso no se cumpla ninguna condición se imprimiría este resultado


                                    #ESTRUCTURAS ITERATIVAS

for i in range(11):                                                 #La estructura iterativa for sirve para crear bucles
    print(i)                                                        #sirve para recorrer estructuras que tienen mas de un elemento o para 
                                                                    #ejecutar una acción varias veces 
                                                                    
                                                                    #Rango es una estructura donde se van a meter todos los números desde el 0 
                                                                    #(ó desde el numero que querramos que comience) hasta el
                                                                    #número que se le indique sin tener en cuenta el número colocado, es decir
                                                                    #si se coloca 14, llegará hasta el 13
                                                                    

#for (estructura que se acabará recorriendo)    y while(Lo que se intenta plantearle es una condición para que el bucle se ejecute mientras esa condición sea verdadera)
#   i = índice

i=0
while i <= 10:                  #En este caso es un Bucle Infinito porque el valor de i siempre será cero y la condición es que el bucle "while"
    print(i)                    #se ejecute mientras el valor de 'i' siga siendo cero
    
    i+=1                        #Aquí se le coloca el suma o asignación con el uno y gracias a eso, cada vez que se ejecute el bucle while se le sumará 1 y
                                #se le asignará el nuevo valor, esto hasta el momento en el que se cumpla la condición se saldrá del bucle y se detendrá




                            #MANEJO DE EXCEPCIONES



try:                                                #El operador Try es como pedir que se intente ejecutar cierto código en específico, pero en caso 
    print(10/0)                                     #de que falle se le coloca un 'except' o excepción para que el programa no se rompa 
except:
    print("Se ha producido un Error")   
finally:                                            #El finally es la última instrucción que se va a ejecutar siempre que finalice el manejo de error, se
    print("Ha finalizado el manejo de Excepciones") #produzca error o no se produzca error




"""
EXTRA
"""


for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
                                            
        print(number)                       #Se coloca el if porque se quiere controlar el flujo, a continuación por medio de una definición matemática
                                            #se sabe que un número es par, si al hallar el módulo de 2 de ese número, el resultado es cero
                                            #es decir, que esa división entera, el resto es cero, aunado a ello se coloca el and porque requerimos comprobar 
                                            #o cumplir con otra condición que es que no aparezca el 16 como se nos indicó, por lo que le agregamos el 
                                            #and para pedirle que sea distinto (!=) a 16. Acto seguido agregamos otro and debido a que tenemos otra condición
                                            #que cumplir, que es que no aparezcan los múltiplos de 3, esto se consigue por medio del módulo
                                            #(si el módulo '%' de 3 != 0) veremos que se cumple la condición
        
