# file_operations.py

def write_to_file(file_name, data):
    with open(file_name, 'w') as file:
        file.write(data)
