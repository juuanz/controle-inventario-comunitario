lista_itens = ['mesa']

def menu_start():
    print(20 * "=")
    print("ESCOLHA UMA OPÇÃO: ")
    print(20 * "=")
    print("0 - Encerrar")
    print("1 - Cadastrar item")
    print("2 - Listar itens")
    
    

def escolha_start():
    while True:
        menu_start()

        try:
            escolha = int(input("OPÇÃO DESEJADA: "))
        except ValueError:
            print("DIGITE APENAS NÚMEROS.")
            continue

        if escolha == 0:
            encerrar(escolha)
            break
        elif escolha == 1:
            cadastro_item(escolha)
        elif escolha == 2:
            listar_item(escolha)
        else:
            print("OPÇÃO INVÁLIDA.")
      
    


def encerrar(escolha):
    if escolha == 0:
        print("Sistema encerrado!")
        return

def cadastro_item(escolha):
    if escolha == 1:
        nome = str(input("Digite o nome do item: ")).strip()

        if nome == "":
            print("O nome não pode ficar vazio.")
            return
        
        lista_itens.append(nome)
        print("Item adicionado com sucesso!")
        
        

def listar_item(escolha):
    if escolha == 2:
        if len(lista_itens) == 0:
            print("Nenhum item cadastrado.")
            return
        
        for item in lista_itens:
            print (item)
        

menu_start()
escolha_start()
