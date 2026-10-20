lista_itens = []

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
    
        while True:
            entrada_codigo = input("Digite o código de identificação do item: ").strip()

            if not entrada_codigo.isdigit():
                print("DIGITE APENAS NÚMEROS.")
                continue

            codigo = int(entrada_codigo)

            if codigo_item_existe(codigo):
                print("Já existe um item com esse código.")
                continue

            break

        while True:
            nome = input("Digite o nome do item: ").strip()

            if nome == "":
                print("O nome não pode ficar vazio.")
                continue

            break

        while True:
            categoria = input("Digite a categoria do item: ").strip()

            if categoria == "":
                print("A categoria não pode ficar vazia.")
                continue

            break

        while True:
            estado = input("Digite o estado atual do item: ").strip()

            if estado == "":
                print("O estado não pode ficar vazio.")
                continue

            break

        item = {
            "codigo": codigo,
            "nome": nome,
            "categoria": categoria,
            "estado": estado,
            "disponivel": True,
            "quantidade_emprestimos": 0
        }

        lista_itens.append(item)
        print("Item adicionado com sucesso!")

def codigo_item_existe(codigo):
    for item in lista_itens:
        if item["codigo"] == codigo:
            return True
    return False

          
def listar_item(escolha):
    if escolha == 2:
        if len(lista_itens) == 0:
            print("Nenhum item cadastrado.")
            return
        
        for item in lista_itens:
            situacao = "Disponível" if item["disponivel"] else "Emprestado"

            print (30 * "=")
            print(f"Código: {item['codigo']}")
            print(f"Nome: {item['nome']}")
            print(f"Categoria: {item['categoria']}")
            print(f"Estado: {item['estado']}")
            print(f"Disponibilidade: {item['disponivel']}")
            print(f"Quantidade de empréstimos: {item['quantidade_emprestimos']}")
            print (30 * "=")
            
        
menu_start()
escolha_start()
