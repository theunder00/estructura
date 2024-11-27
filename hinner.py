# Calculadora en Python

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero"
    return a / b

def calculadora():
    print("Bienvenido a la calculadora interactiva")
    while True:
        print("\nOpciones:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        opcion = input("Selecciona una opción (1-5): ")

        if opcion == '5':
            print("¡Gracias por usar la calculadora! Adiós.")
            break

        if opcion not in ['1', '2', '3', '4']:
            print("Opción no válida. Por favor, intenta de nuevo.")
            continue

        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Por favor, ingresa valores numéricos válidos.")
            continue

        if opcion == '1':
            print(f"El resultado de la suma es: {suma(num1, num2)}")
        elif opcion == '2':
            print(f"El resultado de la resta es: {resta(num1, num2)}")
        elif opcion == '3':
            print(f"El resultado de la multiplicación es: {multiplicacion(num1, num2)}")
        elif opcion == '4':
            print(f"El resultado de la división es: {division(num1, num2)}")

if __name__ == "__main__":
    calculadora()
