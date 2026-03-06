from Estoque_v1.app.crud import create
from Estoque_v1.app.crud import read
from Estoque_v1.app.crud import delete
import Estoque_v1.app.crud as crud
import Estoque_v1.app.func as func


while True:
    print('''GERENCIADOR DE ESTOQUE
        Digite o que deseja realizar:
        1- Adicionar ao estoque um novo piso
        2- Listar todos os pisos do estoque
        3- Atualizar um dado específico como a chegada de um carregamento
        4- Deletar um piso do estoque
        5- Sair do sistema de estoque

        ''') 
    num = input("")
    
    if num == "1": #Escolha 1, adicionar
        func.titulo("ADICIONAR")
        print("Adicione o nome do lote de piso que deseja adicionar:")
        nome = input("") #Adiconando o nome
        func.limpar()

        while True: #Tipo
            func.titulo("ADICIONAR")
            print("Adicione o tipo deste lote de piso: ")
            tipo = input("") #O tipo
            if tipo != "A" and tipo != "B" and tipo != "C": #Caso o usuario digitar um tipo fora do padrão
                print("Valor inválido, adicione apenas o A, B ou C")
                func.pausa()
                func.limpar()
            else:
                func.limpar()
                break
        
        func.titulo("ADICIONAR")
        print("Adicione a cor do piso: ") #Cor
        cor = input("")
        func.limpar()

        while True: #Quantidade de caixas chegando do novo piso
            func.titulo("ADICIONAR")
            print("Adicione a quantidade de caixas deste lote de piso: ")
            try:
                quantidade = int(input(""))
                func.limpar()
                break
            except ValueError:
                print("Letras ou simbolos encontrados, digite apenas a numeração correta de caixa")
                func.pausa()
                func.limpar()

        while True: #Quantidade de metros por caixa deste novo piso
            func.titulo("ADICIONAR")
            print("Adicione a quantidade de metros por caixa deste lote de piso: ")
            try:
                metros = int(input(""))
                func.limpar()
                break
            except ValueError:
                print("Metros inválidos, digite apenas a numeração em metros sem simbolos ou letras")
                func.pausa()
                func.limpar()
        
        while True: #Data de entrada, não foi adicionado a ultima data de saída por ser um novo piso, afinal acabou de entrar
            func.titulo("ADICIONAR")
            print("Adicione a data (DD/MM/AAA) de entrada deste novo lote de piso: ")
            data_entrada = input("Digite a data: ")
            try:
                func.data(data_entrada)
                func.limpar()
                break
            except ValueError:
                print("Data invalida, digite corretamente a data (DD/MM/AAAA)")
                func.pausa()
                func.limpar()

        while True: #Valor por caixa
            func.titulo("ADICIONAR")
            print("Adicione o valor por caixa deste lote de piso: ")
            valor = float(input(""))
            try:
                valor
                func.limpar()
                break
            except ValueError:
                print("Valor invalido, digite apenas numeros")
                func.pausa()
                func.limpar()

        dados = (nome, tipo, cor, quantidade, metros, data_entrada, valor) #Definindo a ordem dos valores para adicionar
        create(dados) # Adicionando ao banco de dados

    elif num == "2": #Listar
        while True:
            func.limpar()
            func.titulo("LISTAR")
            for lista in read():
                print(f'''
                |ID: {lista[0]}|
Nome: {lista[1]}
tipo: {lista[2]}
cor: {lista[3]}
quantidade de caixas: {lista[4]}
Metros por caixa: {lista[5]}
Data entrada: {lista[6]}
data saída: {lista[7]}
valor por caixa: {lista[8]}
''')
            input("Digite Enter para sair")
            func.limpar()
            break

    elif num == "3":
        while True:
            func.titulo("ATUALIZAR")
            print('''Escolha se deseja adicionar a data de saída ou atualizar algum valor:

1- Atualizar nome
2- Atualizar tipo
3- Atualizar cor
4- Atualizar quantidade de caixas
5- Atualizar metros por caixa
6- Atualizar data de entrada
7 Atualizar a data de saída
8 Atualizar o valor da caixa
''')
            escolha = input("")

            if escolha == "1":
                try:
                    id = int(input("Digite o id do piso onde deseja atualizar: "))
                    atualizar = input("Digite o nome do piso para atualizar: ")
                    
                except ValueError:
                    print("Valor inválido")
                    func.pausa()
                    func.limpar()
                    continue
                    
                update = (atualizar, id)
                crud.update(update)
                func.pausa()
                func.limpar()
                break

            elif escolha == "2":
                try:
                    id = int(input("Digite o id do piso onde deseja atualizar: "))
                    atualizar = input("Digite o tipo do piso para atualizar: ")
                except ValueError:
                    print("Valor inválido")
                    func.pausa()
                    func.limpar()
                    continue
                
                if atualizar != "A" and atualizar != "B" and atualizar != "C": #Caso o usuario digitar um tipo fora do padrão
                    print("Valor inválido, adicione apenas o A, B ou C")
                    func.pausa()
                    func.limpar()
                else:
                    update = (atualizar, id)
                    crud.update_type(update)
                    func.pausa()
                    func.limpar()
                    break

            elif escolha == "3":
                try:
                    id = int(input("Digite o id do piso onde deseja atualizar: "))
                    atualizar = input("Digite o cor do piso para atualizar: ")
                except ValueError:
                    print("Valor inválido")
                    func.pausa()
                    func.limpar()
                    continue
                update = (atualizar, id)
                crud.update_color(update)
                func.pausa()
                func.limpar()
                break

            elif escolha == "4":
                try:
                    id = int(input("Digite o id do piso onde deseja atualizar: "))
                    atualizar = int(input("Digite a quantidade de caixas que deseja do piso para atualizar: "))
                except ValueError:
                    print("Valor inválido")
                    func.pausa()
                    func.limpar()
                    continue
                update = (atualizar, id)
                crud.update_box(update)
                func.pausa()
                func.limpar()
                break

            elif escolha == "5":
                try:
                    id = int(input("Digite o id do piso onde deseja atualizar: "))
                    atualizar = int(input("Digite o  metros por caixa do piso para atualizar: "))
                except ValueError:
                    print("Valor inválido")
                    func.pausa()
                    func.limpar()
                    continue

                update = (atualizar, id)
                crud.update_meters(update)
                func.pausa()
                func.limpar()
                break

            elif escolha == "6":
                try:
                    id = int(input("Digite o id do piso onde deseja atualizar: "))
                    atualizar = input("Digite a data de entrada do piso para atualizar: ")
                    func.data(atualizar)
                except ValueError:
                    print("Valor inválido")
                    func.pausa()
                    func.limpar()
                    continue

                update = (atualizar, id)
                crud.update_entry(update)
                func.pausa()
                func.limpar()
                break

            elif escolha == "7":
                try:
                    id = int(input("Digite o id do piso onde deseja atualizar: "))
                    atualizar = input("Digite a data de saída do piso para atualizar: ")
                except ValueError:
                    print("Valor inválido")
                    func.pausa()
                    func.limpar()

                update = (atualizar, id)
                crud.update_depar(update)
                func.pausa()
                func.limpar()
                break

            elif escolha == "8":
                try:
                    id = int(input("Digite o id do piso onde deseja atualizar: "))
                    atualizar = float(input("Digite o valor do piso que deseja atualizar: "))
                except ValueError:
                    print("Valor inválido")
                    func.pausa()
                    func.limpar()

                update = (atualizar, id)
                crud.update_value(update)
                func.pausa()
                func.limpar()
                break
                

    elif num == "4":
        while True:
            func.titulo("DELETAR")
            try:
                deletar = int(input("Digite o id do piso que deseja deletar: "))
                delete((deletar,))
            except ValueError:
                print("Valor invalido")
                func.pausa()
                func.limpar()
                continue

            func.limpar()
            break
  
    elif num == "5": #Sair do sistema
        func.sair()
        break

    else:
        print("Valor invalido")
        func.pausa()
        func.limpar()