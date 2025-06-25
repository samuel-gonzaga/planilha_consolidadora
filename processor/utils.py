import os

def identify_category(file_path):
    """Tenta identificar categoria com base no nome do arquivo."""
    filename = os.path.basename(file_path).lower()
    if "nota" in filename:
        return "Notas"
    elif "banco" in filename:
        return "Bancos"
    elif "receita" in filename:
        return "Receitas"
    else:
        return "Outros"
