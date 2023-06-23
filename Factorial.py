# Ingresar un numero entero y devuelva du factorial 

def factorial (num):
    res = 1 
    while num > 0:
        res *= num
        num-=1

    print(res)

num= int (input('Ingrese un numero entero -> '))
factorial(num)
