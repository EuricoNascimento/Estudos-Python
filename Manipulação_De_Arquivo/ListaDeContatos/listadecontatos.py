# Codigo que cria uma lista de contatos

with open("listadecontatos.txt", "a") as arquivo:
    telefone = " "
    while telefone != "0":
        telefone = input("Digite o contato (se quiser sair, digite '0'): ")
        if telefone != "0":
            nomedocontato = input("Digite o nome do contato: ")
            arquivo.write(f'Nome: {nomedocontato}; Contato: {telefone}\n')
