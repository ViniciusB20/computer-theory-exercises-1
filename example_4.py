#Calcular o Reajuste Preço Farmácia
nome = input('NOME DO PRODUTO:')
valor = float(input('VALOR DO PRODUTO:'))
 
if  (50<=valor) and (valor<200):
    preco = (valor*0.95)
if (200<=valor) and valor<500:
     preco = (valor*0.94)
if (500<=valor) and (valor<1000):
     preco = (valor*0.93)
 
if valor >= 1000:
     preco = (valor*0.92)   
 
print("")
print("Nome do produto: %s " %nome)
print("Preço normal = $%.2f" %valor)
print("Preço com desconto = $%.2f" %preco)