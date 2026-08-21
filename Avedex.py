import unicodedata


# ============================================================
# CONSTANTES
# ============================================================

LARGURA_TELA = 78

OPCOES_MENU = [
    "1 - Listar aves",
    "2 - Buscar ave",
    "3 - Ver detalhes de uma ave",
    "4 - Comparar duas aves",
    "5 - Sobre a AveDex",
    "0 - Sair"
]

CAMPOS_BUSCA = [
    "nome_popular",
    "nome_cientifico",
    "familia",
    "ordem",
    "dieta_tipo"
]

CAMPOS_COMPARACAO = [
    ("Nome científico", "nome_cientifico", ""),
    ("Ordem", "ordem", ""),
    ("Família", "familia", ""),
    ("Dieta", "dieta_tipo", ""),
    ("Habitat", "habitat", ""),
    ("Comprimento", "comprimento_cm", "cm"),
    ("Peso", "peso_g", "g"),
    ("Conservação", "status_conservacao", ""),
    ("Índice", "indice_conservacao", "")
]


# ============================================================
# FUNÇÕES AUXILIARES DE EXIBIÇÃO
# ============================================================

def linha(caractere="=", largura=LARGURA_TELA):
    # Retorna uma linha formada pela repetição de um caractere.
    return caractere * largura


def titulo(texto):
    # Exibe um título padronizado.
    print()
    print(linha("="))
    print(texto)
    print(linha("="))


def mensagem_aviso(texto):
    # Exibe uma mensagem simples de aviso.
    print(f"[AVISO] {texto}")


def mensagem_sucesso(texto):
    # Exibe uma mensagem de sucesso padronizada.
    print(f"[SUCESSO] {texto}")


# ============================================================
# MENU PRINCIPAL
# ============================================================

def exibir_menu():
    # Exibe o título do menu.
    titulo("AVEDEX - MENU PRINCIPAL")

    # Percorre a lista de opções e imprime uma por uma.
    for opcao in OPCOES_MENU:
        print(opcao)


# ============================================================
# FUNÇÕES DE BUSCA
# ============================================================

def normalizar_texto(texto):
    texto = str(texto)
    texto = texto.lower().strip()

    texto = unicodedata.normalize("NFD", texto)

    texto = "".join(
        caractere
        for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )

    return texto


def criar_texto_busca(ave):
    # Lista temporária que guardará os valores dos campos pesquisáveis.
    valores = []

    # Percorre cada campo definido em CAMPOS_BUSCA.
    for campo in CAMPOS_BUSCA:
        # Busca o valor do campo no dicionário da ave.
        # Se o campo não existir, usa texto vazio.
        valores.append(str(ave.get(campo, "")))

    # Junta todos os valores em um único texto.
    texto = " ".join(valores)

    # Normaliza o texto para facilitar a busca.
    return normalizar_texto(texto)


def buscar_aves(catalogo, termo_busca):
    # Lista que receberá as aves encontradas.
    resultados = []

    # Normaliza o termo digitado pelo usuário.
    termo = normalizar_texto(termo_busca)

    # Percorre todas as aves.
    for ave in catalogo:
        # Cria o texto pesquisável da ave.
        texto_busca = criar_texto_busca(ave)

        # Se o termo estiver no texto, adiciona a ave aos resultados.
        if termo in texto_busca:
            resultados.append(ave)

    return resultados


def buscar_ave_por_id(catalogo, id_procurado):
    for ave in catalogo:
        if str(ave["id"]) == id_procurado:
            return ave

    return None


# ============================================================
# FUNÇÕES DE FORMATAÇÃO
# ============================================================

def valor_ou_indisponivel(valor, unidade=""):
    if valor is None or valor == "":
        return "Não informado"

    if unidade != "":
        return f"{valor} {unidade}"

    return str(valor)


def cortar_texto(texto, tamanho=25):
    # Se o texto não existir, retornamos uma mensagem padrão.
    if texto is None:
        return "Não informado"

    # Garantimos que o valor será tratado como texto.
    texto = str(texto).strip()

    # Se o texto já couber no tamanho definido, retornamos sem alteração.
    if len(texto) <= tamanho:
        return texto

    # Se for longo demais, cortamos e adicionamos reticências.
    return texto[: tamanho - 3] + "..."


def preparar_valor_comparacao(ave, campo, unidade):
    # Busca o valor original da ave.
    valor = ave.get(campo)

    # Habitat costuma ser longo, então cortamos para não quebrar a tabela.
    if campo == "habitat":
        return cortar_texto(valor, 25)

    # Os demais campos usam a função padrão.
    return valor_ou_indisponivel(valor, unidade)


# ============================================================
# LISTAGEM DE AVES
# ============================================================

def listar_aves(catalogo):
    titulo("AVES CADASTRADAS")

    for ave in catalogo:
        print(f"{ave['id']} - {ave['nome_popular']}")


# ============================================================
# EXIBIÇÃO DE DETALHES
# ============================================================

def exibir_detalhes_ave(ave):
    titulo("DETALHES DA AVE")

    print(f"ID: {ave['id']}")
    print(f"Nome popular: {ave['nome_popular']}")
    print(f"Nome científico: {ave['nome_cientifico']}")
    print(f"Ordem: {ave['ordem']}")
    print(f"Família: {ave['familia']}")
    print(f"Dieta: {ave['dieta_tipo']}")
    print(f"Habitat: {ave['habitat']}")

    print(
        f"Comprimento: "
        f"{valor_ou_indisponivel(ave.get('comprimento_cm'), 'cm')}"
    )

    print(
        f"Peso: "
        f"{valor_ou_indisponivel(ave.get('peso_g'), 'g')}"
    )

    print(
        f"Status de conservação: "
        f"{ave.get('status_conservacao', 'Não informado')}"
    )

    print(
        f"Índice de conservação: "
        f"{ave.get('indice_conservacao', 'Não informado')}"
    )

    print(f"Alimentação: {ave['alimentacao']}")

    print(
        f"Curiosidade: "
        f"{ave.get('curiosidade', 'Não informada')}"
    )


def selecionar_ave_por_id(catalogo):
    ave_encontrada = escolher_ave(catalogo, "Digite o ID da ave")

    if ave_encontrada is not None:
        exibir_detalhes_ave(ave_encontrada)


# ============================================================
# TELA DE BUSCA
# ============================================================

def exibir_resultados_busca(resultados):
    titulo("RESULTADOS DA BUSCA")

    if len(resultados) == 0:
        mensagem_aviso("Nenhuma ave encontrada.")
    else:
        print(f"Quantidade de resultados: {len(resultados)}")
        print()

        for ave in resultados:
            print(
                f"{ave['id']} - {ave['nome_popular']} "
                f"({ave['familia']}, {ave['dieta_tipo']})"
            )


def tela_busca(catalogo):
    termo = input(
        "Digite parte do nome, família, ordem ou dieta: "
    ).strip()

    if termo == "":
        mensagem_aviso("Digite algum texto para realizar a busca.")
        return

    resultados = buscar_aves(catalogo, termo)

    exibir_resultados_busca(resultados)

    if len(resultados) > 0:
        escolha = input(
            "\nDigite o ID para ver detalhes ou ENTER para voltar: "
        ).strip()

        if escolha != "":
            ave_encontrada = buscar_ave_por_id(
                resultados,
                escolha
            )

            if ave_encontrada is None:
                mensagem_aviso("ID não encontrado nos resultados.")
            else:
                exibir_detalhes_ave(ave_encontrada)


# ============================================================
# COMPARAÇÃO
# ============================================================

def imprimir_linha_comparacao(rotulo, valor_1, valor_2):
    print(
        f"{rotulo:<18} | "
        f"{str(valor_1):<25} | "
        f"{str(valor_2):<25}"
    )


def exibir_comparacao_aves(ave_1, ave_2):
    # Cabeçalho da comparação.
    titulo("COMPARAÇÃO ENTRE AVES")

    # Primeira linha com o nome das aves.
    imprimir_linha_comparacao(
        "Campo",
        ave_1["nome_popular"],
        ave_2["nome_popular"]
    )

    print(linha("-"))

    # Percorre todos os campos configurados em CAMPOS_COMPARACAO.
    for rotulo, campo, unidade in CAMPOS_COMPARACAO:
        # Obtém e prepara o valor da primeira ave.
        valor_1 = preparar_valor_comparacao(
            ave_1,
            campo,
            unidade
        )

        # Obtém e prepara o valor da segunda ave.
        valor_2 = preparar_valor_comparacao(
            ave_2,
            campo,
            unidade
        )

        # Imprime a linha já formatada.
        imprimir_linha_comparacao(
            rotulo,
            valor_1,
            valor_2
        )


def escolher_ave(catalogo, mensagem):
    listar_aves(catalogo)

    id_escolhido = input(
        f"\n{mensagem}: "
    ).strip()

    ave_encontrada = buscar_ave_por_id(
        catalogo,
        id_escolhido
    )

    if ave_encontrada is None:
        mensagem_aviso("Ave não encontrada. Confira o ID informado.")
        return None

    return ave_encontrada


def comparar_duas_aves(catalogo):
    print()
    print("Escolha a primeira ave")

    ave_1 = escolher_ave(
        catalogo,
        "Digite o ID da primeira ave"
    )

    if ave_1 is None:
        return

    print()
    print("Escolha a segunda ave")

    ave_2 = escolher_ave(
        catalogo,
        "Digite o ID da segunda ave"
    )

    if ave_2 is None:
        return

    exibir_comparacao_aves(ave_1, ave_2)


# ============================================================
# OUTRAS FUNÇÕES
# ============================================================

def mostrar_sobre():
    print("A AveDex é um catálogo interativo de aves.")
    print(
        "Em breve, teremos batalha, imagens, sons "
        "e dados em arquivo JSON."
    )


def pausar():
    input("\nPressione ENTER para voltar ao menu...")


# ============================================================
# CATÁLOGO DE AVES
# ============================================================

catalogo_aves = [
    {
        "id": 1,
        "nome_popular": "Bem-te-vi",
        "nome_cientifico": "Pitangus sulphuratus",
        "ordem": "Passeriformes",
        "familia": "Tyrannidae",
        "dieta_tipo": "Onívora",
        "habitat": "Áreas abertas, cidades e bordas de florestas",
        "comprimento_cm": 23,
        "peso_g": 68,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,
        "alimentacao": "Insetos, frutos e pequenos animais",
        "curiosidade": "Seu canto parece dizer o próprio nome."
    },
    {
        "id": 2,
        "nome_popular": "João-de-barro",
        "nome_cientifico": "Furnarius rufus",
        "ordem": "Passeriformes",
        "familia": "Furnariidae",
        "dieta_tipo": "Insetívora",
        "habitat": "Campos, cidades e áreas rurais",
        "comprimento_cm": 20,
        "peso_g": 49,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,
        "alimentacao": "Insetos e outros invertebrados",
        "curiosidade": "É conhecido por construir ninhos de barro."
    },
    {
        "id": 3,
        "nome_popular": "Canário-da-terra",
        "nome_cientifico": "Sicalis flaveola",
        "ordem": "Passeriformes",
        "familia": "Thraupidae",
        "dieta_tipo": "Granívora",
        "habitat": "Campos e áreas abertas",
        "comprimento_cm": 13,
        "peso_g": 20,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,
        "alimentacao": "Sementes e pequenos insetos",
        "curiosidade": "Possui canto forte e melodioso."
    },
    {
        "id": 4,
        "nome_popular": "Arara-azul",
        "nome_cientifico": "Anodorhynchus hyacinthinus",
        "ordem": "Psittaciformes",
        "familia": "Psittacidae",
        "dieta_tipo": "Granívora",
        "habitat": "Pantanal, cerrado e áreas de mata",
        "comprimento_cm": 100,
        "peso_g": 1500,
        "status_conservacao": "Vulnerável",
        "indice_conservacao": 3,
        "alimentacao": "Frutos, sementes e castanhas",
        "curiosidade": "É uma das maiores espécies de arara do mundo."
    },
    {
        "id": 5,
        "nome_popular": "Tucano-toco",
        "nome_cientifico": "Ramphastos toco",
        "ordem": "Piciformes",
        "familia": "Ramphastidae",
        "dieta_tipo": "Onívora",
        "habitat": "Cerrados, florestas e áreas abertas",
        "comprimento_cm": 56,
        "peso_g": 540,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,
        "alimentacao": "Frutas, insetos e pequenos animais",
        "curiosidade": "Possui um grande bico que ajuda na alimentação."
    },
    {
        "id": 6,
        "nome_popular": "Sabiá-laranjeira",
        "nome_cientifico": "Turdus rufiventris",
        "ordem": "Passeriformes",
        "familia": "Turdidae",
        "dieta_tipo": "Onívora",
        "habitat": "Florestas, jardins, parques e áreas urbanas",
        "comprimento_cm": 25,
        "peso_g": 75,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,
        "alimentacao": "Frutos, sementes e pequenos animais",
        "curiosidade": "É conhecido pelo canto melodioso."
    },
    {
        "id": 7,
        "nome_popular": "Beija-flor-tesoura",
        "nome_cientifico": "Eupetomena macroura",
        "ordem": "Apodiformes",
        "familia": "Trochilidae",
        "dieta_tipo": "Nectarívora",
        "habitat": "Jardins, áreas abertas, bordas de matas e cidades",
        "comprimento_cm": 17,
        "peso_g": 9,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,
        "alimentacao": "Néctar e pequenos insetos",
        "curiosidade": "Possui uma cauda longa e bifurcada."
    }
]


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

titulo("AVEDEX")

nome_usuario = input("Digite seu nome: ").strip()

opcao_menu = ""

while opcao_menu != "0":
    exibir_menu()

    opcao_menu = input(
        "Escolha uma opção: "
    ).strip()

    print()

    if opcao_menu == "1":
        listar_aves(catalogo_aves)

    elif opcao_menu == "2":
        tela_busca(catalogo_aves)

    elif opcao_menu == "3":
        selecionar_ave_por_id(catalogo_aves)

    elif opcao_menu == "4":
        comparar_duas_aves(catalogo_aves)

    elif opcao_menu == "5":
        mostrar_sobre()

    elif opcao_menu == "0":
        print("Encerrando a AveDex. Até logo!")

    else:
        mensagem_aviso(
            "Opção inválida. "
            "Digite apenas 0, 1, 2, 3, 4 ou 5."
        )

    if opcao_menu != "0":
        pausar()