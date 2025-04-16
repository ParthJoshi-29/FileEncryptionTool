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

@app.route("/", methods=["GET", "POST"])
def index():
    download_file = None
    if request.method == "POST":
        action = request.form.get("action")
        uploaded_file = request.files.get("file")

        if uploaded_file:
            filename = secure_filename(uploaded_file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            uploaded_file.save(file_path)

            if action == "encrypt":
                generate_key()
                key = load_key()
                new_filename = encrypt(file_path, key)
                flash("File encrypted successfully!", "success")
                download_file = new_filename
            elif action == "decrypt":
                if not os.path.exists(KEY_FILE):
                    flash("Key not found for decryption.", "danger")
                else:
                    key = load_key()
                    result = decrypt(file_path, key)
                    if result:
                        flash("File decrypted successfully!", "success")
                        download_file = result
                    else:
                        flash("Invalid key or file. Decryption failed.", "danger")

            return render_template("index.html", download_file=download_file)
        else:
            flash("No file selected.", "warning")
            return redirect("/")
    return render_template("index.html", download_file=download_file)

@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename, as_attachment=True)

if _name_ == "_main_":
    app.run(debug=True)

encrypt-decrypt-flask
