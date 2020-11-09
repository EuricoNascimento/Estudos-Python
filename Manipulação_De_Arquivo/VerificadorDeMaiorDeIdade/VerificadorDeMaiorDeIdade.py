# Codigo que verifica se uma pessoa: é maior de idade, está entrando na maior idade ou se ela ainda não nasceu.
# O formato dos dados é: <Nome da pessoa>;<data de nascimento (dd/mm/aaaa)>

try:
    ano = int(input('Digite o ano atual: '))
    arquivo_entrada = input('Digite o arquivo de entrada: ')
    arquivo_saida = input('Digite o arquivo de saida: ')
    with open(arquivo_entrada, 'r') as arqen:
        with open(arquivo_saida, 'w') as arqsa:
            for dados in arqen:
                # A variavel armazena_dados armazena a linha dos depois de ser convertida
                # em string e depois armazena a lista só da data
                armazena_dados = dados.split(';')
                armazena_dados = armazena_dados[1].split('/')
                # Remove as quebras de linhas
                if not armazena_dados[2].isalpha():
                    armazena_dados[2].replace("\n", "")
                idade = ano - int(armazena_dados[2])
                if idade <= 0:
                    arqsa.write(f'{dados.split(";")[0]};Essa pessoa ainda não nasceu\n')
                elif idade < 18:
                    arqsa.write(f'{dados.split(";")[0]};Menor de idade\n')
                elif idade == 18:
                    arqsa.write(f'{dados.split(";")[0]};Entrando na maior idade\n')
                else:
                    arqsa.write(f'{dados.split(";")[0]};Maior de idade\n')
except ValueError:
    print('Erro: Não foi digitado um numero', )
except FileNotFoundError:
    print(f'Erro: Arquivo {arquivo_entrada} não existe')
except FileExistsError:
    print(f'Erro: Arquivo {arquivo_saida} já existe')
