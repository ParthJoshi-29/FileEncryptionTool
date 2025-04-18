def encrypt(file_path, key):
    f = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)
    encrypted_path = file_path + ".enc"
    with open(encrypted_path, "wb") as file:
        file.write(encrypted_data)
    return os.path.basename(encrypted_path)

def decrypt(file_path, key):
    f = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
        try:
            decrypted_data = f.decrypt(encrypted_data)
        except InvalidToken:
            return None
    # Remove .enc extension for the decrypted file
    if file_path.endswith(".enc"):
        decrypted_path = file_path[:-4]
    else:
        decrypted_path = file_path + ".dec"
    with open(decrypted_path, "wb") as file:
        file.write(decrypted_data)
    return os.path.basename(decrypted_path)