try:
    edad = int(input("Edad: "))
    print("Edad registrada:", edad)
except ValueError:
    print("Debe ingresar un número entero.")
finally:
    print("Proceso finalizado.")