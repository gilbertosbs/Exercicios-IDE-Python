#mostra os numeros em ordem descrecente
a=int(input("Insira um numero:"))
b=int(input("Insira um numero:"))
c=int(input("Insira um numero:"))
if a<b:
    x=a
    a=b
    b=x
    if a<c:
        x=a
        a=c
        c=x
        if b<c:
            x=b
            b=c
            c=x
print(a,b,c)
