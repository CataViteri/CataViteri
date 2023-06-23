# funcion que calcula el area de un circulo 
import math
def area_circle(r):
    res = math.pi *(r**2)
    return res

r = float(input('Ingrese el radio del circulo -> '))
print(f'El Area del circulo es {area_circle(r):.2f}')

# Funcion que calcula el volumen de un cilindro 
def vol_cilindro(h):
    res = area_circle(r) * h
    return res

h = float( input('Ingrese la altura del cilindro -> '))
print(f'El volumen del cilindro es {vol_cilindro(h):.2f}')
