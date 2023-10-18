from elements import elementos as el

nome = str(input("Qual o seu nome? "))
erro = "Desculpe, não entendi. Digite o nome de um elemento válido!"

def respostas(entrada):
    entrada = entrada.lower()
    saida = el.get(entrada, erro)
    return saida

def chat():
    print("Olá, {}! Eu sou o ElementoBot. Digite o nome de algum elemento para saber suas propriedades ou diga 'tchau' para sair.".format(nome))
    while True:
        entrada = input("{}: ".format(nome))
        if entrada.lower() == "tchau":
            print("ElementoBot: Até mais, {}!".format(nome))
            break
        saida = respostas(entrada)
        print("ElementoBot: ", saida)

if __name__ == "__main__":
    chat()