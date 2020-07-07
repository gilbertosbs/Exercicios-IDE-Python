#programa que pede o nome e senha e avalia se a senha é keyboard acesso permitido
name=str(input("Digite o nome:"))
if name=='Gilberto':
   print('hello Gilberto')
password=str(input("Digite o password:"))
if password== 'keyboard':
   print('Acess granted.')
else:
    print('Wrong password.')

