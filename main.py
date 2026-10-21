lista_itens = []
lista_usuarios = []


def menu_start():
    print(20 * "=")
    print("ESCOLHA UMA OPÇÃO: ")
    print(20 * "=")
    print("0 - Encerrar")
    print("1 - Cadastrar item")
    print("2 - Listar itens")
    print("3 - Cadastrar usuário")
    print("4 - Listar usuários")
    print(20 * "=")

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
        elif escolha == 3: 
            cadastrar_usuario(escolha)
        elif escolha == 4:
            listar_usuarios(escolha)
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


def cadastrar_usuario(escolha):
    if escolha == 3:
        while True:
            codigo_entrada = input("Digite o código de identificação do usuário: ").strip()
            if not codigo_entrada.isdigit():
                print("DIGITE APENAS NÚMEROS!")
                continue

            codigo_usuario = int (codigo_entrada) 

            if codigo_usuario_existe(codigo_usuario):
                print("Já existe um usuário com esse código.")   
                continue

            break

        while True:
            nome_usuario = input("Digite o nome do usuário: ").strip()
            if nome_usuario == "":
                print("O nome não pode ficar vazio.")
                continue
            break

        while True:
            telefone_usuario = input("Digite o telefone do usuário: ")
            if telefone_usuario == "":
                print("O telefone não pode ficar vazio")
                continue

            if not telefone_usuario.isdigit() or len(telefone_usuario) not in (10,11):
                print("Digite um telefone com DDD, contendo 10 ou 11 números.")
            break

        usuario_ativo = True

        usuario = {
            "codigo" : codigo_usuario,
            "nome" : nome_usuario,
            "telefone" : telefone_usuario,
            "ativo" : usuario_ativo
        }

        lista_usuarios.append(usuario)
        print("Usuário cadastro com sucesso!")

def codigo_item_existe(codigo):
    for item in lista_itens:
        if item["codigo"] == codigo:
            return True
    return False

def codigo_usuario_existe(codigo_usuario):
    for usuario in lista_usuarios:
        if usuario["codigo"] == codigo_usuario:
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
            print(f"Disponibilidade: {item['situacao']}")
            print(f"Quantidade de empréstimos: {item['quantidade_emprestimos']}")
            print (30 * "=")


def listar_usuarios(escolha):
    if escolha == 4:

        if len(lista_usuarios) == 0:
            print("Nenhum usuário foi cadastrado!")
            return
        
        for usuario in lista_usuarios:
            situacao = "Sim" if usuario["ativo"] else "Não"

            print(30 * "=")
            print(f"Código: {usuario['codigo']}" )
            print(f"Nome: {usuario['nome']}" )
            print(f"Telefone: {usuario['telefone']}" )
            print(f"Ativo: {usuario['situacao']}" )
            print(30 * "=")

        

escolha_start()
