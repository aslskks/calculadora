import random

def jugar_nuevo_juego():
    print("¡Bienvenido al juego del Ahorcado!")
    palabras = ["PYTHON", "COMPUTADORA", "ALGORITMO", "PROGRAMACION", "INTELIGENCIA", "ARTIFICIAL", "DATOS", "ESTRUCTURA", "LEVIATAN2"]
    palabra_secreta = random.choice(palabras).upper()
    palabra_oculta = "_" * len(palabra_secreta)
    intentos = 6
    letras_erroneas = []
    
    muñeco_etapas = [
        "  ________\n  |      |\n         |\n         |\n         |\n         |\n",
        "  ________\n  |      |\n  O      |\n         |\n         |\n         |\n",
        "  ________\n  |      |\n  O      |\n  |      |\n         |\n         |\n",
        "  ________\n  |      |\n  O      |\n /|      |\n         |\n         |\n",
        "  ________\n  |      |\n  O      |\n /|\\     |\n         |\n         |\n",
        "  ________\n  |      |\n  O      |\n /|\\     |\n /       |\n         |\n",
        "  ________\n  |      |\n  O      |\n /|\\     |\n / \\     |\n         |\n"
    ]

    while intentos > 0 and "_" in palabra_oculta:
        print("La palabra a adivinar es:", palabra_oculta)
        print(f"Te quedan {intentos} intentos.")
        print("Letras erróneas:", ", ".join(letras_erroneas))
        letra = input("Ingresa una letra: ").upper()

        if letra in palabra_secreta:
            print("¡Adivinaste una letra!")
            palabra_oculta = "".join(letra if letra == palabra_secreta[i] else palabra_oculta[i] for i in range(len(palabra_oculta)))
            
        else:
            print("¡Esa letra no está en la palabra!")
            intentos -= 1
            letras_erroneas.append(letra)
            etapa_actual = 6 - intentos
            print(muñeco_etapas[etapa_actual])

    if "_" not in palabra_oculta:
        print(f"¡Felicitaciones! Adivinaste la palabra: {palabra_secreta}")
    else:
        print(f"¡Te quedaste sin intentos! La palabra era: {palabra_secreta}")

    volver_a_jugar = input("¿Quieres jugar otra vez? (S/N)").upper()
    if volver_a_jugar == "S":
        jugar_nuevo_juego()

jugar_nuevo_juego()
