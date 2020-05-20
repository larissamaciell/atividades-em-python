area=float(input("informe a área em metros quadrados: "))
litros=area/3
if area%54==0:
  latas=area/54
else:
  latas=int(area/54)+1
  preco=latas*80
  print("a quantidade de tinta necessária é:{} lata(s)".format(latas))
  print("preço total R$ {:.2f}".format(preco))
