#4. Construir una una funcion que reciba como parametros una lista de datos numericos y que retome el promedio de dichos datos.
def promedio_numeros(lista):
    suma=0
    promedio=0
    cont=0
    for i in lista:
        suma=suma +i
        cont+=1
        promedio=suma/cont
        return promedio
lista1=[2,3,4,5,6]
promedio=promedio_numeros(lista1)
print(promedio)
#4. Construir una una funcion que reciba como parametros una lista de datos numericos y que retome el promedio de dichos datos.
def promedio_pares(lista):
    suma=0
    promedio=0
    cont=0
    for i in lista:
        if i%2==0:

            suma=suma +i
            cont=cont+1
    promedio=suma/cont
    return promedio

lista1=[2,3,4,5,6]
promedio=promedio_numeros(lista1)
print(promedio)
