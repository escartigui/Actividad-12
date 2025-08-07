def quick_sort(listas):
    if len(listas) <= 1:
        return listas

    pivote = listas[0]
    menores = [x for x in listas[1:] if x[1]['paquetes'] < pivote[1]['paquetes']]
    iguales = [x for x in listas if x[1]['paquetes'] == pivote[1]['paquetes']]
    mayores = [x for x in listas[1:] if x[1]['paquetes'] > pivote[1]['paquetes']]
    return quick_sort(mayores) + iguales + quick_sort(menores)
Repartidores = {}
def menu():
 while True:
    print("MENU")
    print("1.Agregar")
    print("2.Ordenar")
    print("3.Buscar")
    print("4.Estadistica")
    print("5.Salir")
    op = int(input("ingrese una opcion: "))

    match op:
        case 1:
         cantidad = int(input('Cantidad de Repartidores: '))
         for i in range(cantidad):
          while True:
            nombre = input("ingrese el nombre")
            if nombre in Repartidores:
             print("ya Utilizado")
            else:
                break
          Repartidores[nombre] = {}
          Repartidores[nombre]['paquetes'] = int(input("ingrese cantidad de paquetes: "))
          Repartidores[nombre]['zonas'] = input("ingrese cantidad de zonas: ")
        case 2:
         print("\n Listado")
         lista = list(Repartidores.items())
         ordenados = quick_sort(lista)

         for nombres, valor in ordenados:
          print(f"{nombres}: {valor}")
        case 3:
            print("Busqueda")
            def busqueda(lista, objetivo):
                for elemento in lista:
                    if elemento == objetivo:
                        return elemento
                return None
            buscado = input("ingrese el nombre")
            resultado = busqueda(Repartidores, buscado)
            if resultado is not None:
                print(f"el valor {Repartidores} esta en la lista") #detallistos
            else:
                print("No se encuentra")

menu()