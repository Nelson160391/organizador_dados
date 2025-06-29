# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nIn3840ZdrQm4rQ_T-fHmg6nGhNFbUKm
"""

import re
import json
import os

# --- Funções de Organização de Documentos (do exemplo anterior, levemente adaptadas) ---

def _extrair_info_arquivo(nome_arquivo):
    """Extrai extensão e ano de um nome de arquivo."""
    partes_nome = nome_arquivo.split('.')
    extensao = partes_nome[-1].lower() if len(partes_nome) > 1 else 'desconhecido'

    ano_publicacao = None
    match_ano = re.search(r'(\d{4})', nome_arquivo)
    if match_ano:
        try:
            ano_publicacao = int(match_ano.group(1))
        except ValueError:
            pass
    return extensao, ano_publicacao

def organizar_documentos_digitais(nomes_arquivos):
    """
    Organiza uma lista de nomes de arquivos digitais por categoria, tipo e ano de publicação.
    Retorna a estrutura completa da biblioteca organizada.
    """
    mapa_extensoes_categorias = {
        'pdf': "Documentos de Texto/Leitura", 'epub': "Documentos de Texto/Leitura",
        'mobi': "Documentos de Texto/Leitura", 'doc': "Documentos de Texto/Leitura",
        'docx': "Documentos de Texto/Leitura", 'txt': "Documentos de Texto/Leitura",
        'rtf': "Documentos de Texto/Leitura", 'odt': "Documentos de Texto/Leitura",
        'html': "Documentos de Texto/Leitura", 'xml': "Documentos de Texto/Leitura",
        'jpg': "Imagens", 'jpeg': "Imagens", 'png': "Imagens", 'gif': "Imagens",
        'tiff': "Imagens", 'bmp': "Imagens", 'svg': "Imagens",
        'mp3': "Áudio", 'wav': "Áudio", 'aac': "Áudio", 'flac': "Áudio", 'ogg': "Áudio",
        'mp4': "Vídeo", 'avi': "Vídeo", 'mov': "Vídeo", 'wmv': "Vídeo", 'flv': "Vídeo",
        'xls': "Dados/Planilhas", 'xlsx': "Dados/Planilhas", 'csv': "Dados/Planilhas",
        'json': "Dados/Planilhas", 'sqlite': "Dados/Planilhas",
        'ppt': "Apresentações", 'pptx': "Apresentações", 'odp': "Apresentações",
        'py': "Programação/Código", 'java': "Programação/Código", 'c': "Programação/Código",
        'cpp': "Programação/Código", 'h': "Programação/Código", 'sh': "Programação/Código",
        'r': "Programação/Código", 'js': "Programação/Código", 'css': "Programação/Código",
        'zip': "Compactados", 'rar': "Compactados", '7z': "Compactados", 'tar': "Compactados",
        'gz': "Compactados",
        'psd': "Outros/Design", 'ai':  "Outros/Design", 'dwg': "Outros/Engenharia/CAD",
        'md':  "Documentos de Texto/Leitura", 'log': "Outros/Log"
    }

    biblioteca_organizada = {}
    todos_arquivos = [] # Manter uma lista simples de todos os nomes para facilitar busca

    for nome_arquivo in nomes_arquivos:
        todos_arquivos.append(nome_arquivo) # Adiciona à lista geral
        extensao, ano_publicacao = _extrair_info_arquivo(nome_arquivo)
        categoria = mapa_extensoes_categorias.get(extensao, "Outros/Diversos")

        if categoria not in biblioteca_organizada:
            biblioteca_organizada[categoria] = {}
        if extensao not in biblioteca_organizada[categoria]:
            biblioteca_organizada[categoria][extensao] = {}

        if ano_publicacao:
            if ano_publicacao not in biblioteca_organizada[categoria][extensao]:
                biblioteca_organizada[categoria][extensao][ano_publicacao] = []
            biblioteca_organizada[categoria][extensao][ano_publicacao].append(nome_arquivo)
        else:
            if 'sem_ano' not in biblioteca_organizada[categoria][extensao]:
                biblioteca_organizada[categoria][extensao]['sem_ano'] = []
            biblioteca_organizada[categoria][extensao]['sem_ano'].append(nome_arquivo)

    return biblioteca_organizada, todos_arquivos

# --- Funções de Persistência de Dados ---

ARQUIVO_DADOS = 'documentos_biblioteca.json'

def carregar_dados():
    """Carrega os dados da biblioteca de um arquivo JSON."""
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    return [] # Retorna uma lista vazia se o arquivo não existir

def salvar_dados(documentos):
    """Salva os dados da biblioteca em um arquivo JSON."""
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
        json.dump(documentos, f, indent=4, ensure_ascii=False)

# --- Funções da Interface de Linha de Comando (CLI) ---

def exibir_menu():
    """Exibe o menu de opções."""
    print("\n--- Gerenciador de Documentos da Biblioteca ---")
    print("1. Listar Documentos")
    print("2. Adicionar Documento")
    print("3. Renomear Documento")
    print("4. Remover Documento")
    print("5. Sair")
    print("---------------------------------------------")

def listar_documentos(documentos_brutos):
    """Lista e organiza os documentos para exibição."""
    if not documentos_brutos:
        print("\nNenhum documento cadastrado na biblioteca.")
        return

    biblioteca_organizada, _ = organizar_documentos_digitais(documentos_brutos)

    print("\n--- Documentos da Biblioteca (Organizado) ---")
    for categoria, extensoes_dict in sorted(biblioteca_organizada.items()):
        print(f"\n## {categoria}:")
        for extensao, anos_dict in sorted(extensoes_dict.items()):
            print(f"  Extensão: .{extensao}")
            # Ordenar os anos para uma exibição mais limpa
            anos_ordenados = sorted([ano for ano in anos_dict.keys() if ano != 'sem_ano'])
            if 'sem_ano' in anos_dict:
                anos_ordenados.append('sem_ano') # Coloca 'sem_ano' por último

            for ano in anos_ordenados:
                if ano == 'sem_ano':
                    print(f"    - Sem Ano de Publicação:")
                else:
                    print(f"    - Ano: {ano}:")
                for documento in anos_dict[ano]:
                    print(f"      * {documento}")
    print("---------------------------------------------")


def adicionar_documento(documentos_brutos):
    """Permite adicionar um novo nome de documento."""
    novo_documento = input("Digite o nome completo do novo documento (ex: Artigo_ABC_2025.pdf): ")
    if novo_documento in documentos_brutos:
        print(f"Erro: O documento '{novo_documento}' já existe na biblioteca.")
    else:
        documentos_brutos.append(novo_documento)
        salvar_dados(documentos_brutos)
        print(f"Documento '{novo_documento}' adicionado com sucesso!")

def renomear_documento(documentos_brutos):
    """Permite renomear um documento existente."""
    if not documentos_brutos:
        print("\nNão há documentos para renomear.")
        return

    nome_antigo = input("Digite o nome EXATO do documento que deseja renomear: ")
    if nome_antigo not in documentos_brutos:
        print(f"Erro: Documento '{nome_antigo}' não encontrado.")
        return

    novo_nome = input(f"Digite o NOVO nome para '{nome_antigo}': ")
    if novo_nome in documentos_brutos and novo_nome != nome_antigo:
        print(f"Erro: Já existe um documento com o nome '{novo_nome}'.")
        return

    try:
        index = documentos_brutos.index(nome_antigo)
        documentos_brutos[index] = novo_nome
        salvar_dados(documentos_brutos)
        print(f"Documento '{nome_antigo}' renomeado para '{novo_nome}' com sucesso!")
    except ValueError:
        print("Erro interno ao renomear. Documento não encontrado na lista (após verificação inicial).")


def remover_documento(documentos_brutos):
    """Permite remover um documento existente."""
    if not documentos_brutos:
        print("\nNão há documentos para remover.")
        return

    nome_remover = input("Digite o nome EXATO do documento que deseja remover: ")
    if nome_remover in documentos_brutos:
        documentos_brutos.remove(nome_remover)
        salvar_dados(documentos_brutos)
        print(f"Documento '{nome_remover}' removido com sucesso!")
    else:
        print(f"Erro: Documento '{nome_remover}' não encontrado.")

def main():
    """Função principal da CLI."""
    documentos_biblioteca = carregar_dados() # Carrega os documentos salvos

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            listar_documentos(documentos_biblioteca)
        elif escolha == '2':
            adicionar_documento(documentos_biblioteca)
        elif escolha == '3':
            renomear_documento(documentos_biblioteca)
        elif escolha == '4':
            remover_documento(documentos_biblioteca)
        elif escolha == '5':
            print("Saindo do Gerenciador de Documentos. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

# Garante que a função main seja executada quando o script for iniciado
if __name__ == "__main__":
    main()