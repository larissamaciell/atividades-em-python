n1=float(input("digite o primeiro numero "))
n2=float(input("digite o segundo numero "))
n3=float(input("digite o terceiro numero "))
if n1>n2 and n1>n3:
 print("este é o maio numero {} ".format(n1))
elif n1<n2 and n1<n3:
 print("este é o menor numero {} ".format(n1))
if n2>n1 and n2>n3:
 print("este é o maior numero {} ".format(n2))
elif n2<n1 and n2<n3:
 print("este é o menor numero {}".format(n2))
if n3>n1 and n3>n2:
 print("este é o maior numero {}".format(n3))
elif n3<n1 and n3<n2:
 print("este é o menor numero {}".format(n3))
else:
 print("não existe numero maior nem menor")
