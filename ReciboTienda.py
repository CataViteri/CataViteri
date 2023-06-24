#                RECIBO TIENDA 

print ('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')
print ('ingresa la lista de tus compras separadas por "," ->')
productos = input('Ejemplo  "leche:3000, " ->')
            # leche:3000, arroz:20000, carne:28000
print ('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')

# Funcion para recibir diccionario 
def diccionario (productos): # Esta funcion va a recibir productos como str
    pares = productos.split(',')
    canasta = {} # En la variable canasta se va a guardar los productos como diccionario
    for par in pares :
        key, value = par.split(':')
        canasta[key.strip()]  = float(value) # se convierte el str en floart para poder operar los productos 
    # strip elimina espacios inecesarios 
    return canasta 

# Variable para saltos de linea en el diccionario 
output = '\n'.join([f'{key}: {value}' for key, value in diccionario(productos).items()])

# variable que Suma de los valores del diccionario 
price = sum(diccionario(productos).values()) 

# Funcion que aplique un descuento a un precio 
def disc (price):
    if price >= 50000:
        desc = price *0.3
    else:
        desc = 0
    return desc # la funcion 'disc' recibe un precio y si es mayor a 50mil se aplica un descuento del 30 %
    # retorna el 'desc' descuento.
descuento = disc(price)


# Funcion que aplique iva al precio 
def iva(price):
    ivva = price * 1.21
    return ivva
    # retorna el precio con el iva  
Iva = iva(price)

#  precio final

total = iva(price) - disc(price)

print ('------------------------------------------------------')
print ('               Tus productos fueron :')
print(f'{output}')
print ('------------------------------------------------------')
print ('            El total con el iva es de  :')
print(f'                   ${Iva}')
print ('           Tienes un descuento de  :')
print(f'                   ${descuento}!!!!')
print ('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')
print (' \n         EL TOTAL A PAGAR DE TU FACTURA ES  :')
print(f'     >>>>>>>>>      ${total}      <<<<<<<<<<<<')
print ('-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')