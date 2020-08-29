#En la actualidad los bares sufren de problemas de organización de dinero y tiempo, además que cometen actos ilegales sin notarlo, muchas veces se pierde dinero ya que los que lo manejan a la hora de hacer servicio a los clientes se confunden con frecuencia, no lleva una cuenta exacta de estos y al final se pierde dinero o se pone de más. Por otro lado, la mayoría de ellos nunca preguntan si son mayores de edad cuando compran bebidas alcohólicas, lo asumen sin estar consientes que es ilegal venderle bebidas alcohólicas a un menor de edad.
#El proyecto consiste en hacer un sistema de bar, donde contenga algunas funciones como la opción de pago y la elección de bebidas con ciertas restricciones como si eres mayor de edad para así no meter en problemas al dueño del bar, si tienes el dinero, se registrará el dinero pagado y te dirá el cambio que necesites de cada producto comprado y en una próxima función funcionará con un menú de comida donde podrás seleccionar el estilo de la comida que se ponga en este, otra solución que propone es la reducción de personal para gestionar el dinero ya que el cliente podrá utilizar la aplicación para que el bar tender o el recepcionista solo lea y complete la orden indicada en la app.

print("Elige tu bebida")
#Este es el menú que se le muestra al cliente (en un futuro se le agregarán más bebidas)
print("Menú:")
print("refreso 20 pesos")
print("cerveza 25 pesos")
print("agua 12 pesos")
#Aqui determinamos el valor de las bebidas
refresco = 20
cerveza = 25
agua = 12
#En ese paso el usuario nos escribirá la bebida que quiere consumir para poder obtener su precio
user1 = input()
#El usuario deberá insertar la cantidad de dinero que pagará para que se calcule el cambio que se le devolverá si es el caso
print("Inserte la cantidad con la que usted va a pagar")


a = int(input())
#este código nos muestra que si el usuario escribe cualquier bebida del menú, se le restará el precio asignado al dinero que pagará el cliente 
#agregamos la condicion "(A<12)" porque teniendo en cuenta que el agua es nuestra bebida más barata y cuesta 12 pesos, si no los tiene no le alcanzará para nada
if (a<12):
        print("no te alcanza para nada")
        
elif (user1 == "refresco"):
    print("tu cambio es")
    print (a-refresco)
    
elif (user1 == "cerveza"):
    print("tu cambio es")
    print (a-cerveza)
    
elif (user1 == "agua"):
    print("tu cambio es")
    print (a-agua)
    

