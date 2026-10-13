from eii_utils import leer_entero, leer_flotante, leer_booleano, limpiar_consola

n:int=0
cantidad_de_horas:float=0
total_de_piezas:float=0
piezas_entotal:float=0
supervivencia:float=1

n=leer_entero("cuantas personas son")


#proceso 
for i in range(n):
    cantidad_de_horas=leer_flotante("digite la cantidad de horas laboradas")
    total_de_piezas=leer_flotante("digite la cantidad de piezas realizadas")


piezas_entotal=piezas_entotal+total_de_piezas
supervivencia=supervivencia*0.99

print("total de piezas",piezas_entotal)
print("supervivencia", supervivencia)




