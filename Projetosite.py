def obter_limite():
 global limite, idade
 print('''Bem-vindo à Loja do Thomas” Aqui quem fala é Julia
 faremos uma análise de crédito.''')
 cargo = input("informe seu cargo: ")
 salario = int(input("informe seu salario: "))
 ano = int(input("informe seu ano: "))
 idade = 2020 - ano
 limite = (salario * (idade / 1000)) + 100
 print ('Seu cargo: {} Seu salario: {} Seu ano de nascimento: {}'.format(cargo, salario, ano))
 print ('A sua idade é: {} Seu limite é: {}  '.format(idade, limite))
obter_limite()


Quantidade = int(input("Quantos produtos deseja cadastrar: "))

valorn = 0

def verificar_produto():
 global valor, limitea, limiteb, limitec, valorn
 produto = input('Digite o nome de um produto: ')
 valor = int(input('qual e o valor dele: '))
 valorn = valorn + valor
 limitea = limite * 60 / 100
 limiteb = limite * 90 / 100
 limitec = limite * 100 / 100
verificar_produto()


for c in range(1,Quantidade):
      verificar_produto()
    





if valorn <= limitea:
  print ('Liberado R${}'.format(valorn))
elif valorn > limitea and valorn < limiteb:
  print ('Liberado ao parcelar em até 2 vezes R${}'.format(valorn))
elif valorn >= limiteb and valorn <= limitec:
  print ('Liberado ao parcelar em 3 ou mais vezes R${}'.format(valorn))
elif valorn > limitec:
  print ('Bloqueado')
else:
  print ('Obrigado por comprar')
if valorn >= 18 and valorn <= idade:
  valora = valorn - (valorn * 18 / 100)
  print ('Com desconto entre caractere e idade(maior que 18 menor que a sua idade {} ficara R${}'.format(idade, valora))

















