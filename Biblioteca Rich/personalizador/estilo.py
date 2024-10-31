from rich.console import Console
from rich.style import Style
import os
def bold(caminho):
    """Imprime o texto do arquivo em negrito

    Paramêtros:
        caminho(str): O caminho do arquivo que contém o texto que será impresso.
    A função recebe o caminho do arquivo txt e testa se o arquivo existe. Se o arquivo existir a função lê o arquivo e imprime ele em negrito.
    """
    if not os.path.isfile(caminho):
        print("O arquivo não existe")
    else:
        with open (caminho, "r") as arquivo:
            texto =arquivo.read()
            Console().print(texto,style="bold")
        
def red(caminho):
    """Imprime o texto do arquivo em vermelho
    
    Paramêtros:
        caminho(str): O caminho do arquivo que contém o texto que será impresso.
    A função recebe o caminho do arquivo txt e testa se o arquivo existe. Se o arquivo existir a função lê o arquivo e imprime ele em vermelho.
    """


    if not os.path.isfile(caminho):
        print("O arquivo não existe")
    else:
        with open (caminho, "r") as arquivo:
            texto =arquivo.read()
            Console().print(texto,style="red")



