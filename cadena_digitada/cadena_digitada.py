# 2. Construir una funcion que reciba una cadena digitada (como parametro) por el usuario y que se muestre n veces en la pantalla. El valor de n tambien es digitado por el usuario.
print(".............................")
print("......Cadena...Digitada......")
print(".............................")
def mostrar_cadena(cadena,n):
    for i in range(n):
        print(cadena)
        
cadena=input("digite una cadena de texto: ")
n=int(input("digite el numero de veces a mostrar la cadena: "))
mostrar_cadena(cadena,n)        