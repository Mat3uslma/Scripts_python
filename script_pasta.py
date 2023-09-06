import os, shutil

print("########### MENU #############")
print("")
print("1- CRIAR PASTA "
      "2-REMOVER PASTA "
      "3- REMOVER SOMENTE ARQUIVOS "
      "4- FECHAR MENU "
      "5- LISTAR DIREORIO"
      )
print("")
def menu():
    while True:
        try:
            option = int(input("Digite um numero ? "))
            if option == 1:
                os.mkdir(input("Digite o nome para pasta a ser criada : "))
                print("PASTA CRIADA COM SUCESSO")
            elif option == 2:
                shutil.rmtree(input("Digite o nome da pasta a ser removida ? "))
                print("PASTA REMOVIDA COM SUCESSO")
            elif option == 3:
                os.remove(input("Digite o nome do arquivo a ser removido? "))
                print("ARQUIVO REMOVIDO COM SUCESSO")
            elif option == 5:
                listar_diretorio = os.listdir()
                print(listar_diretorio)
            elif option == 4:
                break

            elif option != 3 or option != 2 or option != 1 or option != 5:
                print("ERRO DIGITE UMA OPÇÃO VALIDA !! ")
        except ValueError :
            print("Por favor Digite somente numeros nessa etapa da aplicação")

menu()


teste