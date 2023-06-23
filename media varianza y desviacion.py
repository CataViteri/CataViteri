# Funcion que recibe una lista de numeros y devuelve un diccionario con su media, valianza y desviacion

def Estadistics (lista):
    x = 0 
    y = 0 
    for i in lista:
        x += i
        media = x / len(lista)
        y += (i - media) ** 2
        varianza = y / (len(lista) -1 )
        desviacion = varianza ** 0.5
    dicc = {
        'Media':media, 
        'Varianza': varianza,
        'Desviacion': desviacion
            }
    return dicc

lista = list(map(float,input('Ingrese la lista separada con ","-> ').split(',')))
print(f'{Estadistics(lista)}')
