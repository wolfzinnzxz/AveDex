# Testes manuais da AveDex

## Execução

- [x] O projeto executa com `python main.py`.
- [x] O dataset JSON é carregado corretamente.
- [x] O dataset JSON é validado antes da abertura do menu.
- [x] O menu principal aparece corretamente.
- [x] A opção `0` encerra o programa.

## Catálogo

- [x] A opção 1 lista as aves.
- [x] A listagem possui paginação.
- [x] É possível avançar para a próxima página.
- [x] É possível voltar para a página anterior.
- [x] A listagem permite selecionar uma ave pelo ID.
- [x] A opção 2 busca por parte do nome.
- [x] A opção 2 busca por família.
- [x] A opção 2 busca por ordem.
- [x] A opção 2 busca por dieta.
- [x] A busca ignora diferenças entre maiúsculas e minúsculas.
- [x] A busca ignora acentos.
- [x] Uma busca sem resultados mostra um aviso.
- [x] A opção 3 sorteia uma ave aleatoriamente.
- [x] A opção 4 mostra detalhes completos por ID.
- [x] O programa trata ID inexistente.
- [x] O programa trata letras no lugar do ID.
- [x] O programa permite cancelar uma seleção com ENTER.

## Comparação

- [x] A opção 5 compara duas aves existentes.
- [x] A comparação mostra as informações das duas aves.
- [x] A comparação mostra família, dieta, peso e comprimento.
- [x] A comparação trata ID inexistente.
- [x] A comparação impede a seleção da mesma ave duas vezes.

## Batalha AveDex

- [x] A opção 6 abre a Batalha AveDex.
- [x] É possível escolher a primeira ave.
- [x] É possível escolher a segunda ave.
- [x] A batalha permite escolher comprimento.
- [x] A batalha permite escolher peso médio.
- [x] A batalha permite escolher índice de conservação.
- [x] O maior comprimento vence a rodada.
- [x] O maior peso médio vence a rodada.
- [x] O maior índice de conservação vence a rodada.
- [x] A batalha identifica empate.
- [x] A mesma ave não pode batalhar contra ela própria.
- [x] Atributos sem valor numérico válido são tratados com aviso.

## Imagem, som e cache

- [x] A opção 7 permite escolher uma ave para visualizar a imagem.
- [x] Uma ave com `imagem_url` válida consegue baixar a imagem.
- [x] A imagem baixada é armazenada em `cache_midias/`.
- [x] Uma segunda utilização reaproveita a imagem existente no cache.
- [x] Uma ave sem `imagem_url` mostra um aviso.
- [x] A ausência de `term-image` não encerra o programa.
- [x] Sem `term-image`, o caminho da imagem salva é informado.
- [x] A opção 8 permite escolher uma ave para ouvir o som.
- [x] Uma ave com `som_url` válida consegue baixar o som.
- [x] O som baixado é armazenado em `cache_midias/`.
- [x] Uma segunda utilização reaproveita o som existente no cache.
- [x] Uma ave sem `som_url` mostra um aviso.
- [x] A ausência de `pygame` não encerra o programa.
- [x] Sem `pygame`, o caminho do som salvo é informado.
- [ ] Uma falha de conexão mostra uma mensagem clara sem encerrar a aplicação.

## Interface

- [x] A abertura da AveDex é exibida corretamente.
- [x] O banner da AveDex aparece corretamente.
- [x] A abertura mostra a quantidade de aves carregadas.
- [x] O menu aparece dentro de uma caixa visual.
- [x] Os títulos estão padronizados.
- [x] As mensagens de sucesso estão padronizadas.
- [x] As mensagens de aviso estão padronizadas.
- [x] As mensagens de erro estão padronizadas.
- [x] As cores da interface são exibidas corretamente no terminal.
- [x] A tela é limpa entre as operações quando o terminal oferece suporte.

## Ambiente

- [x] A opção 9 verifica o ambiente.
- [x] A verificação informa se `requests` está instalada.
- [x] A verificação informa se `pygame` está instalada.
- [x] A verificação informa se `term-image` está instalada.
- [x] A ausência de uma dependência opcional não impede o funcionamento do núcleo da AveDex.

## Créditos

- [x] A opção 10 abre os créditos e fontes.
- [x] As fontes do dataset são apresentadas corretamente.

## Dados e validação

- [x] O JSON é carregado corretamente.
- [x] O programa identifica JSON ausente.
- [x] O programa identifica JSON mal formatado.
- [x] O programa identifica campo obrigatório ausente.
- [x] O programa identifica ID duplicado.
- [x] O programa identifica campo numérico inválido.
- [x] O programa trata dados de mídia ausentes.
- [x] O programa trata campos opcionais ausentes sem encerrar.

## Boas práticas

A AveDex foi testada tanto em situações normais quanto em situações de erro.

Na multimídia, devem ser considerados principalmente os seguintes cenários:

- URL de imagem vazia;
- URL de som vazia;
- biblioteca opcional ausente;
- falha de conexão;
- arquivo já existente no cache;
- terminal sem suporte para exibição de imagens.

As funcionalidades externas devem apresentar mensagens claras ao usuário sem encerrar a aplicação inteira.