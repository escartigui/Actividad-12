Repartidores = {}
def quick_sort(listas):
    if len(listas) <= 1:
        return listas

    pivote = listas[0]
    menores = [x for x in listas[1:] if x[1] < pivote[1]]
    iguales = [x for x in listas if x[1] == pivote[1]]
    mayores = [x for x in listas[1:] if x[1] > pivote[1]]
    return quick_sort(menores) + iguales + quick_sort(mayores)
def menu():
    print("MENU")
    print("1.Agregar")
    print("2.Ordenar")
    print("3.Buscar")
    print("4.Estadistica")
    print("5.Salir")

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

print("\n Busqueda secuencial")
listas = list(Repartidores.values())
ordenados = quick_sort(listas)

for nombre, cantidad in ordenados:
    datos = Repartidores[nombre]
    print(f"nombre: {nombre}")
    print(f"zonas: {datos['zonas']}")
    print(f"paquetes: {datos['paquetes']}")