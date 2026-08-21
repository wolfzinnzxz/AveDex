# AveDex

A **AveDex** é um catálogo interativo de aves desenvolvido na disciplina de **Boas Práticas de Programação**.

O projeto utiliza um arquivo JSON como fonte de dados e possui recursos para consulta, comparação, batalha, visualização de imagens, reprodução de sons e validação das informações das aves.

## Funcionalidades

- Listagem de aves com paginação;
- Busca textual sem diferenciar acentos ou maiúsculas;
- Detalhes completos das aves por ID;
- Seleção de aves por ID;
- Ave aleatória;
- Comparação entre duas aves;
- Batalha AveDex por atributos numéricos;
- Download de imagens e sons;
- Cache local das mídias baixadas;
- Tentativa de exibição de imagens no terminal;
- Reprodução de sons das aves;
- Validação defensiva do dataset;
- Verificação das dependências do ambiente;
- Créditos e fontes utilizadas no projeto;
- Tratamento de erros durante leitura, download e reprodução de mídias.

## Como executar

Na raiz do projeto, instale as dependências:

```bash
pip install -r requirements.txt
````

Depois execute:

```bash
python main.py
```

Os recursos centrais da AveDex funcionam sem as bibliotecas opcionais.

Os recursos de imagem, som e download dependem das bibliotecas presentes no arquivo `requirements.txt`.

## Estrutura do projeto

* `main.py`: ponto de entrada da aplicação;
* `src/avedex/app.py`: fluxo principal e integração do menu;
* `src/avedex/catalogo.py`: listagem, busca, seleção, detalhes e ave aleatória;
* `src/avedex/comparacao.py`: comparação entre duas aves;
* `src/avedex/batalha.py`: batalha por atributos numéricos;
* `src/avedex/multimidia.py`: download, cache, visualização de imagens e reprodução de sons;
* `src/avedex/interface.py`: abertura e menu principal;
* `src/avedex/dados.py`: carregamento e validação do dataset;
* `src/avedex/ambiente.py`: verificação das dependências opcionais;
* `src/avedex/creditos.py`: informações, créditos e fontes;
* `src/avedex/utils.py`: funções auxiliares compartilhadas;
* `data/avedex_dataset_midias.json`: dataset com os dados das aves;
* `cache_midias/`: mídias baixadas, criada automaticamente;
* `requirements.txt`: dependências opcionais do projeto;
* `docs/testes_manuais.md`: roteiro dos testes manuais.

## Dataset

Os dados das aves são armazenados no arquivo:

```text
data/avedex_dataset_midias.json
```

O dataset contém informações como:

* nome popular;
* nome científico;
* ordem;
* família;
* tipo de dieta;
* comprimento;
* peso médio;
* status de conservação;
* índice de conservação;
* descrição;
* habitat;
* alimentação;
* curiosidades;
* informações de mídia.

A AveDex também realiza uma validação do dataset antes de iniciar o menu principal.

## Cache de mídias

As imagens e os sons baixados são armazenados automaticamente na pasta:

```text
cache_midias/
```

Quando uma mídia já foi baixada anteriormente, a aplicação reutiliza o arquivo local em vez de realizar um novo download.

A pasta de cache não deve ser enviada ao Git, pois os arquivos podem ser baixados novamente quando necessário.

## Batalha AveDex

A Batalha AveDex permite escolher duas aves e comparar um atributo numérico.

Os atributos disponíveis são:

* **Comprimento:** vence a ave com maior comprimento;
* **Peso médio:** vence a ave com maior peso;
* **Índice de conservação:** vence o maior índice.

O índice de conservação representa o nível de atenção necessário para conservação da espécie. Portanto, um índice maior **não significa que uma ave seja melhor ou mais forte**.

## Testes

Os testes manuais realizados durante o desenvolvimento estão documentados em:

```text
docs/testes_manuais.md
```

Entre os testes realizados estão:

* [x] JSON carregado corretamente;
* [x] Arquivo JSON ausente;
* [x] JSON mal formatado;
* [x] Campo obrigatório ausente;
* [x] ID duplicado;
* [x] Campo numérico inválido;
* [x] Entrada inválida no ID;
* [x] Busca sem diferenciar acentos;
* [x] Paginação do catálogo;
* [x] Seleção de ave por ID;
* [x] Ave aleatória;
* [x] Comparação entre aves;
* [x] Batalha AveDex;
* [x] Verificação do ambiente;
* [x] Download e cache de mídias;
* [x] Ausência de URL de mídia;
* [x] Falha de download;
* [x] Reprodução de som;
* [x] Visualização de imagem.

## Boas práticas utilizadas

O projeto aplica conceitos de boas práticas de programação, incluindo:

* Organização do código em módulos;
* Separação de responsabilidades;
* Funções com responsabilidades específicas;
* Reutilização de funções;
* Uso de constantes;
* Validação dos dados antes da execução;
* Tratamento defensivo de entradas;
* Tratamento de erros;
* Tratamento de dependências opcionais;
* Uso de cache para evitar downloads desnecessários;
* Normalização de textos para facilitar buscas;
* Nomes seguros para arquivos de cache;
* Documentação do projeto por meio do README.

## Dependências opcionais

A AveDex utiliza algumas bibliotecas para recursos adicionais:

* `requests`: download de imagens e sons;
* `pygame`: reprodução de sons;
* `term-image`: exibição de imagens no terminal.

A situação dessas bibliotecas pode ser consultada pela opção **Verificar ambiente** no menu principal.

Para instalar todas as dependências:

```bash
pip install -r requirements.txt
```

## Execução

Depois de instalar as dependências, execute:

```bash
python main.py
```

O menu principal disponibiliza:

```text
1 - Listar aves
2 - Buscar ave
3 - Ave aleatória
4 - Ver detalhes de uma ave
5 - Comparar duas aves
6 - Batalha AveDex
7 - Visualizar imagem de uma ave
8 - Tocar som de uma ave
9 - Verificar ambiente
10 - Créditos e fontes
0 - Sair
```