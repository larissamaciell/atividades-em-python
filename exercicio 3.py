peso=float(input("Peso de peixes"))
excedente= peso-50
multa= excedente*4
if peso>50:
 print("o peso excedente é {:.2f} kg e o valor da multa é R${:.2f}".format(excedente,multa))
else:
 print("o peso excedente é 0 kg e o valor da multa é R$0")
