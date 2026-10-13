from eii_utils import leer_entero, limpiar_consola
edad:int=0
edades:list[int]=[]
diferencia:list[float]=[]
n:int=0
i:int=0
total:int=0
promedio:float=0


limpiar_consola()
n=leer_entero("digite la cantidad de persona")
edades=[0]*n
diferencia=[0]*n
for i in range(n):
    edad[i]=leer_entero(f"digite la edad {i-1}")
    total= total+edad
promedio=total/n
print(promedio)
for i in range(len(edades)):
    diferencia[i]=promedio-edades[i]

print(edades)
print(diferencia)
