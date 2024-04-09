# Classe contendo todos atributos que interessam de uma Variavel
class Variavel:

    # Construtor da classe, que recebe e atribui todos valores importantes desejados para a extração
    def __init__(self, posicao_inicial, tamanho, codigo, descricao):

        # No arquivo .xls a contagem começa no 1, porém o primeiro char da string é de index 0, por isso o "-1"
        self.posicao_inicial = int(posicao_inicial) - 1
        self.tamanho = int(tamanho)
        self.codigo = codigo
        self.descricao = descricao
        self.categoria = {}

    # Função para adicionar uma categoria no dicionario de categoria
    def add_categoria(self, categoria):
        self.categoria[categoria.get('categoria_tipo')] = categoria.get('categoria_descricao_tipo')

    def __str__(self):
        return f'{self.codigo} - {self.descricao}'

