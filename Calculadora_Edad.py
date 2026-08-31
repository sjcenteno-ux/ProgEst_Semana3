from colorama import Fore, init

init(autoreset=True)

while True:
    try:
        dad = int(input("Edad: "))
        print("Edad registrada:", edad)
        break 
    except ValueError:
     print(Fore.RED + "Debe ingresar un número entero.")
    finally:
     print("Proceso finalizado.")