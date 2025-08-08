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
            if nombre == "":
                print("Agrega el nombre")
            elif nombre in Repartidores:
             print("ya Utilizado")
            else:
                break
          Repartidores[nombre] = {}
          while True:
              try:
                  paquetes = int(input("ingrese cantidad del paquete: "))
                  if paquetes < 0:
                      print("no puede ser negativo")
                  else:
                      Repartidores[nombre]['paquetes'] = paquetes
                      break
              except ValueError:
                  print("debe ser entero")
          while True:
            zona = input("ingrese la zona: ")
            if zona == "":
                print("esta vacio")
            else:
                Repartidores[nombre]['zona'] = zona
                break
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
                print(f"{Repartidores[buscado]}: {buscado}") #detallistos
            else:
                print("No se encuentra")
        case 4:
            print("Estadistica")
            if len(Repartidores) == 0:
                print("no hay nada aqui")
                continue
            total = 0
            for r in Repartidores.values():
                total += r['paquetes']
            print(f"el total de paquetes es: {total}")

            reparti = len(Repartidores)
            if reparti > 0:
                promedio = total / reparti
                print(f"El promedio es de: {promedio}")
            else:
                print("verifica, no hay nada aqui")
        case 5:
            print("Hasta que nos volvamos a ver :3 ")
            break
menu()