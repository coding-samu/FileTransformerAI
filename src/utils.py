def load_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def save_file(data, file_path):
    with open(file_path, 'w') as file:
        file.write(data)
