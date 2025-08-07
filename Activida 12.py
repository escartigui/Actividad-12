Repartidores = {}
def quick_sort(listas):
    if len(listas) <= 1:
        return listas
    else:
     pivote = listas[0]
     menores = [x for x in listas[1:] if x < pivote]
     iguales = [x for x in listas[1:] if x == pivote]
     mayores = [x for x in listas[1:] if x > pivote]
     return quick_sort(menores) + iguales + quick_sort(mayores)

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
