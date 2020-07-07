altura=float(input("Informe a sua altura:"))
sexo=input("Informe o seu sexo:")
if sexo[0] in ('m','M'):
   peso_ideal=(72.7*altura)-58
   print("\nO peso ideal deste homem deverá ser %d" %peso_ideal)
elif sexo[0] in('f','F'):
    peso_ideal=(62.1*altura)-44.7
    print(peso_ideal)

    
