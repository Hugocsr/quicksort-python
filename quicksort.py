'''
Created on 12 de ago de 2016

@author: Hugo
'''

def qsort(a):
    if len(a)<=1:
        return a
    menor, igual, maior = [], [], []
    pivo = a[0]
    for i in a:
        if i < pivo:
            menor.append(i)
        elif i == pivo:
            igual.append(i)
        else:
            maior.append(i)
    return qsort(menor) + igual + qsort(maior)


entrada = input()
lista = entrada.split(' ')
lista2 = []
for j in lista:
    k = int(j)
    lista2.append(k)
lista2 = qsort(lista2)
for i in range(len(lista2)-1):
    print(lista2[i], end= ' ')
print(lista2[-1], end='')