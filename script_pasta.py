import os, shutil


def Criar_pasta():
    os.mkdir(input("Digite o nome para pasta : "))
    print("PASTA CRIADA COM SUCESSO")


def Criar_subpastas():
    os.makedirs(input("Digite o caminho da pasta onde quer criar ? "))
    print("PASTA CRIADA COM SUCESSO")


def Remover_pasta():
    while True:
        shutil.rmtree(input("Digite o nome da pasta ? "))
        print("PASTA REMOVIDA COM SUCESSO")


def Remover_arquivos():
    while True:
        os.remove(input("Digite o nome do arquivo ? "))
        print("ARQUIVOS REMOVIDOS COM SUCESSO")


def Listar_diretorio():
    while True:
        list_diretorio = os.listdir()
        print(list_diretorio)

def Tamanho_Arquivo():
    Tamanho = os.path.getsize(input("Digite o nome do arquivo que quer verificar o tamanho  ? "))
    print(Tamanho, "Bytes")


def main():
    while True:
        try:
            print("########### MENU #############")
            print("")
            print("INFORMAÇÕES DE DIRETÓRIOS")
            print("1- CRIAR PASTA ")
            print("2- CRIAR PASTAS COM SUBPASTAS DENTRO ")
            print("3- REMOVER PASTA ")
            print("4- REMOVER SOMENTE ARQUIVOS ")
            print("5- LISTAR DIREtORIOs ")
            print("6- CALCULAR TAMANHO DE UM ARQUIVO")
            print("10- FECHAR APLICAÇÃO")
            print("")
            print("")

            resp = int(input("Escolha  uma Opção ?  "))
            if resp == 1:
                Criar_pasta()
            elif resp == 2:
                Criar_subpastas()
            elif resp == 3:
                Remover_pasta()
            elif resp == 4:
                Remover_arquivos()
            elif resp == 5:
                Listar_diretorio()
            elif resp == 6:
                Tamanho_Arquivo()
            elif resp == 10:
                break
        except ValueError :
            print("Por favor Digite um numero correto !!")


main()