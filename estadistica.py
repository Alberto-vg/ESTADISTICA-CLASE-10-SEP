def media(li=[]):
    if len(li) == 0:
        return 0
    nl = len(li)
    suma = 0 
    for x in li:
        suma = suma + x
    return suma/nl

def mediana(li=[]):
    if len(li) == 0:
        return 0
    
    # Ordenar la lista
    lista_ordenada = sorted(li)
    n = len(lista_ordenada)
    
    # Calcular la mediana
    if n % 2 == 1:  # Si es impar
        return lista_ordenada[n // 2]
    else:  # Si es par
        medio1 = lista_ordenada[(n // 2) - 1]
        medio2 = lista_ordenada[n // 2]
        return (medio1 + medio2) / 2

def varianza(li=[]):
    if len(li) == 0:
        return 0
    nl = len(li)
    xm = media(li)
    
    suma = 0
    for x in li:
        suma = suma + (x - xm)**2
    return suma/(nl-1)

def desviacion_estandar(li=[]):
    return varianza(li)**0.5

def asimetria(li=[]):
    if len(li) == 0:
        return 0
    nl = len(li)
    xm = media(li)
    s = desviacion_estandar(li)
    
    suma_cubos = 0
    for x in li:
        suma_cubos = suma_cubos + (x - xm)**3
    
    # Fórmula de asimetría: [Σ(xi - x̄)³ / n] / s³
    asimetria_valor = (suma_cubos / nl) / (s**3)
    return asimetria_valor

def curtosis(li=[]):
    if len(li) == 0:
        return 0
    nl = len(li)
    xm = media(li)
    s = desviacion_estandar(li)
    
    suma_cuartos = 0
    for x in li:
        suma_cuartos = suma_cuartos + (x - xm)**4
    
    # Fórmula de curtosis: [Σ(xi - x̄)⁴ / n] / s⁴ - 3
    curtosis_valor = (suma_cuartos / nl) / (s**4) - 3
    return curtosis_valor



# Ejemplo de uso
datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Media: {media(datos)}")
print(f"Mediana: {mediana(datos):.2f}")
print(f"Varianza: {varianza(datos)}")
print(f"Desviación estándar: {desviacion_estandar(datos)}")
print(f"Asimetría: {asimetria(datos)}")
print(f"Curtosis: {curtosis(datos):.2f}")


#  con datos asimétricos
datos_asimetricos = [1, 1, 1, 2, 2, 3, 4, 5, 10, 15]
print(f"\nDatos asimétricos: {datos_asimetricos}")
print(f"Asimetría: {asimetria(datos_asimetricos)}")

#  con diferentes distribuciones
print("\n" + "="*50)
