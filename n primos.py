# Hacer un programa que diga los numeros primos que hay desde 0 hasta n 

num = int(input('Ingrese un numero -> '))

if num >= 2:
    print('2', end=',') #Es el primer numero primo 

for i in range (3,num +1):
    primo = True
    for j in range (2, int(i ** 0.5)+ 1):
        if i% j == 0 :
         primo = False
        break

    if primo:
       print(i, end=',')


    

'''
if num == 2:
    print('2')
else:
    for i in range (num):
        if i%1 == 0 and not i%2 == 0 :
            print(i)
            if  not i%3 == 0 and not i%5 == 0 and not i%7 == 0:
                print(i)
'''

