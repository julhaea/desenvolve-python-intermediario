from rich import print
from rich.panel import Panel
import os



def borda(caminho):
    """Imprime o texto com borda
    
    Paramêtros:
        caminho(str): O caminho do arquivo que contém o texto que será impresso.
    A função recebe o caminho do arquivo txt e testa se o arquivo existe. Se o arquivo existir a função lê o arquivo e imprime ele com uma borda
    """
    if not os.path.isfile(caminho):
        print("O arquivo não existe")
    else:
        with open (caminho, "r") as arquivo:
            texto =arquivo.read()

            print(Panel(texto))

def titulo(caminho):
    """Imprime o texto com borda e adiciona título e subtítulo
    
    Paramêtros:
        caminho(str): O caminho do arquivo que contém o texto que será impresso.
    A função recebe o caminho do arquivo txt e testa se o arquivo existe. Se o arquivo existir a função lê o arquivo e imprime ele com uma borda,
     e adiciona o nome da música como título e o nome do autor como subtítulo.
    """
    if not os.path.isfile(caminho):
        print("O arquivo não existe")
    else:
        with open (caminho, "r") as arquivo:
            texto =arquivo.read()

            print(Panel(texto, title="SOB O MAR", subtitle='Bullara'))


