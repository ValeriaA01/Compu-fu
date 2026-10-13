from eii_utils import limpiar_consola, leer_texto, leer_flotante, mostrar_menu, leer_entero

#variable
n:int=0
menu:list[str]=("morados", "liguistas", "heredianos", "otros")
resultado:float=0
porcentaje:float=0
opcion:float=-1

#procediemiento
n=leer_entero("Cuántos quieren participar")
menu*n

limpiar_consola
for i in range(n):
    mostrar_menu("menu", menu)
    if opcion==1:
        resultado=1
    elif opcion==2:
        resultado=1