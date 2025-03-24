import random

numero_secreto = random.randint(1,101)
adivinado = False
intentos = 0
intentos_maximos = 5

print("INICIO: Adivina el numero secreto")

while not adivinado:
    if intentos >= intentos_maximos:
        print("Perdiste")
        break
    
    numero_user = int(input(f"Tenes {intentos_maximos - intentos} intentos \nIngrese un numero del 1 al 100:"))
    intentos += 1

    if numero_user == numero_secreto:
        print("¡Felicitaciones! Adivinaste el numero")
        adivinado = True
    elif numero_user < numero_secreto:
        print("El numero secreto es mayor al ingresado")
    else:
        print("El numero secreto es menor al ingresado")
    


