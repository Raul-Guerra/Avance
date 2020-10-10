#En la actualidad los bares sufren de problemas de organización de dinero y tiempo, además que cometen actos ilegales sin notarlo, muchas veces se pierde dinero ya que los que lo manejan a la hora de hacer servicio a los clientes se confunden con frecuencia, no lleva una cuenta exacta de estos y al final se pierde dinero o se pone de más. Por otro lado, la mayoría de ellos nunca preguntan si son mayores de edad cuando compran bebidas alcohólicas, lo asumen sin estar consientes que es ilegal venderle bebidas alcohólicas a un menor de edad.
#El proyecto consiste en hacer un sistema de bar, donde contenga algunas funciones como la opción de pago y la elección de bebidas con ciertas restricciones como si eres mayor de edad para así no meter en problemas al dueño del bar, si tienes el dinero, se registrará el dinero pagado y te dirá el cambio que necesites de cada producto comprado y en una próxima función funcionará con un menú de comida donde podrás seleccionar el estilo de la comida que se ponga en este, otra solución que propone es la reducción de personal para gestionar el dinero ya que el cliente podrá utilizar la aplicación para que el bar tender o el recepcionista solo lea y complete la orden indicada en la app.

import time #Para que no se despliegue todo de golpe 
#Función de introducción para un saludo cordial al cliente
def nombrecliente(nombre):
    print("¡Hola"+" "+"%s!"%nombre)
#time to sleep es para que haya un tiempo de espera de despliegue y no se ponga todo de jalón a la hora de ejecutar el programa
    time.sleep(2)
    print("Este es un programa te ayudará a tener un menú de calidad")
    time.sleep(3)


#este código nos muestra que si el usuario escribe cualquier bebida del menú, se le restará el precio asignado al dinero que pagará el cliente 
#esta función la utilizaremos en un futuro para hacer operaciones
def cambio(user1,a):
#agregamos la condicion "(A<12)" porque teniendo en cuenta que el agua es nuestra bebida más barata y cuesta 12 pesos, si no los tiene no le alcanzará para nada    
    if (a<12):
        print("Lo lamentamos, no te alcanza para nada")
    else:
        #el acumulador tiene la función de manter la suma de los gastos del usuario
        acum=0
        #se establece un limite al cual el acumulado no puede sobrepasar
        limite1=a-12
        refresco = 20
        cerveza = 25
        agua = 12
        bebida=0
        while  acum <= limite1:
            if user1 == "refresco" or user1 == "Refresco" :
                acum=acum+refresco
                bebida=bebida+1
        #elif es una condicional que se hace que si no se cumple la primera condición, en este caso (a<12) o refresco se cumplirá la siguiente condicion y asu sucesivamente     
            elif user1 == "cerveza" or user1 == "Cerveza" :
                acum=acum+cerveza
                bebida=bebida+1
            elif user1 == "agua" or user1 == "Agua" :
                acum=acum+agua
                bebida=bebida+1
            print("lleva acumulados:", acum, "pesos")
            sino=str(input("¿Quiere otra bebida? coloque (sí) o (no)"))
            if sino == "Sí" or sino == "Si" or sino == "sí" or sino == "si":
                user1= str(input("Escriba la otra bebida que quiera consumir. (Refresco),(Cerveza),(Agua)"))
            else:
                break
        cambio=a-acum
        print("El total de su compra fue: ",bebida," bebidas y un total de:", acum, " pesos")
        print("Su cambio total es de: ",cambio," pesos") 
def main():
    print("Bienvenido")
    nombre = input("Escribe tu nombre: ")
    nombrecliente(nombre)
    while True:
        print("Elige tu bebida (1-3)")
        #Este es el menú que se le muestra al cliente (en un futuro se le agregarán más bebidas)
        print("Menú:")
        print("1. refreso 20 pesos")
        print("2. cerveza 25 pesos")
        print("3. agua 12 pesos")
        #En ese paso el usuario nos escribirá la bebida que quiere consumir para poder obtener su precio
        user1 = input()
        #El usuario deberá insertar la cantidad de dinero que pagará para que se calcule el cambio que se le devolverá si es el caso
        print("Inserte la cantidad con la que usted va a pagar")
        a = int(input())
        cambio(user1,a)
        #puede hacer este programa varias repeticiones por eso se colocará la opción de repetir con el while true y con una variable conti
        conti=str(input("¿Volver a realizar otra compra?, coloque (sí) (no)?"))
        if conti == "No" or conti == "no" or conti == "N" or conti == "n":
            print("Gracias por su tiempo")
            break
main()
def imprime(matriz):
    for linea in matriz:
        for columna in linea:
            
            print(columna,' ',end="")
        print("\n")
        
print ("Estas bebidas saldrán a la venta proximanmente:")
bebidasnuevas = ["Tequila", "Mojito", "Cuba","Whisky","Mezcal"]
for bebida in bebidasnuevas:
        print(bebida)
print ("Vuelva pronto")

print ("Esta es una sopa de letras por si quieres resolverla")

matriz=[['T','F','M','B','A','R','F','R','J','J','Q','A','S','Q'],['P','U','K','R','L','Z','B','B','V','D','J','S','P','N'],['E','C','M','A','T','N','S','H','O','T','N','A','X','A'],['T','L','N','O','I','Z','U','Q','U','Q','Y','L','O','J'],['B','F','Q','X','E','F','X','B','R','F','R','U','P','B'],['N','O','I','C','C','U','D','O','R','P','E','D','A','P'],['H','Y','L','Y','Z','M','U','T','K','I','B','P','L','U'],['H','K','I','H','R','M','E','G','Z','M','C','X','P','S'],['O','D','A','M','B','P','B','A','F','Q','S','G','I','Z'],['B','L','R','Q','W','C','H','E','L','A','Z','A','O','O'],['A','U','Z','Z','V','R','O','F','H','C','L','J','D','N'],['J','V','Q','B','P','C','Z','X','Y','W','E','O','R','I'],['R','M','A','M','B','I','E','N','T','E','T','L','Ñ','A'],['N','U','B','R','X','G','E','L','A','Q','I','O','J','C']]
print ("Encuentra las siguientes palabras:")
print ("")
print ("- BAR")
print ("- SALUD")
print ("- SHOTS")
print ("- AMBIENTE")
print ("- CHELA")
print ("")
imprime(matriz)


