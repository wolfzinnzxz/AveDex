import json
from pathlib import Path

from src.avedex.utils import mensagem_erro


CAMINHO_PROJETO = Path(__file__).resolve().parents[2]

CAMINHO_DATASET = (
    CAMINHO_PROJETO
    / "data"
    / "avedex_dataset_midias.json"
)


CAMPOS_OBRIGATORIOS = [
    "id",
    "slug",
    "nome_popular",
    "nome_cientifico",
    "ordem",
    "familia",
    "dieta_tipo",
    "comprimento_cm",
    "peso_g",
    "status_conservacao",
    "indice_conservacao",
    "descricao",
    "habitat",
    "alimentacao",
    "midia",
]

CAMPOS_MIDIA = [
    "pagina_guia",
    "fotografo",
    "wikiaves_url",
    "som_url",
    "imagem_url",
]


def carregar_dataset(caminho=CAMINHO_DATASET):
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    except FileNotFoundError:
        mensagem_erro(
            f"Arquivo de dataset não encontrado: {caminho}"
        )
        return {
            "nome_dataset": "AveDex",
            "aves": []
        }

    except json.JSONDecodeError:
        mensagem_erro("Erro ao ler o JSON do dataset.")
        mensagem_erro(
            "Verifique vírgulas, aspas, chaves e colchetes."
        )
        return {
            "nome_dataset": "AveDex",
            "aves": []
        }


def carregar_aves():
    dataset = carregar_dataset()

    return dataset.get("aves", [])


def obter_fontes_globais():
    dataset = carregar_dataset()

    return dataset.get("fontes_globais", {})