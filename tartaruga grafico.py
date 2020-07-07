import turtle                #importa os gráficos tartaruga
t=turtle.Pen()
turtle.bgcolor("Black")
colors=['red','blue','yellow','green']
your_name= turtle.textinput("Entre seu nome","qual é o seu nome?")  # pede a entrada de dados usando o pop-up.

for x in range(1000): #desenha uma espiral na tela usando o nome, escrevendo-o 100 vezes.
     t.pencolor(colors[x%4]) #circula pelas quatro cores
     t.forward(x*5)    #apenas move a tartaruga pela tela
     t.pendown()        #escreve o nome do usuário, cada vez maior
     t.width(x/120+1)
     t.left(110)
     
