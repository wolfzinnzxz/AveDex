import unicodedata


def exibir_linha():
    print("=" * 50)


def exibir_menu():
    print()
    exibir_linha()
    print("AVEDEX - MENU PRINCIPAL")
    exibir_linha()
    print("1 - Listar aves")
    print("2 - Buscar ave")
    print("3 - Ver detalhes de uma ave")
    print("4 - Comparar duas aves")
    print("5 - Sobre a AveDex")
    print("0 - Sair")


def listar_aves(catalogo):
    print()
    exibir_linha()
    print("AVES CADASTRADAS")
    exibir_linha()

    for ave in catalogo:
        print(f"{ave['id']} - {ave['nome_popular']}")


def buscar_ave_por_id(catalogo, id_procurado):
    for ave in catalogo:
        if str(ave["id"]) == id_procurado:
            return ave

    return None


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


def buscar_aves_por_nome(catalogo, termo_busca):
    resultados = []

    termo = normalizar_texto(termo_busca)

    for ave in catalogo:
        nome = normalizar_texto(ave["nome_popular"])

        if termo in nome:
            resultados.append(ave)

    return resultados


def buscar_aves(catalogo, termo_busca):
    resultados = []

    termo = normalizar_texto(termo_busca)

    for ave in catalogo:
        campos_busca = [
            ave.get("nome_popular", ""),
            ave.get("nome_cientifico", ""),
            ave.get("familia", ""),
            ave.get("ordem", ""),
            ave.get("dieta_tipo", "")
        ]

        texto_busca = " ".join(campos_busca)
        texto_busca = normalizar_texto(texto_busca)

        if termo in texto_busca:
            resultados.append(ave)

    return resultados


def exibir_resultados_busca(resultados):
    print()
    exibir_linha()
    print("RESULTADOS DA BUSCA")
    exibir_linha()

    if len(resultados) == 0:
        print("Nenhuma ave encontrada.")
    else:
        print(f"Quantidade de resultados: {len(resultados)}")
        print()

        for ave in resultados:
            print(
                f"{ave['id']} - {ave['nome_popular']} "
                f"({ave['familia']}, {ave['dieta_tipo']})"
            )


def valor_ou_indisponivel(valor, unidade=""):
    if valor is None or valor == "":
        return "Não informado"

    if unidade != "":
        return f"{valor} {unidade}"

    return str(valor)


def exibir_detalhes_ave(ave):
    print()
    exibir_linha()
    print("DETALHES DA AVE")
    exibir_linha()

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
    listar_aves(catalogo)

    id_escolhido = input(
        "\nDigite o ID da ave: "
    ).strip()

    ave_encontrada = buscar_ave_por_id(
        catalogo,
        id_escolhido
    )

    if ave_encontrada is None:
        print("Ave não encontrada. Confira o ID informado.")
    else:
        exibir_detalhes_ave(ave_encontrada)


def tela_busca(catalogo):
    termo = input(
        "Digite parte do nome, família, ordem ou dieta: "
    ).strip()

    if termo == "":
        print("Digite algum texto para realizar a busca.")
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
                print("ID não encontrado nos resultados.")
            else:
                exibir_detalhes_ave(ave_encontrada)


def imprimir_linha_comparacao(rotulo, valor_1, valor_2):
    print(
        f"{rotulo:<18} | "
        f"{str(valor_1):<25} | "
        f"{str(valor_2):<25}"
    )


def exibir_comparacao_aves(ave_1, ave_2):
    print()
    print("=" * 78)
    print("COMPARAÇÃO ENTRE AVES")
    print("=" * 78)

    imprimir_linha_comparacao(
        "Campo",
        ave_1["nome_popular"],
        ave_2["nome_popular"]
    )

    print("-" * 78)

    imprimir_linha_comparacao(
        "Nome científico",
        ave_1.get("nome_cientifico"),
        ave_2.get("nome_cientifico")
    )

    imprimir_linha_comparacao(
        "Ordem",
        ave_1.get("ordem"),
        ave_2.get("ordem")
    )

    imprimir_linha_comparacao(
        "Família",
        ave_1.get("familia"),
        ave_2.get("familia")
    )

    imprimir_linha_comparacao(
        "Dieta",
        ave_1.get("dieta_tipo"),
        ave_2.get("dieta_tipo")
    )

    imprimir_linha_comparacao(
        "Habitat",
        ave_1.get("habitat"),
        ave_2.get("habitat")
    )

    imprimir_linha_comparacao(
        "Comprimento",
        valor_ou_indisponivel(
            ave_1.get("comprimento_cm"),
            "cm"
        ),
        valor_ou_indisponivel(
            ave_2.get("comprimento_cm"),
            "cm"
        )
    )

    imprimir_linha_comparacao(
        "Peso",
        valor_ou_indisponivel(
            ave_1.get("peso_g"),
            "g"
        ),
        valor_ou_indisponivel(
            ave_2.get("peso_g"),
            "g"
        )
    )

    imprimir_linha_comparacao(
        "Conservação",
        ave_1.get(
            "status_conservacao",
            "Não informado"
        ),
        ave_2.get(
            "status_conservacao",
            "Não informado"
        )
    )

    imprimir_linha_comparacao(
        "Índice",
        ave_1.get(
            "indice_conservacao",
            "Não informado"
        ),
        ave_2.get(
            "indice_conservacao",
            "Não informado"
        )
    )

    # Melhoria escolhida:
    # informar qual ave é mais pesada.

    print()

    peso_1 = ave_1.get("peso_g")
    peso_2 = ave_2.get("peso_g")

    if peso_1 is not None and peso_2 is not None:
        if peso_1 > peso_2:
            print(
                f"A ave mais pesada é a "
                f"{ave_1['nome_popular']} ({peso_1} g)."
            )

        elif peso_2 > peso_1:
            print(
                f"A ave mais pesada é a "
                f"{ave_2['nome_popular']} ({peso_2} g)."
            )

        else:
            print("As duas aves possuem o mesmo peso.")


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
        print("Ave não encontrada. Confira o ID informado.")
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

    exibir_comparacao_aves(
        ave_1,
        ave_2
    )


def mostrar_sobre():
    print("A AveDex é um catálogo interativo de aves.")
    print(
        "Em breve, teremos batalha, imagens, sons "
        "e dados em arquivo JSON."
    )


def pausar():
    input(
        "\nPressione ENTER para voltar ao menu..."
    )


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
    },

    {
        "id": 8,
        "nome_popular": "Coruja-buraqueira",
        "nome_cientifico": "Athene cunicularia",
        "ordem": "Strigiformes",
        "familia": "Strigidae",
        "dieta_tipo": "Carnívora",
        "habitat": "Campos, pastagens, áreas abertas e regiões urbanas",
        "comprimento_cm": 23,
        "peso_g": 170,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,
        "alimentacao": "Insetos, pequenos mamíferos e outros animais",
        "curiosidade": "Costuma utilizar buracos no solo como abrigo."
    },

    {
        "id": 9,
        "nome_popular": "Garça-branca-grande",
        "nome_cientifico": "Ardea alba",
        "ordem": "Pelecaniformes",
        "familia": "Ardeidae",
        "dieta_tipo": "Carnívora",
        "habitat": "Lagos, rios, áreas alagadas e regiões costeiras",
        "comprimento_cm": 100,
        "peso_g": 1000,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,
        "alimentacao": "Peixes, anfíbios, insetos e pequenos animais",
        "curiosidade": "Pode permanecer imóvel por bastante tempo enquanto procura alimento."
    }
]


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

exibir_linha()
print("AVEDEX")
exibir_linha()

nome_usuario = input(
    "Digite seu nome: "
).strip()

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
        print(
            "Opção inválida. "
            "Digite apenas 0, 1, 2, 3, 4 ou 5."
        )

    if opcao_menu != "0":
        pausar()