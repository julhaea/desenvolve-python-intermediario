import time
from rich.progress import track

import os


def ler5seg(caminho):
    """Aguarda 5 segundos e depois imprime o texto com borda e adiciona título e subtítulo
    
    
    A função recebe o caminho do arquivo txt e testa se o arquivo existe. Se o arquivo existir a função executa uma barra de progresso que espera 5 segundos e depois lê o arquivo e imprime.
    """

    if not os.path.isfile(caminho):
        print("O arquivo não existe")
    else:
        for i in track(range(5), description="Lendo texto"):
            time.sleep(1)
        with open (caminho, "r") as arquivo:
            texto =arquivo.read()
            print(texto)
def inverter(caminho):

    """Imprime o texto do arquivo invertendo a ordem das linhas
    
    Paramêtros:
        caminho(str): O caminho do arquivo que contém o texto que será impresso.
    A função recebe o caminho do arquivo txt e testa se o arquivo existe. Se o arquivo existir a função executa uma barra de progresso que espera por 10 segundos e depois lê o arquivo e separa suas linhas em uma lista.
    Depois, a função imprime a lista de linhas ao contrário.
    """
    if not os.path.isfile(caminho):
        print("O arquivo não existe")
    else:
        for i in track(range(10), description="Invertendo ordem do texto..."):
            time.sleep(1)
        with open (caminho, "r") as arquivo:
            linhas =arquivo.readlines()
            for linha in linhas[::-1]:
                print(linha)


