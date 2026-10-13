from eii_utils import leer_booleano, leer_entero
#variables
clima_soleado:bool=True
presupuesto:int=0
sabado:bool=True
trabajos_pendientes:bool=True
pelicula:bool=True
entradascarlos:bool=True
cuponesmaria:bool=True

#imputs
clima_soleado=leer_booleano("Está soleado?")
presupuesto=leer_entero("Digite su presupuesto")
sabado=leer_booleano(" Es sabado?")
trabajos_pendientes=leer_booleano(" No tiene trabajos de la u pendientes?")
pelicula=leer_booleano("Está en cartelera El Coyote vrs Acme?")
entradascarlos=leer_booleano("Carlos tiene entradas?")
cuponesmaria=leer_booleano("Maria tiene entradas?")


#process
if clima_soleado and presupuesto>=95000 and sabado:
    print(" Se puede hacer opcion 1")
elif trabajos_pendientes and presupuesto>=15000:
    print("se puede hacer la opcion 2")
elif pelicula and (entradascarlos or cuponesmaria):
    print("se puede hacer la opcion 3")
else:
    print("No se puede hacer nada")


