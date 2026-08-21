# AveDex

A **AveDex** é um catálogo interativo de aves desenvolvido na disciplina de **Boas Práticas de Programação**.

O projeto utiliza um arquivo JSON como fonte de dados e possui recursos para consulta, comparação e validação das informações das aves.

## Funcionalidades

* Listagem de aves
* Busca por nome, família, ordem ou dieta
* Exibição de detalhes por ID
* Comparação entre duas aves
* Dados carregados de arquivo JSON
* Validação defensiva do dataset
* Verificação de ambiente e dependências
* Tratamento de erros na leitura do dataset

## Como executar

Na raiz do projeto, execute:

```bash
python main.py
```

## Instalação das dependências opcionais

As dependências opcionais estão listadas no arquivo `requirements.txt`.

Para tentar instalar todas:

```bash
pip install -r requirements.txt
```

> **Observação:** algumas dependências podem exigir uma versão compatível do Python para instalação.

## Estrutura do projeto

* `main.py`: ponto de entrada da aplicação.
* `src/avedex/app.py`: menu e fluxo principal.
* `src/avedex/interface.py`: abertura e menu principal.
* `src/avedex/catalogo.py`: listagem, busca e exibição de detalhes das aves.
* `src/avedex/comparacao.py`: comparação entre duas aves.
* `src/avedex/dados.py`: carregamento, leitura e validação do JSON.
* `src/avedex/ambiente.py`: verificação das dependências do ambiente.
* `src/avedex/creditos.py`: informações e fontes utilizadas no projeto.
* `src/avedex/utils.py`: funções auxiliares utilizadas pela aplicação.
* `data/avedex_dataset_midias.json`: dataset com os dados das aves.
* `requirements.txt`: dependências opcionais do projeto.
* `docs/testes_manuais.md`: documentação dos testes manuais.

## Testes

Os testes manuais realizados durante o desenvolvimento estão documentados em:

`docs/testes_manuais.md`

## Boas práticas utilizadas

O projeto aplica conceitos de boas práticas de programação, incluindo:

* Organização do código em módulos.
* Separação de responsabilidades.
* Funções com responsabilidades específicas.
* Validação dos dados antes da execução da aplicação.
* Tratamento de erros na leitura do arquivo JSON.
* Entrada de dados mais defensiva.
* Uso de constantes para campos obrigatórios.
* Documentação do projeto por meio do README.