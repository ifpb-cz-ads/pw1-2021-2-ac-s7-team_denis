#2) Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras
lista1=[0,0,0]
lista2=[0,0,0]
lista3=[]
k = 0
print("****LISTA NUMERO 1*****")
while k < 3:
    lista1[k]= int(input('Informe um numero inteiro:'))
    k = k +1
k = 0
print("****LISTA NUMERO 2******")
while k < 3:
    lista2[k]= int(input('Informe um numero:'))
    k = k +1
k = 0
print("****LISTA NUMERO 3******") 
while k < 3:
    print(f"{lista1[k]},{lista2[k]}")
    k = k +1

    