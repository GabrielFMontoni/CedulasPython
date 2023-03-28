#Criado por Gabriel Felipe Montoni
#https://github.com/GabrielFMontoni
#https://www.linkedin.com/in/gabriel-felipe-montoni/
#Decomposição de Cédulas

#Primeiro Modo
dinheiro = int(input("Digite quanto dinheiro você pegou: "))
nota100 = dinheiro//100#abc
nota50= (dinheiro-nota100*100)//50
nota20= (dinheiro-nota100*100-nota50*50)//20
nota10= (dinheiro-nota100*100-nota50*50-nota20*20)//10
print(f"Foram usadas {nota100} notas de 100, {nota50:} notas de 50, {nota20:} notas de 20"
      f" e {nota10}")

#Segundo Modo
dinheiro = int(input("Digite quanto dinheiro você pegou: "))
nota100 = dinheiro//100
dinheiro = dinheiro % 100
nota50= dinheiro//50
dinheiro = dinheiro % 50
nota20= dinheiro // 20
dinheiro = dinheiro % 20
nota10= dinheiro // 10
dinheiro = dinheiro % 10
print(f"Foram usadas {nota100} notas de 100, {nota50:} notas de 50, {nota20} notas de 20"
      f" e {nota10}")