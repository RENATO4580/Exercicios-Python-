cpf_original = input("Digite o seu cpf apenas números: ")
i = 0
cpf_9 = ""
while i < 9:
    cpf_9+=cpf_original[i]
    i+=1
print(cpf_9)
peso = 10
resultado = 0
i = 0
while i < 9:
    resultado += int(cpf_9[i]) * peso
    peso-=1
    i+=1
print(resultado)
resto = resultado % 11
if resto < 2:
    cpf_9 += "0"
else: 
    cpf_9 += str(11-resto)
print(cpf_9)



peso = 11
resultado = 0
i = 0
while i < 10:
    resultado += int(cpf_9[i]) * peso
    peso-=1
    i+=1
print(resultado)
resto = resultado % 11
if resto < 2:
    cpf_9 += "0"
else: 
    cpf_9 += str(11-resto)
print(cpf_9)
if cpf_9 == cpf_original:
    print("CPF   Valido")
else:
    print("CPF Inválido")
    