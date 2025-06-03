parcelas = {}

def registrar_parcela():
    print("\nRegistrar Parcela")
    id_parcela = input("Ingrese ID de la parcela: ")
    if id_parcela in parcelas:
        print("ID ya registrado.")
        return
    ubicacion = input("Ingrese ubicación: ")
    dimension = input("Ingrese dimensión en ha: ")
    cultivo = input("Ingrese tipo de cultivo: ")
    
    parcelas[id_parcela] = {
        "ubicacion": ubicacion,
        "dimension": dimension,
        "cultivo": cultivo
    }
    
    print("Parcela registrada")

def listar_parcelas():
    print("\nListado de Parcelas: ")
    if not parcelas:
        print("No existen parcelas registradas")
        return
    for id_parcela, datos in parcelas.items():
        print(f"ID: {id_parcela}, Ubicación: {datos['ubicacion']}, Dimensión: {datos['dimension']}, Cultivo: {datos['cultivo']}")

