# AveDex

A AveDex é um catálogo interativo de aves desenvolvido na disciplina de
Boas Práticas de Programação.

## Como executar

```bash
python main.py
```
## Estrutura do projeto

- `main.py`: inicia o programa.
- `src/avedex/app.py`: controla o fluxo principal.
- `src/avedex/interface.py`: mostra abertura e menu.
- `src/avedex/dados.py`: carrega o dataset JSON.
- `src/avedex/catalogo.py`: lista, busca e mostra detalhes.
- `src/avedex/comparacao.py`: compara duas aves.
- `src/avedex/creditos.py`: mostra informações e fontes.
- `src/avedex/utils.py`: reúne funções auxiliares.
- `data/avedex_dataset_midias.json`: dados das aves.

## Testes manuais realizados em 03/08

- [x] Execução com `python main.py`
- [x] Carregamento das aves pelo JSON
- [x] Listagem das aves
- [x] Busca textual
- [x] Detalhes por ID
- [x] Comparação entre aves
- [x] Créditos e fontes
- [x] Encerramento do programa