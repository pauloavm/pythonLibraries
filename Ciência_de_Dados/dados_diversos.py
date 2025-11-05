import pandas as pd
import numpy as np
import glob
import os

# ==============================================================================
# 1. CONFIGURAÇÃO GLOBAL (ÁREA DE ALTERAÇÃO)
#    TODAS AS VARIÁVEIS DESTE BLOCO DEVEM SER AJUSTADAS CONFORME A NECESSIDADE
# ==============================================================================

# PASTA ONDE ESTÃO OS ARQUIVOS EXCEL QUE SERÃO LIDOS E CONCATENADOS.
# EXEMPLO: './dados' (significa a pasta 'dados' no mesmo diretório do script)
caminho_pasta_dados = "[SUA PASTA DE DADOS AQUI]"

# NOME E CAMINHO DO ARQUIVO CONCATENADO DE SAÍDA NO FORMATO EXCEL.
# O SCRIPT SALVARÁ O MESMO ARQUIVO TAMBÉM EM CSV, JSON E PARQUET.
nome_arquivo_saida_excel = f"{caminho_pasta_dados}/dados_consolidados_finais.xlsx"

# EXTENSÃO DOS ARQUIVOS QUE SERÃO PROCURADOS E LIDOS.
# PODE SER ALTERADA PARA '.xls' ou OUTROS FORMATOS DE ARQUIVO.
extensao_arquivos_busca = "*.xlsx"

# LISTA DE COLUNAS QUE CONTÊM DADOS DE TIPOS MISTOS (TEXTO E NÚMERO, string e int).
# ESTAS COLUNAS SÃO CONVERTIDAS FORÇADAMENTE PARA TEXTO (string)
# PARA EVITAR ERROS DE SERIALIZAÇÃO, PRINCIPALMENTE NO FORMATO PARQUET.
colunas_com_tipos_mistos = ["Telefone", "data_nascimento"]

# ==============================================================================
# 2. FUNÇÃO PRINCIPAL DE CONCATENAÇÃO E EXPORTAÇÃO
# ==============================================================================


def concatenar_arquivos_excel(
    caminho_da_pasta, nome_arquivo_saida, extensao_busca, colunas_problema_tipo
):
    """
    Localiza, lê e concatena arquivos Excel, tratando erros de formatação
    e exportando o resultado para múltiplos formatos (Excel, CSV, JSON, Parquet).

    Args:
        caminho_da_pasta (str): Caminho do diretório dos arquivos de entrada.
        nome_arquivo_saida (str): Caminho e nome base do arquivo de saída (Excel).
        extensao_busca (str): Padrão de busca de arquivos (ex: '*.xlsx').
        colunas_problema_tipo (list): Lista de colunas para forçar o tipo 'string'.
    """

    # --- 2.1. BUSCA E FILTRAGEM DE ARQUIVOS ---

    # 1. Cria o padrão de busca completo (ex: './dados/*.xlsx')
    padrao_busca = os.path.join(caminho_da_pasta, extensao_busca)
    lista_arquivos = glob.glob(padrao_busca)

    # 2. Filtra o arquivo de saída (EVITA RE-INCLUSÃO):
    #    Garante que o arquivo consolidado anterior não seja lido novamente.
    lista_arquivos = [
        f
        for f in lista_arquivos
        if os.path.abspath(f) != os.path.abspath(nome_arquivo_saida)
    ]

    if not lista_arquivos:
        print(
            f"ATENÇÃO: Nenhum arquivo {extensao_busca} encontrado no caminho: {caminho_da_pasta}"
        )
        return  # Finaliza a função se não houver arquivos

    print(f"Arquivos encontrados para concatenação ({len(lista_arquivos)}):")
    for arquivo in lista_arquivos:
        print(f"- {os.path.basename(arquivo)}")

    lista_dataframes = []

    # --- 2.2. LEITURA COM TRATAMENTO DE ERRO (FALLBACK PARA CALAMINE) ---
    for arquivo in lista_arquivos:
        df_temp = None

        # TENTATIVA 1: Leitura Padrão (usa 'openpyxl' para .xlsx)
        try:
            df_temp = pd.read_excel(arquivo)
            print(
                f"Arquivo {os.path.basename(arquivo)} lido com sucesso (Motor Padrão)."
            )

        # Tratamento de Falha: Ocorre geralmente devido a corrupção de formatação
        except Exception as e:
            print(
                f"ERRO: Falha na leitura padrão de {os.path.basename(arquivo)}. Tentando 'calamine'..."
            )

            # TENTATIVA 2: Fallback para 'calamine' (Motor mais robusto contra corrupção)
            try:
                # O motor 'calamine' deve ser instalado com 'pip install calamine'
                df_temp = pd.read_excel(arquivo, engine="calamine")
                print(
                    f"Arquivo {os.path.basename(arquivo)} lido com sucesso (Motor Calamine)."
                )

            except Exception as e_calamine:
                print(
                    f"ERRO CRÍTICO: Falha ao ler o arquivo {os.path.basename(arquivo)} com 'calamine'."
                )
                print(f"Causa: Formatação corrompida. Erro Original: {e_calamine}")

        # Adiciona o DataFrame lido (se existir) à lista
        if df_temp is not None:
            lista_dataframes.append(df_temp)

    # --- 2.3. CONCATENAÇÃO E TRATAMENTO DE DADOS ---
    if lista_dataframes:
        # CONCATENAÇÃO: Junta todos os DataFrames verticalmente (empilha as linhas)
        df_final = pd.concat(lista_dataframes, ignore_index=True)

        # TRATAMENTO: Substitui valores infinitos por NaN (Not a Number)
        df_final.replace([np.inf, -np.inf], np.nan, inplace=True)

        # TRATAMENTO: CONVERSÃO DE TIPOS PARA COLUNAS PROBLEMÁTICAS
        # Converte as colunas de tipos mistos para garantir a serialização em Parquet.
        for coluna in colunas_problema_tipo:
            try:
                if coluna in df_final.columns:
                    # Converte para string (texto)
                    df_final[coluna] = df_final[coluna].astype(str)
                    print(
                        f"COLUNA TRATADA: A coluna '{coluna}' foi convertida para texto (string)."
                    )
            except Exception as e:
                print(f"AVISO: Falha ao converter a coluna '{coluna}' para string: {e}")

        # --- 2.4. SALVAR RESULTADOS ---

        # CRIAÇÃO DA PASTA: Cria o diretório de saída caso ele não exista
        os.makedirs(os.path.dirname(nome_arquivo_saida), exist_ok=True)

        # SALVAR EXCEL
        try:
            df_final.to_excel(nome_arquivo_saida, index=False)
            print("\n--- CONCATENAÇÃO CONCLUÍDA ---")
            print(f"Total de linhas consolidadas: {len(df_final)}")
            print(f"O arquivo EXCEL final foi salvo como: {nome_arquivo_saida}")
        except Exception as e:
            print(f"Erro ao salvar o arquivo EXCEL concatenado: {e}")

        # SALVAR EM OUTROS FORMATOS
        print("\n--- SALVANDO EM OUTROS FORMATOS (CSV, JSON, PARQUET) ---")

        # SALVAR CSV
        nome_csv = nome_arquivo_saida.replace(".xlsx", ".csv")
        try:
            df_final.to_csv(nome_csv, index=False, encoding="utf-8")
            print(f"Arquivo CSV salvo como: {nome_csv}")
        except Exception as e:
            print(f"Erro ao salvar o arquivo CSV: {e}")

        # SALVAR JSON
        nome_json = nome_arquivo_saida.replace(".xlsx", ".json")
        try:
            # Orientação 'records' gera um JSON no formato de lista de objetos
            df_final.to_json(nome_json, orient="records", indent=4)
            print(f"Arquivo JSON salvo como: {nome_json}")
        except Exception as e:
            print(f"Erro ao salvar o arquivo JSON: {e}")

        # SALVAR PARQUET (Requer 'pip install pyarrow' ou 'pip install fastparquet')
        nome_parquet = nome_arquivo_saida.replace(".xlsx", ".parquet")
        try:
            # Formato ideal para Big Data (comprimido e otimizado)
            df_final.to_parquet(nome_parquet, engine="pyarrow", index=False)
            print(f"Arquivo PARQUET salvo como: {nome_parquet}")
        except ImportError:
            # Informa se a biblioteca Parquet (pyarrow) não estiver instalada
            print(
                f"ATENÇÃO: A biblioteca 'pyarrow' ou 'fastparquet' é necessária para Parquet. Por favor, instale uma delas (ex: pip install pyarrow)."
            )
        except Exception as e:
            print(f"Erro ao salvar o arquivo PARQUET: {e}")

    else:
        print("Nenhum dado válido para concatenar após a leitura dos arquivos.")


# ==============================================================================
# 3. BLOCO DE EXECUÇÃO PRINCIPAL
# ==============================================================================

# Este bloco garante que a função principal só seja chamada quando o script
# for executado diretamente (e não importado como módulo).
if __name__ == "__main__":
    concatenar_arquivos_excel(
        caminho_pasta_dados,
        nome_arquivo_saida_excel,
        extensao_arquivos_busca,
        colunas_com_tipos_mistos,
    )
