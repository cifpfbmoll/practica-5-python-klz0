#Práctica 5 - Ejercicios para realizar con bucles for
#P5E3_sgonzalez
# Escribe un programa que pida dos números y escriba la suma de enteros
# desde el primero hasta el último.

numero1=int(input("Dame un número "))
numero2=(int(input("Dame otro número mayor que %d " %(numero1))))

suma=0

for i in range (numero1,numero2+1):
    #print (i+suma) visualmente prefiero no imprimir los valores obtenidos en cada suma
    suma=(i+suma)
print ("La suma de todos los números comprendidos entre %d y %d es de %d" %(numero1,numero2,suma))    


   
     
    


    



    








