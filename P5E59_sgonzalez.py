#Práctica 5 - Ejercicios para realizar con bucles for
#P5E9_sgonzalez
# Escribe un programa que pida la anchura de un rectángulo y lo dibuje
# de la siguiente manera: anchura: 5 altura: 4
#*****
#*   *
#*   *
#*****


ancho=int(input("Introduce el ancho del rectángulo "))
alto=int(input("Introduce el alto del rectángulo "))
PX="*"

for i in range(alto):
    if (i==0)or(i==alto-1):
        print(PX*ancho)
        print (" ")
    else:
        print(PX+((ancho-2)*" ")+PX)  
        print (" ")  






   
     
    


    



    








