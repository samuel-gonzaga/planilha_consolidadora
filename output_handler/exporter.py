import pandas as pd
from openpyxl import Workbook
from output_handler.filename_generator import generate_filename
import os

def export_consolidated_data(client_name, df_dict, output_path="output/"):
    filename = generate_filename(client_name)
    filepath = os.path.join(output_path, filename)

    with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
        for category, df in df_dict.items():
            df.to_excel(writer, sheet_name=category[:31], index=False)  # Limite de 31 chars

    print(f"✔ Arquivo salvo: {filepath}")
