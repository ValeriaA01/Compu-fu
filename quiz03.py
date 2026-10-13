from eii_utils import leer_booleano, leer_flotante, limpiar_consola, leer_entero

#variables primera parte
temperatura:float=0
presion:bool=True
materiaprima:bool=True
ordendereabastecimiento:bool=True
autorizado:bool=True



#entradas primera parte
temperatura=leer_flotante("Digite la temperatura en °C")
presion=leer_booleano("¿La presión de la línea es óptima?")
materiaprima=leer_booleano("¿Hay materia prima disponible en bodega?")
ordendereabastecimiento=leer_booleano("¿Hay una orden de reabastecimiento activa?")


#variable parte 3 
calidad:bool=True
mantenimiento:bool=True

#entradas tercera parte 
calidad=leer_booleano("¿La inspeción de calidad no fue aprobada?")
mantenimiento=leer_booleano("¿Existe un manteniemiento pendiente")


#proceso primera parte
limpiar_consola()
if (temperatura>=180 and presion
    and (materiaprima or ordendereabastecimiento)): 
    print(autorizado)  
else:
    print (not autorizado)
    if calidad and mantenimiento:
        print("Paro Técnico Obligatorio")
    else:print("Detenido en Espera de Materia Prima")



#variables segunda parte
operarioscapacitados:int=0
turno_nocturno:bool=True

#entradas parte intermedia 
operarioscapacitados=leer_entero("¿Cuántos operarios capacitados?")
turno_nocturno=leer_booleano("¿La planta se encuntra en turno nocturno?")

#proceso parte intermedia 
if autorizado and operarioscapacitados>=3 and turno_nocturno:
    print("línea 1")
else:
    print("línea 2")

limpiar_consola()


