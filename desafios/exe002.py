#funçao mensagem
def mensagem(msg):
    print("Seja bem Vindo")
    print(msg)
#fim função mensagem

#função caixaTexto
def caixaTexto(txto):
    print ("-=-" * 20)
    print(txto) 
    print ("-=-" * 20)
#fim função caixa texto
    

nome = input("Digite o Seu nome: ")

print (caixaTexto(mensagem(nome)))

