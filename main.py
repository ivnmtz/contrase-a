import random
caracteres="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud=int(input("introduzca la longitud"))
contrasena=""
for i in range(longitud):
    contrasena += random.choice(caracteres)
print(contrasena)
