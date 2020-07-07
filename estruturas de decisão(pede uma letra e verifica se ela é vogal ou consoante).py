#verifica se o caractere digitado é consoante ou vogal
l = str(input('Digite uma letra: ').lower())# o comando lower deixa qualquer letra minuscula
#para facilitar o processamento com a decisão em letras minusculas.
if l == 'a'or l=='e' or l=='i' or l== 'o' or l== 'u':
    print('A letra',l,'é vogal')
else:
    print('A letra',l,'é consoante')
