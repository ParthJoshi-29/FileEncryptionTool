def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
        
def load_key():
    return open(KEY_FILE, "rb").read()