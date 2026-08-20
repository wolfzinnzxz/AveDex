from src.avedex.utils import (
    titulo,
    mensagem_aviso,
    normalizar_texto,
    valor_ou_indisponivel,
)


CAMPOS_BUSCA = [
    "nome_popular",
    "nome_cientifico",
    "familia",
    "ordem",
    "dieta_tipo",
]


def listar_aves(aves):
    titulo("AVES CADASTRADAS")

    for ave in aves:
        print(f"{ave['id']} - {ave['nome_popular']}")


def buscar_ave_por_id(aves, id_procurado):
    for ave in aves:
        if str(ave["id"]) == str(id_procurado):
            return ave

    return None


def escolher_ave(aves, mensagem="Escolha uma ave"):
    listar_aves(aves)

    id_escolhido = input(f"\n{mensagem}: ").strip()

    ave_encontrada = buscar_ave_por_id(aves, id_escolhido)

    if ave_encontrada is None:
        mensagem_aviso("Ave não encontrada. Confira o ID informado.")
        return None

    return ave_encontrada


def mostrar_detalhes(ave):
    titulo(ave.get("nome_popular", "Ave"))

    print(f"ID: {ave.get('id')}")
    print(f"Nome popular: {ave.get('nome_popular')}")
    print(f"Nome científico: {ave.get('nome_cientifico')}")
    print(f"Ordem: {ave.get('ordem')}")
    print(f"Família: {ave.get('familia')}")
    print(f"Dieta: {ave.get('dieta_tipo')}")
    print(
        f"Comprimento: "
        f"{valor_ou_indisponivel(ave.get('comprimento_cm'), 'cm')}"
    )
    print(
        f"Peso médio: "
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

    print()
    print("Descrição")
    print(ave.get("descricao", "Não informado"))

    print()
    print("Habitat")
    print(ave.get("habitat", "Não informado"))

    print()
    print("Alimentação")
    print(ave.get("alimentacao", "Não informado"))

    curiosidade = ave.get("curiosidade")

    if curiosidade:
        print()
        print("Curiosidade")
        print(curiosidade)

    midia = ave.get("midia", {})

    print()
    print("Mídia")
    print(f"Página no guia: {midia.get('pagina_guia', 'Não informado')}")
    print(f"Fotógrafo: {midia.get('fotografo', 'Não informado')}")
    print(f"WikiAves: {midia.get('wikiaves_url', 'Não informado')}")
    print(f"Som: {midia.get('som_url', 'Não informado')}")
    print(f"Imagem: {midia.get('imagem_url', 'Não informado')}")


def tela_detalhes(aves):
    ave = escolher_ave(
        aves,
        "Digite o ID da ave para ver detalhes"
    )

    if ave is not None:
        mostrar_detalhes(ave)


def criar_texto_busca(ave):
    valores = []

    for campo in CAMPOS_BUSCA:
        valores.append(str(ave.get(campo, "")))

    texto = " ".join(valores)

    return normalizar_texto(texto)


def buscar_lista_aves(aves, termo_busca):
    resultados = []

    termo = normalizar_texto(termo_busca)

    for ave in aves:
        texto_busca = criar_texto_busca(ave)

        if termo in texto_busca:
            resultados.append(ave)

    return resultados


def buscar_aves(aves):
    titulo("BUSCAR AVE")

    termo = input(
        "Digite parte do nome, família, ordem ou dieta: "
    ).strip()

    if termo == "":
        mensagem_aviso(
            "Digite algum texto para realizar a busca."
        )
        return

    resultados = buscar_lista_aves(aves, termo)

    if len(resultados) == 0:
        mensagem_aviso("Nenhuma ave encontrada.")
        return

    titulo("RESULTADO DA BUSCA")

    for ave in resultados:
        print(
            f"{ave['id']} - {ave['nome_popular']} "
            f"({ave['familia']}, {ave['dieta_tipo']})"
        )

    escolha = input(
        "\nDigite o ID para ver detalhes ou ENTER para voltar: "
    ).strip()

    if escolha != "":
        ave = buscar_ave_por_id(resultados, escolha)

        if ave is None:
            mensagem_aviso("ID não encontrado nos resultados.")
        else:
            mostrar_detalhes(ave)