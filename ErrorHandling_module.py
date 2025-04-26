import os
import logging
from flask import Flask, request, flash, redirect
from werkzeug.utils import secure_filename
from cryptography.fernet import Fernet, InvalidToken

app = Flask(__name__)
app.secret_key = "your_secret_key"
app.config['UPLOAD_FOLDER'] = "uploads"
KEY_FILE = "key.key"

# Setup logging
logging.basicConfig(filename='error.log', level=logging.INFO)

# Load key from file
def load_key():
    return open(KEY_FILE, "rb").read()

# Generate a new key and save
def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

def encrypt(file_path, key):
    try:
        f = Fernet(key)
        with open(file_path, "rb") as file:
            file_data = file.read()
            encrypted_data = f.encrypt(file_data)
        encrypted_path = file_path + ".enc"
        with open(encrypted_path, "wb") as file:
            file.write(encrypted_data)
        return os.path.basename(encrypted_path)
    except Exception as e:
        logging.error(f"Encryption failed: {e}")
        return None

def decrypt(file_path, key):
    try:
        f = Fernet(key)
        with open(file_path, "rb") as file:
            encrypted_data = file.read()
            decrypted_data = f.decrypt(encrypted_data)

        decrypted_path = file_path[:-4] if file_path.endswith(".enc") else file_path + ".dec"
        with open(decrypted_path, "wb") as file:
            file.write(decrypted_data)
        return os.path.basename(decrypted_path)
    except InvalidToken:
        logging.warning("Invalid token: wrong key or corrupted file.")
        return None
    except Exception as e:
        logging.error(f"Decryption failed: {e}")
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    download_file = None
    if request.method == "POST":
        action = request.form.get("action")
        uploaded_file = request.files.get("file")

        if not uploaded_file or uploaded_file.filename == "":
            flash("No file uploaded!", "danger")
            return redirect(request.url)

        filename = secure_filename(uploaded_file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        uploaded_file.save(file_path)

        if action == "encrypt":
            try:
                generate_key()
                key = load_key()
                new_filename = encrypt(file_path, key)
                if new_filename:
                    flash("File encrypted successfully!", "success")
                    download_file = new_filename
                else:
                    flash("Encryption failed. Please try again.", "danger")
            except Exception as e:
                logging.error(f"Unexpected error during encryption: {e}")
                flash("Something went wrong during encryption.", "danger")

        elif action == "decrypt":
            if not os.path.exists(KEY_FILE):
                flash("Key not found for decryption.", "danger")
                return redirect(request.url)
            try:
                key = load_key()
                result = decrypt(file_path, key)
                if result:
                    flash("File decrypted successfully!", "success")
                    download_file = result
                else:
                    flash("Invalid key or file. Decryption failed.", "danger")
            except Exception as e:
                logging.error(f"Unexpected error during decryption: {e}")
                flash("Something went wrong during decryption.", "danger")

    return "Flask UI for FileEncryptionTool here..."  # Placeholder response

