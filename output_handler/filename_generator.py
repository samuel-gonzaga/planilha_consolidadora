from datetime import datetime

def generate_filename(client_name):
    now = datetime.now().strftime("%Y%m")
    return f"{client_name}_consolidado_{now}.xlsx"
