#Para validar la entrada del jugador 1: 
def validar_entrada(prompt, min_num=1, max_num=1000):
    while True: 
        try: 
            numero= int(input(prompt))
            if min_num <= numero <= max_num:
                return numero 
            else: 
                print(f"Error: Por favor, introduce un número entre {min_num} y {max_num}.")
        except ValueError:
            print("Error: Entrada inválida, asegúrate de introducir un número correcto.")