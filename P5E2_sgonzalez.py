#Práctica 5 - Ejercicios para realizar con bucles for
#P5E2_sgonzalez
#ESCRIBE UN PROGRAMA QUE PIDA DOS NÚMEROS Y ESCRIBA QUÉ NÚMEROS ENTRE 
#ESE PAR DE NÚMEROS SON PARES Y CUÁLES IMPARES

print ("Escriba dos números y le indicaré qué números pares e impares se encuentran entre ellos dos")
a=int(input("Escriba el primer número "))
b=int(input("Escriba el segundo número "))
for i in list(range(a, b+1)):
    if (i%2==0):
        print ("El número", i, "es par")
    else:
        print ("El número", i, "es impar")
    








