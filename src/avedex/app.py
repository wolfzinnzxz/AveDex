from src.avedex.catalogo import (
    listar_aves,
    buscar_aves,
    tela_detalhes,
)

from src.avedex.comparacao import comparar_aves
from src.avedex.creditos import mostrar_creditos
from src.avedex.dados import carregar_aves
from src.avedex.interface import (
    abertura,
    exibir_menu_principal,
)

from src.avedex.utils import (
    pausar,
    mensagem_aviso,
)


def executar():
    aves = carregar_aves()

    if not aves:
        mensagem_aviso("Nenhuma ave foi carregada.")
        return

    abertura(aves)

    while True:
        exibir_menu_principal()

        opcao = input(
            "Escolha uma opção: "
        ).strip()

        if opcao == "1":
            listar_aves(aves)
            pausar()

        elif opcao == "2":
            buscar_aves(aves)
            pausar()

        elif opcao == "3":
            tela_detalhes(aves)
            pausar()

        elif opcao == "4":
            comparar_aves(aves)
            pausar()

        elif opcao == "5":
            mostrar_creditos()
            pausar()

        elif opcao == "0":
            print(
                "Encerrando a AveDex. Até logo!"
            )
            break

        else:
            mensagem_aviso("Opção inválida.")
            pausar()