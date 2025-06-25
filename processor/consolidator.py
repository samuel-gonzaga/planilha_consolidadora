import pandas as pd
from processor.utils import identify_category

def consolidate_client_data(file_paths, date_column="data"):  # <-- especifique o nome da coluna de data aqui
    consolidated = {}
    
    for file in file_paths:
        try:
            if file.endswith(".csv"):
                df = pd.read_csv(file)
            elif file.endswith(".xlsx"):
                df = pd.read_excel(file)
            else:
                continue

            category = identify_category(file)

            # Converte a coluna de data para datetime
            if date_column in df.columns:
                df[date_column] = pd.to_datetime(df[date_column], errors='coerce')

            if category not in consolidated:
                consolidated[category] = []
            consolidated[category].append(df)
        except Exception as e:
            print(f"Erro ao processar {file}: {e}")
    
    # Concatena por categoria em ordem de data (mais antiga → mais recente)
    for cat in consolidated:
        # Ordena os DataFrames individualmente
        sorted_dfs = []
        for df in consolidated[cat]:
            if date_column in df.columns:
                df = df.sort_values(by=date_column)
            sorted_dfs.append(df)
        # Concatena os DataFrames já ordenados
        consolidated[cat] = pd.concat(sorted_dfs, ignore_index=True)

    return consolidated
