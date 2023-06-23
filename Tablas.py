# ingresar un numero y el programa da la tabla de multiplicar

num = int(input('Ingrese la tabla de multiplicar que desea consultar ->'))

for i in range (1,11):
    res = num * i 
    print(f'{num} x {i} = {res}')