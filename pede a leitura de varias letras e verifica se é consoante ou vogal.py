total_consoantes=0
caracteres=[]
for i in range(3):
    letra= input(f"Informe a letra {i+1}:")
    caracteres.append(letra)
    if letra.lower() not in ("aeiou"):
        total_consoantes +=1
print("Os caracteres entrados são",caracteres)
print("O total de consoantes são",total_consoantes)
for c in caracteres:
    if c.lower() not in ("aeiou"):
       print("A consoante é ",c,end="" )
