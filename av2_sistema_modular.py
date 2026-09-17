# ==============================================================================
# PROVA PRÁTICA AV2 - 3º BIMESTRE
# ARQUIVO: av2_sistema_modular.py
# Nome do Aluno: Allan
# Data: 17/09/2026
# Link do Repositório: https://github.com/Allanbrenno/logica-de-programacao/blob/main/av2_sistema_modular.py
# ==============================================================================

# Lista inicial de dados brutos
dados_brutos = [
    "  carlos eduardo silva;desenvolvedor;11988887777  ",
    "  ana paula mendes;analista de rh;21977776666  ",
    "  roberto carlos oliveira;gerente de projetos;31966665555  "
]


# ------------------------------------------------------------------------------
# 1. FUNÇÕES DO SISTEMA
# ------------------------------------------------------------------------------

def limpar_e_formatar_texto(texto):
    """
    FUNÇÃO 1:
    Remove espaços extras e transforma o texto em letras maiúsculas.
    """
    texto_formatado = texto.strip().upper()
    return texto_formatado


def extrair_codigo_ou_ddd(dado):
    """
    FUNÇÃO 2:
    Remove espaços e utiliza fatiamento para pegar os 2 primeiros dígitos.
    """
    dado = dado.strip()
    ddd = dado[0:2]
    return ddd


def processar_e_exibir_cadastros(lista_dados):
    """
    FUNÇÃO 3:
    Percorre a lista, separa os dados, formata nome e cargo,
    extrai o DDD e exibe as informações.
    """
    total = 0

    # Percorre cada cadastro da lista
    for dado in lista_dados:

        # Separa nome, cargo e telefone
        partes = dado.strip().split(";")

        nome = partes[0]
        cargo = partes[1]
        telefone = partes[2]

        # Utiliza as outras funções
        nome_formatado = limpar_e_formatar_texto(nome)
        cargo_formatado = limpar_e_formatar_texto(cargo)
        ddd = extrair_codigo_ou_ddd(telefone)

        # Exibe o cadastro formatado
        print(f"Nome: {nome_formatado}")
        print(f"Cargo: {cargo_formatado}")
        print(f"DDD: {ddd}")
        print("-" * 50)

        total += 1

    return total


# ------------------------------------------------------------------------------
# 2. PROGRAMA PRINCIPAL
# ------------------------------------------------------------------------------

def main():
    print("==================================================")
    print("     SISTEMA DE GESTÃO MODULARIZADO - AV2        ")
    print("==================================================\n")

    print("Iniciando o processamento dos dados...\n")

    # Chama a Função 3 e recebe a quantidade de registros processados
    total_processado = processar_e_exibir_cadastros(dados_brutos)

    # Exibe a quantidade total
    print(f"\nTotal de registros processados: {total_processado}")

    print("\n==================================================")
    print("             PROCESSAMENTO CONCLUÍDO              ")
    print("==================================================")


# Execução do programa
if __name__ == "__main__":
    main()
