# Vamos usar uma variável chamada nome para 
# guarda o nome do cliente.Utilizaremos também 
# o comando input(in -> dentro | put-> por em algum lugar)
nome = input("digite o seu nome: ")
print("olá Sr(a)."+nome)
print(f"olá, Sr(a). {nome}")
# O operador +(mais) foi utilizado para 
# concatenar (juntar) o texto entre aspa("")
# com a variável nome 
print("olá Sr(a)."+nome+".Seja bem vindo")
# Abaixo, usamos o comando print com a letra 
# f(format) para inserir uma variável no meio 
#  de uma string. A variável foi inserida com chaves({})
# esta tecnica é chamada de interpolação
print(f"olá, Sr(a). {nome}. Seja bem vindo")