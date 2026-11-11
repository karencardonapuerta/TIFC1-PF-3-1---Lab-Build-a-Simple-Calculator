
# CALCULADORA

while True:

    # Menú de opciones
    print("\n===== CALCULADORA =====")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    
    option = input("Escoge la operación que deseas realizar (1-5): ")
    
# Ingresar los dos números
    number1 = int(input("\nIngresa el primer número: "))
    number2 = int(input("Ingresa el segundo número: "))

     

    # Realizar la operación seleccionada
    if option == "1":
        result = number1 + number2
        print("El resultado de la suma es:", result)

    elif option == "2":
        result = number1 - number2
        print("El resultado de la resta es:", result)

    elif option == "3":
        result = number1 * number2
        print("El resultado de la multiplicación es:", result)

    elif option == "4":
        if number2 != 0:
            result = number1 / number2
            print("El resultado de la división es:", result)
        else:
            print("Error: No se puede dividir entre cero.")

    elif option == "5":
        print("Gracias por usar la calculadora.")
        break

    else:
        print("Opción no válida. Escoge entre 1 y 5.")
