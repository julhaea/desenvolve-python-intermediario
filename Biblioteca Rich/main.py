from personalizador import estilo, painel, layout, progresso
import os
import argparse

modulos = {'estilo': estilo,'1': estilo,'layout': layout,'2': layout,'painel': painel, '3': painel,'progresso': progresso,'4': progresso
}

funcoes = {'bold': 'bold','red': 'red', 'estrofes':"estrofes", 'colunas':'colunas','borda':'borda','titulo':'titulo','ler5seg':'ler5seg','inverter':'inverter'
}

# Função para imprimir o texto ou arquivo com a função escolhida
def imprimirtxt(texto, arquivo, modulo, funcao):
    if arquivo:
        if os.path.isfile(texto):
            with open(texto, 'r') as f:
                conteudo = f.read()
        else:
            print("Erro: O caminho do arquivo não existe.")
            return
    else:
        conteudo = texto
    
    mod = modulos.get(modulo)
    func = getattr(mod, funcao, None)


    func(conteudo)



def funcao():
    parser = argparse.ArgumentParser()

    # Argumento do caminho do txt
    parser.add_argument(
        'texto',
        type=str,
        help="Caminho do arquivo que vai ser impresso."
    )

    
    parser.add_argument(
        '-a', '--arquivo',
        action='store_true',
        help="Testa se o argumento é caminho para um arquivo."
    )

    # Escolhe o módulo
    parser.add_argument(
        '-m', '--modulo',
        type=str,
        choices=['estilo', 'layout', 'painel', 'progresso', '1', '2', '3', '4'],
        required=True,
        help="Escolhe o módulo a ser usado. Pode ser: estilo (1), layout (2), painel (3), progresso (4)."
    )

    # Escolhe a função
    parser.add_argument(
        '-f', '--funcao',
        type=str,
        choices=list(funcoes.keys()),
        required=True,
        help="Escolhe a função do módulo."
    )

    args = parser.parse_args()

   
    imprimirtxt(args.texto, args.arquivo, args.modulo, args.funcao)


if __name__ == '__main__':
    funcao()