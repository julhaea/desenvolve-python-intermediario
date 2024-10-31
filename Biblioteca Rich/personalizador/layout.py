from rich import print
from rich.layout import Layout
import os
layout=Layout()


def estrofes(caminho):
    """Imprime o texto do arquivo dividido em estrofes
    
    Paramêtros:
        caminho(str): O caminho do arquivo que contém o texto que será impresso.
    A função recebe o caminho do arquivo txt e testa se o arquivo existe. Se o arquivo existir a função lê o arquivo e separa suas linhas em uma lista.
    Depois, a função monta o layout e imprime as duas primeiras linhas em uma estrofe e as três últimas em outra estrofe.
    """


    if not os.path.isfile(caminho):
        print("O arquivo não existe")
    else:
        with open (caminho, "r") as arquivo:
            linhas =arquivo.readlines()
            layout.split_column(
                Layout(name="upper"),
                Layout(name="lower"))
            layout["upper"].update("".join(linhas[:2]))
            layout["lower"].update("".join(linhas[2:5]))
            print(layout)

def colunas(caminho):
    """Imprime o texto do arquivo dividido em colunas
    
    Paramêtros:
        caminho(str): O caminho do arquivo que contém o texto que será impresso.
    A função recebe o caminho do arquivo txt e testa se o arquivo existe. Se o arquivo existir a função lê o arquivo e separa suas linhas em uma lista.
    Depois, a função monta o layout e imprime as duas primeiras linhas em uma coluna e as três últimas em outra coluna.
    """
    if not os.path.isfile(caminho):
        print("O arquivo não existe")
    else:
        with open (caminho, "r") as arquivo:
            linhas =arquivo.readlines()
            layout.split_row(
                Layout(name="left"),
                Layout(name="right"))
            layout["left"].update("".join(linhas[:2]))
            layout["right"].update("".join(linhas[2:5]))
            print(layout)

