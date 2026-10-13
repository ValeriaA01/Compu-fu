from eii_utils import leer_entero 
# variables
promediogeneral:int=0
materia1:int=0
materia2:int=0
materia3:int=0
materia4:int=0
lavadocarrom:int=0
lavadocarrop:int=0
rendimientoacademico:bool=True
ayudacasa:bool=True
decision:bool=True

#imputs
materia1=leer_entero("Digite su promedio de ciencias")
materia2=leer_entero("Digite su promedio de estudios")
materia3=leer_entero("Gigite su promedio de matematicas")
materia4=leer_entero("Digite su promedio de español")
lavadocarrom=leer_entero("Digite cuantas veces ha lavado el carro de su madre")
lavadocarrop=leer_entero("digite cuantas veces ha lavado el carro de su padre")

promediogeneral=(materia1+materia2+materia3+materia4)/4

#process
if (promediogeneral>=75 and materia1>=70 and materia2>=70 and materia3>=70 and materia4>=70
    and (lavadocarrom>=6 and lavadocarrom >=10 or lavadocarrom+lavadocarrop>=14)):
    print("Se le compra videojuesgos")
else:
    print("No se le compra los videojusgos")















