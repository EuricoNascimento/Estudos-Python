# O objetivo do codigo é contar as palavras, letras e os paragrafos de um determinado texto


def countletter(text):
    # Conta as letras
    count = 0
    for letra in text:
        if letra != " ":
            count += 1
    print(f"O texto tem {count} letras")


def countword(text):
    # Conta as palavras de um texto, removendo possiveis strings vazias ("" ou " ")
    # Que possam ser formadas atraves do split
    auxiliar = []
    for palavra in text.split(" "):
        if palavra != " " and palavra != "":
            auxiliar.append(palavra)
    print(f"O texto tem {len(auxiliar)} palavras")


def remove(arq):
    # Remove as pontuações, quebra de textos e numeros lendo o paragrafo do texto e verificando, trocando
    # por espaço e acrescentando na variavel text
    text = ""
    for paragrafo in arq:
        auxiliar = paragrafo
        for ponto in """?!,.;:(){}[]%'"><+=-_\\*&$#@1234567890\n""":
            auxiliar = auxiliar.replace(ponto, " ")
        text += auxiliar
    return text


try:
    with open("LoremImpsu.txt", "r") as arquivo:
        print(f"O texto tem {len(arquivo.readlines())} paragrafo")
        arquivo.seek(0)
        texto = remove(arquivo)
        countword(texto)
        countletter(texto)
except FileNotFoundError:
    print("Arquivo não existe")
