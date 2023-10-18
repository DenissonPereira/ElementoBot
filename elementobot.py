from elements import elementos as el

erro = "Desculpe, não entendi. Digite o nome de um elemento válido!"

def respostas(entrada):
    entrada = entrada.lower()
    saida = el.get(entrada, erro)
    return saida

def chat():
    print("Olá! Eu sou o ElementoBot. Digite o nome de algum elemento para saber suas propriedades ou diga 'tchau' para sair.")
    while True:
        entrada = input("Você: ")
        if entrada.lower() == "tchau":
            print("ElementoBot: Até mais!")
            break
        saida = respostas(entrada)
        print("ElementoBot: ", saida)

if __name__ == "__main__":
    chat()