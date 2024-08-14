def load_file(file_path, mode='text'):
    if mode == 'text':
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    elif mode == 'image':
        with open(file_path, 'rb') as file:
            return file.read()
    else:
        raise ValueError(f"Unknown mode: {mode}")

def save_file(data, file_path, mode='text'):
    if mode == 'text':
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)
    elif mode == 'image':
        with open(file_path, 'wb') as file:
            file.write(data)
    else:
        raise ValueError(f"Unknown mode: {mode}")
