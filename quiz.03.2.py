from eii_utils import leer_booleano, leer_flotante, leer_entero, limpiar_consola

#variables 
kw_consumidos:float=0
subtotal_consumo:float=0
Alumbrado:float=0
tributo_bomberos:float=0
IVA:float=0

limpiar_consola()
#imputs
kw_consumidos=leer_flotante("Digite su consumo de luz en Kw")


#proceso 
if kw_consumidos<=30:
    subtotal_consumo=1744.80
elif kw_consumidos<=200 and kw_consumidos>=31:
    subtotal_consumo=1744.80+(kw_consumidos-30)*58.16
elif kw_consumidos<=300 and kw_consumidos>=201:
    subtotal_consumo=(1744.80 + (170*58.16)+((kw_consumidos-230)*89.24))
else:
    subtotal_consumo=(1744.80+(170*58.16)+(130*89.24)+(kw_consumidos-300)*92.27)


#Alumbrado
Alumbrado=kw_consumidos*3.2

#tributo de bomberos
if kw_consumidos<=100:
    tributo_bomberos=0
else: 
    kw_consumidos<=1750
    tributo_bomberos=(subtotal_consumo*(0.0175))

#IVA
if kw_consumidos<280:
    IVA=0
else:
    kw_consumidos>=280
    IVA=(subtotal_consumo+Alumbrado+tributo_bomberos)*0.13

#total
Pago_total=subtotal_consumo+Alumbrado+tributo_bomberos+IVA

#salidas
limpiar_consola()

print("="*45)
print("          DESGLOSE DE FACTURA ELÉCTRICA (CNFL)      ")
print("="*45)
print(f"Consumo mensual:              {kw_consumidos:10.2f} kWh")
print("="*45)
print(f"subtotal_consumo:             ₡ {subtotal_consumo:10.2f}")
print(f"Alumbrado Público:            ₡ {Alumbrado:10.2f}")
print(f"Tributo a Bomberos (1.75%):   ₡ {tributo_bomberos:10.2f}")
print(f"Impuesto IVA (13%):           ₡ {IVA:10.2f}")
print("-"*45)
print(f"TOTAL A PAGAR:                ₡ {Pago_total:10.2f}")
print("="*45)
