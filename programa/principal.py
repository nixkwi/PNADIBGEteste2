# xlrd é a biblioteca que lê e manipula arquivos .xls (formato antigo do excel)
import xlrd
from modelos import Variavel


# Função que será chamada para extrair os objetos "Variavel" do dicionario
def extrair_variaveis(dicionario):
    # open_workbook() é para abrir a planilha, e sheet_by_index(0) é para pegar a primeira ABA (sheet) da planilha
    planilha = xlrd.open_workbook(dicionario)
    primeira_aba = planilha.sheet_by_index(0)

    variaveis = []
    nova_variavel = None

    # get_rows() é um generator que cada iteração retorna uma linha da aba, um dicionario com o conteudo de cada celula
    # enumerate() é utilizado para contar a quantidade de linhas para poder limitar o programa à quantidade desejada
    for idx, linha in enumerate(primeira_aba.get_rows()):
        primeira_celula = linha[0]

        # Linha 22: verifica o tipo da primeira celula, toda vez que a primeira celula é do tipo "number" significa que
        #       é uma nova variavel, entao para detectar novas variaveis basta verificar o tipo da primeira celula
        if primeira_celula.ctype == 2:

            # Atribui nova_variavel a lista de variaveis a partir da segunda iteração, quando for diferente de None
            if nova_variavel:
                variaveis.append(nova_variavel)

            # Variaveis contendo os valores para serem utilizados no construtor do objeto "Variavel"
            posicao_inicial = linha[0].value
            tamanho = linha[1].value
            codigo = linha[2].value
            descricao = linha[4].value

            # Cosntroi a nova variavel com os valores de cada celula útil (0-1-2-4)
            nova_variavel = Variavel(posicao_inicial, tamanho, codigo, descricao)

            # Variaveis contendo os valores do atributo "categoria" a ser adicionado no objeto "Variavel"
            # Linha 40 e 41: Pega o tipo da categoria e sua descrição, se for do tipo numero
            #    transforma a variavel em int, e se não for numero, pega do jeito que está (String)
            categoria_tipo = int(linha[5].value) if linha[5].ctype == 2 else linha[5].value
            categoria_descricao_tipo = int(linha[6].value) if linha[6].ctype == 2 else linha[6].value

            # Adiciona as variaveis anteriores ao dicionario "categoria" do objeto "Variavel"
            nova_variavel.add_categoria({'categoria_tipo': categoria_tipo,
                                         'categoria_descricao_tipo': categoria_descricao_tipo})
        else:
            # O atributo "categoria" do objeto "Variavel" é um dicionario com distintos tipos e descrições, onde cada
            #   linha terá o mesmo valor nas celulas 0-1-2-4. Esse bloco else pega todos valores da categoria de uma
            #   variavel antes de passar para a próxima.

            # Checa se ja existe uma variavel, para evitar o cabeçalho da planilha
            if nova_variavel:
                if primeira_celula.ctype == 0:  # 0 = Nulo
                    categoria_tipo = int(linha[5].value) if linha[5].ctype == 2 else linha[5].value
                    categoria_descricao_tipo = int(linha[6].value) if linha[6].ctype == 2 else linha[6].value
                    nova_variavel.add_categoria({'categoria_tipo': categoria_tipo,
                                                 'categoria_descricao_tipo': categoria_descricao_tipo})
        if idx > 100:
            break

    return variaveis
