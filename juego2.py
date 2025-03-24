#-----------------------------------# 
# Juego: Piedra, papel o tijera

print("Bienvenidos al clasico \"Piedra, papel o tijera\"")
nombre1 = input("Ingrese el nombre del jugador 1: ").capitalize()
nombre2 = input("Ingrese el nombre del jugador 2: ").capitalize()

puntos_jugador1 = 0
puntos_jugador2 = 0
turno = 1



while turno <= 3:
    print("Turno", turno)
    jugador1 = input(f"{nombre1} elige: ¿Piedra, papel o tijera? ").lower()
    jugador2 = input(f"Ahora {nombre2}. Elige: ¿Piedra, papel o tijera? ").lower()

    condicion1 = jugador1 == "piedra" and jugador2 == "tijera"
    condicion2 = jugador1 == "papel" and jugador2 == "piedra"
    condicion3 = jugador1 == "tijera" and jugador2 == "papel"

  
    if jugador1 == jugador2:
        print("Resultado de la ronda: Empate")
    elif condicion1 or condicion2 or condicion3:
        puntos_jugador1 += 1
        print("Ganador de la ronda:" , nombre1)
    else:
        puntos_jugador2 += 1
        print("Ganador de la ronda:" , nombre2)

    turno += 1

if puntos_jugador1 > puntos_jugador2:
    print("¡Felicitaciones" , nombre1 , "ganaste el partido!")
elif puntos_jugador1 == puntos_jugador2:
    print(nombre1 , "y" , nombre2 ,"han empatado")
else:
    print("¡Felicitaciones" , nombre2 , "ganaste el partido!")





