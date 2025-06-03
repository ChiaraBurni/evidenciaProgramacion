from gestion_parcelas import registrar_parcela, listar_parcelas
from gestion_sensores import registrar_sensor
from registro_mediciones import registrar_medicion
from consulta_datos import consultar_datos
from recomendaciones import recomendacion

def mostrar_menu():
    print("\nMenú Principal")
    print("1. Registrar parcela")
    print("2. Listar parcelas")
    print("3. Registrar nuevo sensor")
    print("4. Registrar nueva medición")
    print("5. Consultar datos")
    print("6. Recomendación según medición")
    print("0. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_parcela()
        elif opcion == "2":
            listar_parcelas()
        elif opcion == "3":
            registrar_sensor()
        elif opcion == "4":
            registrar_medicion()
        elif opcion == "5":
            consultar_datos()
        elif opcion == "6":
            recomendacion()
        elif opcion == "0":
            print("Saliendo")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
