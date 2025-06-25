from input_handler.file_loader import load_all_client_files
from processor.consolidator import consolidate_client_data
from output_handler.exporter import export_consolidated_data

def main():
    client_dirs = load_all_client_files("input/")
    
    for client_name, file_paths in client_dirs.items():
        df_dict = consolidate_client_data(file_paths)
        export_consolidated_data(client_name, df_dict, output_path="output/")
    
    print("✔ Consolidação finalizada com sucesso.")

if __name__ == "__main__":
    main()
