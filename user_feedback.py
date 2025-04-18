# Inside the index() function
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

# In case no file is selected
flash("No file selected.", "warning")