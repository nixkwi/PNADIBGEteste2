# Pandas é a biblioteca utilizada para criar a planilha em um arquivo csv a ser lido pelo excel
import principal
import pandas
from pathlib import Path

# Chama a função do arquivo principal para extrair todas variaveis do arquivo "dicionario_pessoas.xls"
variaveis = principal.extrair_variaveis("dados/dicionario_pessoas.xls")

# Cada varivael servirá como o titulo de uma coluna no arquivo csv final
colunas = [str(variavel) for variavel in variaveis]
# Cada linha será uma lista aninhada contendo um valor para cada celula na tabela (coluna)
linhas = []

# Abre o arquivo texto contendo os microdados a serem lidos e transformados
with open("dados/pessoas_2015.txt") as microdados:

    # Enumera as linhas como index para permitir limitação do tamanho do csv a ser feito
    for idx, linha in enumerate(microdados):
        nova_linha = []
        for variavel in variaveis:

            # Pega o valor numerico a ser traduzido
            valor = linha[variavel.posicao_inicial:variavel.posicao_inicial + variavel.tamanho].strip()
            if valor:

                # Transforma o valor de string para int
                valor = int(valor)

            # Traduz o valor, o utilizando como chave no dicionario categoria
            # Caso nao haja algo atribuido aquela chave se usa o valor numerico como traduzido
            valor_traduzido = variavel.categoria.get(valor) if variavel.categoria.get(valor) else valor

            # Adiciona o valor traduzido a lista de nova linha
            nova_linha.append(valor_traduzido)

        # Adiciona a lista "nova_linha" aninhada na lista "linhas"
        linhas.append(nova_linha)

        # Limita o programa a rodar somente 1000 linhas
        if idx > 1000:
            break

# Variavel contendo o path para o desktop do usuario
desktop_dir = Path.home() / "Desktop"

# Cria o DataFrame (tabela/planilha) utilizando a Lista de linhas e de colunas
df = pandas.DataFrame(linhas, columns=colunas)

# Printa a quantidade de linhas e colunas geradas ao executar o programa
print(df.shape)

# Transforma esse DataFrame em um arquivo csv na Area de trabalho
df.to_csv(rf'{desktop_dir}\microdados_traduzidos.csv', sep=';')

