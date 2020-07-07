'programa que le numero e diz se é par ou ímpar'
numero=int(input("Digite um número:"))
numero1=numero%2
if numero1==0:
    print("O numero %d" %numero, 'é par')
elif numero1!=0:
    print("O numero %d" %numero,'é ímpar')
