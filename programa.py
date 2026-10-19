# Estela Mariano - RM569513
# Gabriela Labrada - RM569849
import subalgoritmos as sub
import os

os.system("cls")

id = ""
livros = {}

# PRINCIPAL
while True:
    sub.exibir_menu()

    try:
        escolha = int(input("Escolha: "))

        match escolha:
            case 0:
                print("Saindo do sistema ...")
                break

            case 1:
                sub.limpar_tela()

                while True:
                    id = sub.pedir_id(id)

                    if id == "":
                        print("Cadastro encerrado.")
                        break

                    if sub.verificar_id(id):
                        print("Esse ID já está cadastrado!")

                    else:
                        nome, nome_autor, obs, nota = sub.pedir_info()

                        livros[id] = {
                            "nome": nome,
                            "nome_autor": nome_autor,
                            "obs": obs,
                            "nota": nota
                        }

                        sub.gravar_livros(livros, id)

                        print("Livro cadastrado com sucesso!")

                sub.continuar()
                sub.limpar_tela()

            case 2:
                sub.limpar_tela()
                sub.exibir_submenu()

                try:
                    opcao = int(input("Escolha: "))

                    match opcao:
                        case 1:
                            sub.limpar_tela()
                            sub.ler_txt()
                            sub.continuar()

                        case 2:
                            sub.limpar_tela()
                            sub.ler_csv()
                            sub.continuar()

                        case 3:
                            sub.limpar_tela()
                            sub.ler_json()
                            sub.continuar()

                        case 4:
                            sub.limpar_tela()
                            sub.ler_excel()
                            sub.continuar()

                        case _:
                            sub.limpar_tela()
                            print("Digite um valor válido!")
                            sub.continuar()

                except ValueError:
                    print("Digite um número!")

                except:
                    print("Ocorreu um erro!")

            case 3:
                while True:
                    id = input("Informe o ID do livro (pressione ENTER vazio para voltar ao menu anterior): ")
                    if id == "":
                        print("Pesquisa encerrada.")
                        break
                    sub.pesquisar_id(id)
                    sub.continuar()
                    sub.limpar_tela()

            case _:
                sub.limpar_tela()
                print("Digite um valor válido!")
                sub.continuar()

    except ValueError:
        print(30 * "-")
        print("Digite um número!")
        print(30 * "-")
        sub.continuar()

    except:
        print(30 * "-")
        print("Ocorreu um erro!")
        print(30 * "-")
        sub.continuar()