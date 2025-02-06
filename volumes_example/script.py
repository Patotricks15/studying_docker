import os

def listar_arquivos(diretorio):
    # Lista os arquivos e pastas presentes no diretório
    itens = os.listdir(diretorio)
    if not itens:
        print(f"Empty directory: '{diretorio}'")
    else:
        print(f"Files in '{diretorio}':")
        for item in itens:
            print(item)
            return item

def ler_saida(caminho):
    with open(caminho, 'r') as arquivo:
        conteudo = arquivo.read()
    return conteudo


caminho = '/app/dados'
arquivo = listar_arquivos(caminho)
print(ler_saida(caminho+'/'+arquivo))