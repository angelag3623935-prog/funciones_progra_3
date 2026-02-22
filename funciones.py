def convertir_a_binario(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return convertir_a_binario(n // 2) + str(n % 2)



def contar_digitos(n):
    n = abs(n)
    if n < 10:
        return 1
    return 1 + contar_digitos(n // 10)



def calcular_raiz_cuadrada(numero, intento):
    if intento * intento > numero:
        return intento - 1
    return calcular_raiz_cuadrada(numero, intento + 1)

def raiz_cuadrada_entera(numero):
    if numero < 0:
        return "No existe raíz cuadrada real para números negativos."
    return calcular_raiz_cuadrada(numero, 0)



def convertir_a_decimal(romano):
    valores = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    if len(romano) == 0:
        return 0

    if len(romano) == 1:
        return valores[romano]

    if valores[romano[0]] < valores[romano[1]]:
        return valores[romano[1]] - valores[romano[0]] + convertir_a_decimal(romano[2:])
    else:
        return valores[romano[0]] + convertir_a_decimal(romano[1:])



def suma_numeros_enteros(n):
    if n == 0:
        return 0
    return n + suma_numeros_enteros(n - 1)




def main():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Convertir a Binario")
        print("2. Contar Dígitos")
        print("3. Raíz Cuadrada Entera")
        print("4. Convertir a Decimal desde Romano")
        print("5. Suma de Números Enteros")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero = int(input("Ingrese un número entero: "))
            print("Binario:", convertir_a_binario(numero))

        elif opcion == "2":
            numero = int(input("Ingrese un número entero: "))
            print("Cantidad de dígitos:", contar_digitos(numero))

        elif opcion == "3":
            numero = int(input("Ingrese un número: "))
            print("Raíz cuadrada entera:", raiz_cuadrada_entera(numero))

        elif opcion == "4":
            romano = input("Ingrese un número romano: ").upper()
            print("Valor decimal:", convertir_a_decimal(romano))

        elif opcion == "5":
            numero = int(input("Ingrese un número entero positivo: "))
            if numero < 0:
                print("Debe ser un número positivo.")
            else:
                print("Resultado:", suma_numeros_enteros(numero))

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()