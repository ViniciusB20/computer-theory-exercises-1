#Entrada de dados
res1 = float(input('Informe valor da Resistência 1: '))
res2 = float(input('Informe valor da Resistência 2: '))
res3 = float(input('Informe valor da Resistência 3: '))
res4 = float(input('Informe valor da Resistência 4: '))
 
if (res1>res2) and (res1>res3) and (res1>res4):
    maior = res1
    if (res4<res2) and (res4<res3) :
      menor = res4
    if (res2<res4) and (res2<res3) : 
      menor = res2  
    if (res3<res4) and (res3<res2) :
      menor = res3 
  
if (res2>res1) and (res2>res3) and (res2>res4):
    maior = res2
    if (res1<res4) and (res1<res3) :
      menor = res1
    if (res4<res1) and (res4<res3) : 
      menor = res4  
    if (res3<res1) and (res3<res4) :
      menor = res3 
        
if (res3>res1) and (res3>res2) and (res3>res4):
    maior = res3
    if (res1<res2) and (res1<res4) :
      menor = res1
    if (res2<res1) and (res2<res4) : 
      menor = res2  
    if (res4<res1) and (res4<res2) :
      menor = res4 
 
if (res4>res1) and (res4>res2) and (res4>res3):   
  maior = res4   
  if (res1<res2) and (res1<res3) :
      menor = res1
  if (res2<res1) and (res2<res3) : 
      menor = res2  
  if (res3<res1) and (res3<res2) :
      menor = res3 
       
print("")
print("A maior Resistência é = %.2f" %maior)
print("A menor Resistência é = %.2f" %menor)