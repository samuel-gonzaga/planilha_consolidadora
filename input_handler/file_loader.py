import os
import glob

def load_all_client_files(base_path):
    clients = {}
    for client_name in os.listdir(base_path):
        client_path = os.path.join(base_path, client_name)
        if os.path.isdir(client_path):
            pattern = os.path.join(client_path, "*")
            files = glob.glob(pattern)
            clients[client_name] = files
    return clients
