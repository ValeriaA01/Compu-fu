from eii_utils import leer_booleano, leer_texto, limpiar_consola
pieza_metalica:bool=(True)
prueba_dimenciones:bool=(True)
prueba_dureza:bool=(True)

#proceso
prueba_dimenciones=leer_booleano("Las dimenciones están correctas")
prueba_dureza=leer_booleano("la dureza está aceptable")

if prueba_dureza and prueba_dimenciones:
    print("se pasa a despacho")
else: print("desechar")

limpiar_consola