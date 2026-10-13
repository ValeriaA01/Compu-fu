from eii_utils import limpiar_consola, pausar, mostrar_menu, leer_flotante
#variables
menu:list[str]=["ver salgo","depositar","retirar"]
opcion=int=-1
saldo:float=0
dinero:float=0



while not(opcion==0):
    opcion=mostrar_menu("Menu", menu)
    if opcion==0:
        print("muchas gracias por confiar en el grupo 01")
    elif opcion==1:
        print(f"saldo{saldo}")
        pausar()
    elif opcion==2:
        dinero=leer_flotante("monto a depositar")
        saldo=saldo=+dinero
    elif opcion==3:
        dinero=leer_flotante("monto a retirar")
        saldo=saldo-dinero

    limpiar_consola
    


    

