import funcoes

while True:
    print("Escolha uma opção:")
    print("1. Cenourinha GPT")
    print("2. Consultar Clima")
    print("3. Recomendação por Época")
    print("4. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        funcoes.cenourinha_gpt()
    elif opcao == "2":
        funcoes.get_clima()
    elif opcao == "3":
        funcoes.recomendacao_por_epoca()
    elif opcao == "4":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")

