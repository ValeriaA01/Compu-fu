from eii_utils import limpiar_consola, leer_booleano, leer_entero, leer_flotante
#variable
total:float=0
costo_producto:float=0
impuesto:float=0
cantidad_de_producto:int=0
#Proceso
limpiar_consola=()


cantidad_de_producto=leer_entero("digite la cantidad de productos")

costo_producto=leer_flotante("Digite precio del producto")


if (costo_producto*cantidad_de_producto)>50000:
    impuesto=(costo_producto*cantidad_de_producto)*0.10
    total=(costo_producto*cantidad_de_producto)+impuesto
else: 
    total=costo_producto*cantidad_de_producto

print("su impuesto es de",impuesto)

print("su total a pagar es", total)

