# PNADIBGEteste2
#### Curto programa em Python para manipular os microdados de uma pesquisa PNAD feita em 2015 pelo IBGE que está em formato .txt e transforma-lo em um arquivo CSV que pode ser lido e interpretado.
---
## *Organização dos microdados e como traduzi-los:*

Existem 2 arquivos de microdados:


O primeiro arquivo está em formato .txt, contendo conjuntos de números que são chamados de Variáveis, estas agem como códigos que apontam para o valor traduzido em texto da informação. 

O segundo arquivo está no formato .xls (excel), que contém uma planilha do Dicionario necessário para a tradução das Variavéis em informação legível.

### O dicionario funciona assim:

![Screenshot 2024-04-10 142600](https://github.com/nixkwi/PNADIBGEteste2/assets/140534789/473bad40-5001-4b73-9a12-dcadc468e541)

- A primeira coluna contém a posição inicial, que é onde está o primeiro número da variável contando da esquerda para a direita.
- A segunda coluna informa o tamanho da variável, isto é, quantas casas decimais ela ocupa na linha.
- A quarta coluna informa a descrição da variável, qual informação está contida nela.

Neste exemplo o próprio valor numerico ja é a informação de "Ano de referencia".

### Veja como é representado no arquivo .txt:

![Screenshot 2024-04-10 163302](https://github.com/nixkwi/PNADIBGEteste2/assets/140534789/f117f1a7-2e69-4085-9720-a37d61a8a240) 

_Como mostrado no dicionario, a posição inicial é 1, portanto começa no primeiro numero da linha. O tamanho é 4, então está incluso os proximos 3 digitos na linha. O valor numérico encontrado é 2015, que é descrito como o "Ano de referência"._

Neste exemplo, a informação ("Ano de referência" = "2015") já é contida dentro do valor numérico da variável (2015), porém, na maioria das variavéis, existe a necessidade do atributo "categoria", onde é verificado uma série de possiveis valores para a variável, onde cada valor traduz para uma informação diferente.

### Veja, por exemplo, a variavel referente a "Unidade da Federação":
![image_2024-04-11_140803073](https://github.com/nixkwi/PNADIBGEteste2/assets/140534789/6ecbbeac-9364-419b-a148-c8cb90fc6ceb)

- A quinta coluna chamada "Categorias" possui as colunas de "Tipo" e "Descrição" aninhadas dentro de si.
- A coluna "Tipo" refere ao valor numerico achado no arquivo txt, variando entre alguns números de 11 a 53.
- A coluna "Descrição" contém a informação em texto a ser retirada do valor numérico, onde cada número aponta para um estado do Brasil.

### Novamente, a representação dentro do arquivo de microdados .txt:
![image_2024-04-11_142010942](https://github.com/nixkwi/PNADIBGEteste2/assets/140534789/6844fb77-ebc4-4597-b703-9168343e6c23)

_A posição inicial 5 nos informa que o primeiro digito se encontra na quinta posição da linha da esquerda para a direita. Tamanho 2 significa que ocupa duas casas decimais, com isso achamos o valor numérico 11, que por si só não significa nada, mas utilizando o dicionario e procurando no atributo "Categorias" obtemos a informação de que o código "11" equivale a "Rondônia"._

E assim, traduzimos parte dos valores numericos da primeira linha em informações textuais legíveis e uteis.

O Script em Python não só automatiza essa tradução para todas variaveis em todas linhas, mas também gera um arquivo .csv organizado em formato de planilha que pode ser vizualizado em ferramentas de gerenciamento de informações e dados como Excel e Power BI.

A explicação do código Python é feita linha a linha por meio de comentários.

---
## *Como baixar os dados e rodar o programa:*

#### Primeiro verifique os *requisitos* :
- OS: Windows 7 ou superior / Linux Ubuntu ou Derivados de Debian.
- Python 3.10 ou superior instalado em sua maquina (caso não tenha, navegue até Files em [Python Org](https://www.python.org/downloads/release/python-3100/)).
- pip instalado.
- 512mb de espaço livre (pessoas_2015.txt pesa em torno de 330mb).



### 1- Vá em [releases](https://github.com/nixkwi/PNADIBGEteste2/releases) e baixe o arquivo .zip ou .tar.
![image_2024-04-11_195128293](https://github.com/nixkwi/PNADIBGEteste2/assets/140534789/dea36e4b-104b-449b-89e5-402b63758ad6)

### 2- Extraia o arquivo em uma pasta
![image 2024-04-11 198293832](https://github.com/nixkwi/PNADIBGEteste2/assets/140534789/ca7439c7-f547-476c-9bab-3f6c1f1db763)

### 3- *WINDOWS:* Entre na pasta extraída e clique no path do diretório, localizado na parte superior do Explorador de Arquivos, digite "cmd" e pressione enter para abrir o terminal:
![imagem2](https://github.com/nixkwi/PNADIBGEteste2/assets/140534789/cb3d2505-0bce-473e-82b3-7a45ec335127) ![imagem3](https://github.com/nixkwi/PNADIBGEteste2/assets/140534789/b4c8648b-6961-44e2-8073-fa4a3f397d9e)

### 4- No terminal digite o comando "py pip install -r requirements.txt";
![imagem 5](https://github.com/nixkwi/PNADIBGEteste2/assets/140534789/cf33ade7-6886-458c-96f2-f9332b63d08e)
### Essa deverá ser a mensagem de êxito de instalação retornada:
![imagem 6](https://github.com/nixkwi/PNADIBGEteste2/assets/140534789/cc9dc124-2b2a-413d-829f-c8f99afbbce4)

### 5- Ainda no terminal, logo após a instalação dos requisitos, digite o comando "cd programa" para mover a pasta contendo os scripts e "py extracao.py" para executar o script que fará a extração do arquivo.csv diretamente a área de trabalho.
![imagem 7](https://github.com/nixkwi/PNADIBGEteste2/assets/140534789/b58dd6b5-88fc-4517-8acc-2548e8397e2c)
#### Caso tudo dê certo, a mensagem exibida no terminal deve ser "(1002, 21)" {Numero de linhas e colunas no arquivo .csv gerado}
#### E um arquivo csv deve ter sido criado no desktop:
![imagem 8](https://github.com/nixkwi/PNADIBGEteste2/assets/140534789/5bf182dd-dfed-4dbd-a102-b014516be8a7)

---


# Resultado Final
![imagem 9](https://github.com/nixkwi/PNADIBGEteste2/assets/140534789/bf6e269f-0e71-4d1c-86bd-4b11bd19b742)
> Planilha do Excel após importar o arquivo microdados_traduzidos.csv como dados e tranforma-los em uma tabela.
