# Verificar si es primo
def primos(N):
    primo=True
    for i in range(2,N):
        if N% i ==0:
            primo= False
    return primo
N=int(input("digite la cantidad de primos: "))
i=2
s="Primo: "
cont=0
while cont<N:
    if primos(i):
        

