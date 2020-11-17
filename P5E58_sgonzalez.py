#Práctica 5 - Ejercicios para realizar con bucles for
#P5E8_sgonzalez
# Escribe un programa que pida la anchura de un triángulo y lo dibuje 
# de la siguiente manera: Altura: 4
#*
#**
#***
#****
#***
#**
#*

altura=int(input("Introduce la altura del triángulo "))
PX="*"

for i in list(range(altura)):
    print ((i)*PX)
    print (" ")

for i in list(range(altura,0,-1)):
    print ((i)*PX)
    print (" ")






   
     
    


    



    








