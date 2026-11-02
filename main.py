import json
from datetime import date, timedelta
from busca_ordenacao import busca_sequencial, ordenar_insercao, busca_binaria

def carregar_dados():
    with open("data/data.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

        return dados

dados = carregar_dados()

lista_itens = dados["itens"]
lista_usuarios = dados ["usuarios"]
lista_emprestimos = dados ["emprestimos"]
lista_reservas = dados ["reservas"]


def menu_start():
    print(20 * "=")
    print("ESCOLHA UMA OPÇÃO: ")
    print(20 * "=")
    print("0 - Encerrar")
    print("1 - Cadastrar item")
    print("2 - Listar itens")
    print("3 - Cadastrar usuário")
    print("4 - Listar usuários")
    print("5 - Realizar empréstimo")
    print("6 - Listar empréstimos")
    print("7 - Buscar item por código")
    print("8 - Listar itens ordenados por código")
    print("9 - Buscar item com busca binária")
    print("10 - Ranking de itens mais emprestados")
    print("11 - Exibir relatório")
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
        elif escolha == 5:
            realizar_emprestimo(escolha)
        elif escolha == 6:
            listar_emprestimos(escolha)
        elif escolha == 7:
            buscar_item(escolha)
        elif escolha == 8:
            listar_itens_ordenados(escolha)
        elif escolha == 9:
            buscar_item_binario(escolha)
        elif escolha == 10:
            ranking_itens(escolha)
        elif escolha == 11:
            exibir_relatorio(escolha)
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
            nome = input("Digite o nome do item: ").strip().capitalize()

            if nome == "":
                print("O nome não pode ficar vazio.")
                continue

            break

        while True:
            categoria = input("Digite a categoria do item: ").strip().capitalize()

            if categoria == "":
                print("A categoria não pode ficar vazia.")
                continue

            break

        while True:
            estado = input("Digite o estado atual do item: ").strip().capitalize()

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
        salvar_dados(dados)
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
            nome_usuario = input("Digite o nome do usuário: ").strip().capitalize()
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
                continue
            
            break   

        usuario_ativo = True

        usuario = {
            "codigo" : codigo_usuario,
            "nome" : nome_usuario,
            "telefone" : telefone_usuario,
            "ativo" : usuario_ativo
        }

        lista_usuarios.append(usuario)
        salvar_dados(dados)
        print("Usuário cadastro com sucesso!")

def realizar_emprestimo(escolha):
    if escolha == 5:
        while True:
            codigo_entrada = input("Digite o código de identificação do empréstimo: ").strip()
            if not codigo_entrada.isdigit():
                print("Digite apenas números nesse campo!")
                continue

            codigo_emprestimo = int(codigo_entrada)

            if codigo_emprestimo_existe(codigo_emprestimo):
                print("Código não disponível, tente novamente!")
                continue

            break

        while True:
            codigo_entrada_usuario = input("Digite o código do usuário que vai realizar o empréstimo: ").strip()
            if not codigo_entrada_usuario.isdigit():
                print("Digite apenas números nesse campo!")
                continue

            codigo_usuario = int(codigo_entrada_usuario)
            usuario = buscar_usuario_por_codigo(codigo_usuario)

            if usuario is None:
                print("Usuário não encontrado!")
                continue

            if not usuario["ativo"]:
                print("Usuário inativo!")
                continue

            break

        while True:
            codigo_entrada_item = input("Digite o código do item que procura: ").strip()
            if not codigo_entrada_item.isdigit():
                print("Digite apenas números nesse campo!")
                continue

            codigo_item = int(codigo_entrada_item)
            item = buscar_item_por_codigo(codigo_item)

            if item is None:
                print("O código/item não foi encontrado!")
                continue

            if not item["disponivel"]:
                print("O item não está disponível para empréstimo!")
                continue

            break

        data_emprestimo = date.today()
        data_prevista_devolucao = data_emprestimo + timedelta(days=7)

        emprestimo = {
            "codigo": codigo_emprestimo,
            "codigo_usuario": codigo_usuario,
            "codigo_item": codigo_item,
            "data_emprestimo": data_emprestimo.isoformat(),
            "data_prevista_devolucao": data_prevista_devolucao.isoformat(),
            "data_devolucao": None,
            "status": "ativo"
        }

        lista_emprestimos.append(emprestimo)
        item["disponivel"] = False
        item["quantidade_emprestimos"] += 1
        salvar_dados(dados)

        print("Empréstimo realizado com sucesso!")
        print(f"Devolução prevista para: {data_prevista_devolucao.isoformat()}")

def codigo_emprestimo_existe(codigo_emprestimo):
    for codigo in lista_emprestimos:
        if codigo["codigo"] == codigo_emprestimo: 
            return True
    return False

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

def buscar_usuario_por_codigo(codigo_usuario):
    for usuario in lista_usuarios:
        if usuario["codigo"] == codigo_usuario:
            return usuario
    return None


def buscar_item_por_codigo(codigo):
    for item in lista_itens:
        if item["codigo"] == codigo:
            return item
    return None

def buscar_item(escolha):
    if escolha == 7:
        entrada_codigo = input("Digite o código do item que deseja buscar: ").strip()

        if not entrada_codigo.isdigit():
            print("Digite apenas números nesse campo!")
            return

        codigo = int(entrada_codigo)
        posicao, comparacoes = busca_sequencial(lista_itens, codigo)

        if posicao == -1:
            print("Item não encontrado!")
            print(f"Comparações realizadas: {comparacoes}")
            return

        item = lista_itens[posicao]
        situacao = "Disponível" if item["disponivel"] else "Emprestado"

        print(30 * "=")
        print(f"Código: {item['codigo']}")
        print(f"Nome: {item['nome']}")
        print(f"Categoria: {item['categoria']}")
        print(f"Estado: {item['estado']}")
        print(f"Disponibilidade: {situacao}")
        print(f"Comparações realizadas: {comparacoes}")
        print(30 * "=")

def buscar_item_binario(escolha):
    if escolha == 9:
        entrada_codigo = input("Digite o código do item que deseja buscar: ").strip()

        if not entrada_codigo.isdigit():
            print("Digite apenas números nesse campo!")
            return

        codigo = int(entrada_codigo)
        itens_ordenados = ordenar_insercao(lista_itens, "codigo")
        posicao, comparacoes = busca_binaria(itens_ordenados, codigo)

        if posicao == -1:
            print("Item não encontrado!")
            print(f"Comparações realizadas: {comparacoes}")
            return

        item = itens_ordenados[posicao]
        situacao = "Disponível" if item["disponivel"] else "Emprestado"

        print(30 * "=")
        print(f"Código: {item['codigo']}")
        print(f"Nome: {item['nome']}")
        print(f"Categoria: {item['categoria']}")
        print(f"Estado: {item['estado']}")
        print(f"Disponibilidade: {situacao}")
        print(f"Comparações realizadas: {comparacoes}")
        print(30 * "=")


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
            print(f"Disponibilidade: {situacao}")
            print(f"Quantidade de empréstimos: {item['quantidade_emprestimos']}")
            print (30 * "=")

def listar_itens_ordenados(escolha):
    if escolha == 8:
        if len(lista_itens) == 0:
            print("Nenhum item cadastrado.")
            return

        itens_ordenados = ordenar_insercao(lista_itens, "codigo")

        for item in itens_ordenados:
            situacao = "Disponível" if item["disponivel"] else "Emprestado"

            print(30 * "=")
            print(f"Código: {item['codigo']}")
            print(f"Nome: {item['nome']}")
            print(f"Categoria: {item['categoria']}")
            print(f"Estado: {item['estado']}")
            print(f"Disponibilidade: {situacao}")
            print(f"Quantidade de empréstimos: {item['quantidade_emprestimos']}")
            print(30 * "=")

def ranking_itens(escolha):
    if escolha == 10:
        if len(lista_itens) == 0:
            print("Nenhum item cadastrado.")
            return

        itens_ordenados = ordenar_insercao(lista_itens, "quantidade_emprestimos")[::-1]
        posicao = 1

        for item in itens_ordenados:
            print(30 * "=")
            print(f"{posicao}º lugar")
            print(f"Código: {item['codigo']}")
            print(f"Nome: {item['nome']}")
            print(f"Quantidade de empréstimos: {item['quantidade_emprestimos']}")
            print(30 * "=")
            posicao += 1

def exibir_relatorio(escolha):
    if escolha == 11:
        total_itens = len(lista_itens)
        total_usuarios = len(lista_usuarios)
        total_emprestimos = len(lista_emprestimos)
        itens_disponiveis = 0
        usuarios_ativos = 0
        emprestimos_ativos = 0
        quantidade_emprestimos = 0

        for item in lista_itens:
            if item["disponivel"]:
                itens_disponiveis += 1

            quantidade_emprestimos += item["quantidade_emprestimos"]

        for usuario in lista_usuarios:
            if usuario["ativo"]:
                usuarios_ativos += 1

        for emprestimo in lista_emprestimos:
            if emprestimo["status"] == "ativo":
                emprestimos_ativos += 1

        itens_emprestados = total_itens - itens_disponiveis

        if total_itens > 0:
            media_emprestimos = quantidade_emprestimos / total_itens
        else:
            media_emprestimos = 0

        print(30 * "=")
        print("RELATÓRIO DO SISTEMA")
        print(30 * "=")
        print(f"Total de itens: {total_itens}")
        print(f"Itens disponíveis: {itens_disponiveis}")
        print(f"Itens emprestados: {itens_emprestados}")
        print(f"Total de usuários: {total_usuarios}")
        print(f"Usuários ativos: {usuarios_ativos}")
        print(f"Total de empréstimos registrados: {total_emprestimos}")
        print(f"Empréstimos ativos: {emprestimos_ativos}")
        print(f"Média de empréstimos por item: {media_emprestimos:.2f}")
        print(30 * "=")


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
            print(f"Ativo: {situacao}")
            print(30 * "=")

def listar_emprestimos(escolha):
    if escolha == 6:
        if len(lista_emprestimos) == 0:
            print("Nenhum empréstimo foi cadastrado!")
            return

        for emprestimo in lista_emprestimos:
            usuario = buscar_usuario_por_codigo(emprestimo["codigo_usuario"])
            item = buscar_item_por_codigo(emprestimo["codigo_item"])

            nome_usuario = usuario["nome"] if usuario is not None else "Usuário não encontrado"
            nome_item = item["nome"] if item is not None else "Item não encontrado"

            print(30 * "=")
            print(f"Código: {emprestimo['codigo']}")
            print(f"Usuário: {nome_usuario}")
            print(f"Item: {nome_item}")
            print(f"Data do empréstimo: {emprestimo['data_emprestimo']}")
            print(f"Devolução prevista: {emprestimo['data_prevista_devolucao']}")
            print(f"Status: {emprestimo['status'].capitalize()}")
            print(30 * "=")

def salvar_dados(dados):
    with open("data/data.json", "w", encoding="utf-8") as arquivo:        
        json.dump(dados, arquivo, ensure_ascii=False, indent=2)


escolha_start()
