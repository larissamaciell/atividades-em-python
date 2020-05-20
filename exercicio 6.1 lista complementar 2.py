vh=float(input("quanto você ganha por hora trabalhada?"))
ht=float(input("quantas horas você trabalha no mês?"))
sb= vh*ht
print("salario bruto R${:.2f}",sb, "irpf {:.2f}",(sb*11/100), "inss {:.2f}",(sb*8/100), "sindicato {:.2f}",(sb*5/100))
