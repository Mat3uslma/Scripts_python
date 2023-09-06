import os, shutil

print("########### MENU #############")
print("")
print("10- CRIAR PASTA "
      "20-REMOVER PASTA "
      "30- REMOVER SOMENTE ARQUIVOS "
      "40- LISTAR DIREORIO"
      )
print("")

Funcao = int (input(" Qual Função deseja Ultilizar ? "))


if Funcao == 10:
    print("1 PARA CRIAR A PASTA 5 PARA FECHAR A APLICAÇÃO")
    def Criar_pasta():
        while True:
            option = int(input("Digite um numero ? "))
            if option == 1:
                os.mkdir(input("Digite o nome para pasta : "))
                print("PASTA CRIADA COM SUCESSO")
            elif option != 3 or option != 5:
                print("Digite uma Opção Valida !!")

    Criar_pasta()

elif Funcao == 20:
    print("2 PARA REMOVER PASTA 5 PARA FECHAR A APLICAÇÃO ? ")
    def Remover_pasta():
        while True:
            option = int(input("Digite um numero ? "))
            if option == 2:
                shutil.rmtree(input("Digite o nome da pasta ? "))
                print("PASTA REMOVIDA COM SUCESSO")
            elif option == 5:
                break
            elif option != 3 or option != 5:
                print("Digite uma Opção Valida !!")

    Remover_pasta()
elif Funcao == 30:
    print("3 PARA REMOVER ARQUIVOS 5 PARA FECHAR A APLICAÇÃO ? ")
    def Remover_arquivos():
        while True:
            option = int(input("Digite um numero ? "))
            if option == 3:
                os.remove(input("Digite o nome do arquivo ? "))
                print("ARQUIVOS REMOVIDOS COM SUCESSO")
            elif option == 5:
                break
            elif option != 3 or option != 5:
                print("Digite uma Opção Valida !!")
    Remover_arquivos()

elif Funcao == 40:
    print("4 PARA LISTAR DIRETORIOS 5 PARA FECHAR A APLICAÇÃO ? ")
    def Listar_diretorio():
        while True:
            option = int(input("Digite um numero ? "))
            if option == 4:
                list_diretorio = os.listdir()
                print(list_diretorio)
            elif option == 5:
                break
            elif option != 3 or option != 5:
                print("Digite uma Opção Valida !!")
    Listar_diretorio()