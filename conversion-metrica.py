# Paso 1: Solicitar al usuario las medidas de l apieza del mueble en cms

medida_en_cms = float(input("por favor, ingrese la medida de la pieza del mueble (en cms): "))

# Paso 2: Convertir las medidas de centimetros a pulgadas

medida_en_pulgadas = medida_en_cms / 2.54

# Paso 3: Mostrar las medidas convertidas en pulgadas al usuario

print("las medidas en pulgadas de la pieza ingresada son", medida_en_pulgadas)