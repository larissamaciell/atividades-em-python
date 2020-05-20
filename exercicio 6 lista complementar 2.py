vh=float(input("quanto você ganha por hora trabalhada?"))
ht=float(input("quantas horas você trabalha no mês?"))
sb= vh*ht
irpf=(sb*11/100)
inss=(sb*8/100)
sindicato=(sb*5/100)
sl= sb-irpf-inss-sindicato
print("salario bruto R${:.2f}, irpf {:.2f}, inss {:.2f}, sindicato {:.2f} = salario liquido {:.2f}".format(sb,irpf,inss,sindicato,sl))
