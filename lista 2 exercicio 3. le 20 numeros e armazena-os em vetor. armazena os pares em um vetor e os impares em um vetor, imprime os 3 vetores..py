#apresenta todos os numeros em um vetor, os pares em uma lista os impares em outro vetor.
numero = []
par = []
impar = []
for i in range ( 20):
    NUMERO2 = int ( input ( "Digite um número: " ) )
    numero.append ( NUMERO2 )  
    if ( NUMERO2% 2 ) == 0:
        par.append ( NUMERO2 )
    else:
        impar.append ( NUMERO2 )

print ("Os numeros são", numero )
print ( "Os numeros pares são",par )
print ("Os  numeros impares são", impar )
