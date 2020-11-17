#Práctica 5 - Ejercicios para realizar con bucles for
#P5E4_sgonzalez
#ESCRIBE UN PRÓGRAMA QUE PIDA UN NÚMERO Y CALCULE SU FACTORIAL.
#DAME UN NÚMERO:  5
#EL FACTORIAL DE 5 ES: 120

numero=int(input("Escribe un número para que calcule su factorial "))    
factorial=1
for i in list(range(1, numero+1)):
    factorial=(factorial*i)
print("El factorial de",numero,"es",factorial)

    



    








