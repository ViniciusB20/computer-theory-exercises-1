#Calcular IMC Da Galera
resp=0
while resp!=2 :
  nome = input('NOME:')
  altura = float(input('ALTURA:'))
  peso = float(input('PESO:'))
  imc = peso/(altura*altura)
  print('')
  print("Nome: %s " %nome)
  print("IMC = %.2f" %imc)
  print('')
  print('1 = Sim')
  print('2 = Não')
  resp = int(input('Deseja continuar ? :'))
