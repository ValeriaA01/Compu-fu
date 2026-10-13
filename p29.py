from eii_utils import limpiar_consola, leer_flotante, leer_texto, leer_entero

# listas
n:int=0
personas:list[str]=[]
montos:list[float]=[]
nombre:str=""
monto:float=0
total:float=0
promedio:float=0

n =leer_entero("Digite la cantidad de personas")
personas=[""]*n
montos=[1]*n
limpiar_consola
for i in range(n):
    nombre=leer_texto("Digite el nombre")
    personas[i]=nombre
    monto=leer_flotante("Digite el monto")
    montos[i]=monto
    total=total+monto
    print("-"*10)

promedio=total/n

for i in range (n):
    nombre=personas[i]
    monto=montos[i]
    if monto>promedio:
        print(f"{nombre:20}{monto:10}")
    else:
        print(f"{nombre:20}{monto:10}")

print(f"total  {total}")
print(f"promedio {promedio}")
