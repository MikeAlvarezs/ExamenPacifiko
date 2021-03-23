# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 17:28:12 2021

@author: Mike

Miguel Alvarez 
Pacifiko recruitment test
Ejercicio 3 
"""
import math # Libreria para uso de funciones matematicas

# Ejercicio 3a
def checkPrime(n): 
    raiz = math.sqrt(n) # Se obtiene la raiz cuadrada de n
    raizUp = math.ceil(raiz) # Se aproxima la raiz al entero mas alto
    
    for i in range(2, raizUp+1): # Se divide n entre todos los enteros entre 
                                 # 2 y la raiz rondeada de n   
        if(n % i == 0): # Si el modulo de n/i es igual a cero
            print(n, "no es primo") # El numero no es primo
            break # Dejamos de dividir 
    else: # Si ninguna de los modulos es 0
        print(n, "es primo") # El numero es primo
        
        
# Ejercicio 3b 
def sumCon(N):
    suma = 0 # Variable para almacenar la suma de numeros consecutivos
    i = 0 # Variable a aumentar 
    for i in range(N+1): 
        suma += i # Se agrega a suma el numero consecutivo hasta N+1 (tomandolo en cuenta)
    
    print("Respuesta: ", suma) # Se muestra el resultado en la consola
        
        
        
        