#vetor que pede a entrada de valores e os exibe na ordem inversa
vetor=[]
for i in range(3):
    valor = float(input(f" Informe o valor {i+1}: "))
    vetor.append(valor)
vetor.reverse()
print(vetor)
