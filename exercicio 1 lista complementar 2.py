l1=float(input("digite o primeiro lado do triangulo"))
l2=float(input("digite o segundo lado do triangulo"))
l3=float(input("digite o terceiro lado do trinangulo"))
if l1<l2+l3 or l2<l1+l3 or l3<l1+l2:
    if l1==l2 and l2==l3:
        print ("triangulo equilatero")
    elif l1==l2 or l2==l3 or l3==l1:
        print ("triangulo isosceles")
    elif l1!=l2 and l2!=l3 and l3!=l1:
        print("triangulo escaleno")
    else:
            print ("nao é possivel formar um triangulo")
