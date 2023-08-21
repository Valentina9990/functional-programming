from functions import fibonacci, volumeSphere, result, evenNumbers, numbers

def showMenu():
    print("Selecciona una opción:")
    print("1. Secuencia de Fibonacci.")
    print("2. Volumen de una esfera.")
    print("3. Calcular la suma de los cuadrados de los números impares de una lista.")
    print("4. Filtrar números pares de una lista.")
    print("5. Salir")

def main():
    print(f'Programación funcional')
    print()
    showMenu()
    option = int(input("Opción: "))

    while option != 5:
        if option == 1:
            n = int(input("Ingrese la cantidad de términos de la serie de Fibonacci: "))
            print(f"Serie de Fibonacci: {fibonacci(n)}")
        elif option == 2:
            radius = float(input("Ingrese el radio de la esfera: "))
            print(f"Volumen de la pirámide: {volumeSphere(radius)} m^3 ")
        elif option == 3:
            print(f"Lista: {str(numbers)}")
            print(f"Suma de los cuadrados de los números impares:{result}")
        elif option == 4:
            print(f"Números pares filtrados: {evenNumbers}")
        else:
            print("Opción inválida")

        print()
        showMenu()
        option = int(input("Opción: "))

    print("Saliendo del programa")


if __name__ == "__main__":
    main()