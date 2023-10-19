from elements import elementos as el
import random
from unidecode import unidecode

nome = str(input("Qual o seu nome? "))
erro = "Desculpe, não entendi. Digite o nome de um elemento válido!"

def respostas(entrada):
    entrada = unidecode(entrada.lower())
    saidas = el.get(entrada)
    if saidas is None:
        return erro
    return random.choice(saidas)


def chat():
    print("Olá, {}! Eu sou o ElementoBot. Digite o nome ou número atômico de algum elemento para saber suas propriedades. Diga 'tchau' ou 'bye' para sair.".format(nome))
    while True:
        entrada = input("{}: ".format(nome))
        if entrada.lower() == "tchau" or entrada.lower() == "bye":
            print("ElementoBot: Até mais, {}!".format(nome))
            break
        saida = respostas(entrada)
        print("ElementoBot: ", saida)

if __name__ == "__main__":
    chat()