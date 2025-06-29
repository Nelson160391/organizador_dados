# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12GxDo8T7LGWPKykAhITUrRoeA4sgHokK
"""



import re

def organizar_documentos_digitais(nomes_arquivos):
    """
    Organiza uma lista de nomes de arquivos digitais por tipo e ano de publicação.

    Args:
        nomes_arquivos (list): Uma lista de strings, onde cada string é o nome de um arquivo.

    Returns:
        dict: Um dicionário onde as chaves são os tipos de arquivo e os valores são
              dicionários aninhados organizados por ano de publicação, contendo
              os nomes dos arquivos.
              Ex: {
                  'pdf': {
                      2023: ['Artigo_Neurociencia_Cognitiva_2023.pdf'],
                      2022: ['Tese_Doutorado_Otimizacao_Sistemas_Energeticos_2022.pdf']
                  },
                  'epub': {
                      ...
                  }
              }
    """
    documentos_organizados = {}

    for nome_arquivo in nomes_arquivos:
        # Extrair a extensão do arquivo (tipo)
        partes_nome = nome_arquivo.split('.')
        if len(partes_nome) < 2:
            # Ignora arquivos sem extensão aparente
            continue
        tipo_arquivo = partes_nome[-1].lower()

        # Extrair o ano de publicação (tentar encontrar 4 dígitos numéricos)
        ano_publicacao = None
        match_ano = re.search(r'(\d{4})', nome_arquivo)
        if match_ano:
            try:
                ano_publicacao = int(match_ano.group(1))
            except ValueError:
                pass # Se não conseguir converter para int, ignora o ano

        # Inicializar a estrutura se o tipo de arquivo não existir
        if tipo_arquivo not in documentos_organizados:
            documentos_organizados[tipo_arquivo] = {}

        # Adicionar o arquivo ao ano correspondente
        if ano_publicacao:
            if ano_publicacao not in documentos_organizados[tipo_arquivo]:
                documentos_organizados[tipo_arquivo][ano_publicacao] = []
            documentos_organizados[tipo_arquivo][ano_publicacao].append(nome_arquivo)
        else:
            # Adiciona arquivos sem ano específico a uma categoria 'sem_ano' ou similar
            if 'sem_ano' not in documentos_organizados[tipo_arquivo]:
                documentos_organizados[tipo_arquivo]['sem_ano'] = []
            documentos_organizados[tipo_arquivo]['sem_ano'].append(nome_arquivo)

    return documentos_organizados

# Seus exemplos de nomes de arquivos
meus_documentos = [
    'Artigo_Neurociencia_Cognitiva_2023.pdf',
    'Revisao_Literatura_Inteligencia_Artificial_IEEE.pdf',
    'Impacto_Mudancas_Climaticas_Agricultura_ISSN_0123-4567.pdf',
    'Analise_Dados_Big_Data_Jornal_Cientifico_XYZ.pdf',
    'Pesquisa_Qualitativa_Educacao_Revista_Pedagogia_Aplicada.pdf',
    'Metodos_Estatisticos_Ciencias_Sociais_2024.pdf',
    'Desafios_Desenvolvimento_Sustentavel_Artigo_Conferencia.pdf',
    'Tese_Doutorado_Otimizacao_Sistemas_Energeticos_2022.pdf',
    'Dissertacao_Mestrado_Uso_Tecnologia_Educacao_2023.pdf',
    'Tese_Analise_Literaria_Romantismo_Brasileiro_USP.pdf', # Sem ano específico no nome
    'Dissertacao_Modelagem_Computacional_Farmacologia_2021.pdf',
    'Tese_Impacto_Redes_Sociais_Saude_Mental_2024.pdf',
    'Livro_Introducao_Programacao_Python_2ed.pdf', # Sem ano específico no nome
    'Historia_Filosofia_Ocidental_Vol_1.epub', # Sem ano específico no nome
    'Guia_Completo_Marketing_Digital.mobi', # Sem ano específico no nome
    'Manual_Psicologia_Desenvolvimento.pdf', # Sem ano específico no nome
    'Fisica_Quantica_Para_Iniciantes.epub', # Sem ano específico no nome
    'Romance_Classico_Aventura_No_Mar.pdf', # Sem ano específico no nome
    'Economia_Global_Perspectivas_Futuras.pdf', # Sem ano específico no nome
    'Culinaria_Regional_Receitas_Tradicionais.pdf' # Sem ano específico no nome
]

# Chamar a função para organizar os documentos
documentos_organizados = organizar_documentos_digitais(meus_documentos)

# Imprimir o resultado de forma legível
for tipo, anos in documentos_organizados.items():
    print(f"Tipo de Arquivo: .{tipo}")
    for ano, arquivos in sorted(anos.items()): # Ordena os anos para melhor visualização
        if ano == 'sem_ano':
            print(f"  Sem Ano de Publicação:")
        else:
            print(f"  Ano: {ano}:")
        for arquivo in arquivos:
            print(f"    - {arquivo}")
    print("-" * 30) # Separador para facilitar a leitura

import re

def organizar_documentos_digitais(nomes_arquivos):
    """
    Organiza uma lista de nomes de arquivos digitais por tipo e ano de publicação.

    Args:
        nomes_arquivos (list): Uma lista de strings, onde cada string é o nome de um arquivo.

    Returns:
        dict: Um dicionário onde as chaves são os tipos de arquivo e os valores são
              dicionários aninhados organizados por ano de publicação, contendo
              os nomes dos arquivos.
              Ex: {
                  'pdf': {
                      2023: ['Artigo_Neurociencia_Cognitiva_2023.pdf'],
                      2022: ['Tese_Doutorado_Otimizacao_Sistemas_Energeticos_2022.pdf']
                  },
                  'epub': {
                      ...
                  }
              }
    """
    documentos_organizados = {}

    for nome_arquivo in nomes_arquivos:
        # Extrair a extensão do arquivo (tipo)
        partes_nome = nome_arquivo.split('.')
        if len(partes_nome) < 2:
            # Ignora arquivos sem extensão aparente
            continue
        tipo_arquivo = partes_nome[-1].lower()

        # Extrair o ano de publicação (tentar encontrar 4 dígitos numéricos)
        ano_publicacao = None
        match_ano = re.search(r'(\d{4})', nome_arquivo)
        if match_ano:
            try:
                ano_publicacao = int(match_ano.group(1))
            except ValueError:
                pass # Se não conseguir converter para int, ignora o ano

        # Inicializar a estrutura se o tipo de arquivo não existir
        if tipo_arquivo not in documentos_organizados:
            documentos_organizados[tipo_arquivo] = {}

        # Adicionar o arquivo ao ano correspondente
        if ano_publicacao:
            if ano_publicacao not in documentos_organizados[tipo_arquivo]:
                documentos_organizados[tipo_arquivo][ano_publicacao] = []
            documentos_organizados[tipo_arquivo][ano_publicacao].append(nome_arquivo)
        else:
            # Adiciona arquivos sem ano específico a uma categoria 'sem_ano' ou similar
            if 'sem_ano' not in documentos_organizados[tipo_arquivo]:
                documentos_organizados[tipo_arquivo]['sem_ano'] = []
            documentos_organizados[tipo_arquivo]['sem_ano'].append(nome_arquivo)

    return documentos_organizados

# Seus exemplos de nomes de arquivos
meus_documentos = [
    'Artigo_Neurociencia_Cognitiva_2023.pdf',
    'Revisao_Literatura_Inteligencia_Artificial_IEEE.pdf',
    'Impacto_Mudancas_Climaticas_Agricultura_ISSN_0123-4567.pdf',
    'Analise_Dados_Big_Data_Jornal_Cientifico_XYZ.pdf',
    'Pesquisa_Qualitativa_Educacao_Revista_Pedagogia_Aplicada.pdf',
    'Metodos_Estatisticos_Ciencias_Sociais_2024.pdf',
    'Desafios_Desenvolvimento_Sustentavel_Artigo_Conferencia.pdf',
    'Tese_Doutorado_Otimizacao_Sistemas_Energeticos_2022.pdf',
    'Dissertacao_Mestrado_Uso_Tecnologia_Educacao_2023.pdf',
    'Tese_Analise_Literaria_Romantismo_Brasileiro_USP.pdf', # Sem ano específico no nome
    'Dissertacao_Modelagem_Computacional_Farmacologia_2021.pdf',
    'Tese_Impacto_Redes_Sociais_Saude_Mental_2024.pdf',
    'Livro_Introducao_Programacao_Python_2ed.pdf', # Sem ano específico no nome
    'Historia_Filosofia_Ocidental_Vol_1.epub', # Sem ano específico no nome
    'Guia_Completo_Marketing_Digital.mobi', # Sem ano específico no nome
    'Manual_Psicologia_Desenvolvimento.pdf', # Sem ano específico no nome
    'Fisica_Quantica_Para_Iniciantes.epub', # Sem ano específico no nome
    'Romance_Classico_Aventura_No_Mar.pdf', # Sem ano específico no nome
    'Economia_Global_Perspectivas_Futuras.pdf', # Sem ano específico no nome
    'Culinaria_Regional_Receitas_Tradicionais.pdf' # Sem ano específico no nome
]

# Chamar a função para organizar os documentos
documentos_organizados = organizar_documentos_digitais(meus_documentos)

# Imprimir o resultado de forma legível
for tipo, anos in documentos_organizados.items():
    print(f"Tipo de Arquivo: .{tipo}")
    # Ordena os anos para melhor visualização, colocando 'sem_ano' no final
    for ano, arquivos in sorted(anos.items(), key=lambda item: (item[0] != 'sem_ano', item[0])):
        if ano == 'sem_ano':
            print(f"  Sem Ano de Publicação:")
        else:
            print(f"  Ano: {ano}:")
        for arquivo in arquivos:
            print(f"    - {arquivo}")
    print("-" * 30) # Separador para facilitar a leitura