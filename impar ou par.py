#verifica se o numero é impar ou par
n1=int(input("Informe um numero inteiro:"))
n2=n1*2-n1%2
if n2==0:
   print("O numero é par %d" %n1)
else:
    print("O numero é impar %d" %n1)
