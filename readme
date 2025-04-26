Hello, This is a readme file which includes information and instructions to use the File Encryption/Decryption Tool!

# 🔒 File Encryption and Decryption Web Application

This project is a simple **Flask-based web application** that allows users to **upload a file**, **encrypt** it securely, and **decrypt** it back using **Fernet symmetric encryption** from the `cryptography` library.

---

## 📂 Features

- Upload a file through the browser.
- Encrypt the uploaded file securely.
- Decrypt an encrypted file (.enc) back to its original form.
- Download the encrypted or decrypted file.
- User-friendly flash messages for success, warnings, or errors.

---

## 🛠 Technologies Used

- **Python 3**
- **Flask** (Backend web framework)
- **Cryptography (Fernet)** (For encryption and decryption)
- **Werkzeug** (For secure filename handling)
- **HTML (with Flask templates)**
- **CSS 

---

## 📋 How to Run the Project

### 1. Clone or Download the Project
```bash
cd path_to_your_folder
```

### 2. Set up a Virtual Environment (Optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate    # On Windows
```

### 3. Install Required Packages
```bash
pip install Flask cryptography
```

### 4. Run the Application
```bash
python app.py
```
or
```bash
set FLASK_APP=app.py
set FLASK_ENV=development
python -m flask run
```

The application will start on:

> http://127.0.0.1:5000/

---

## 📁 Project Structure

```
project/
│
├── uploads/               # Folder to store uploaded/encrypted/decrypted files
├── templates/
│   └── index.html          # Frontend page
├── app.py                  # Main application file
├── Secret.key              # Encryption key (generated automatically)
├── README.md               # Project documentation (this file)
```

---

## 📌 How It Works

1. Upload a file using the form.
2. Choose **Encrypt** or **Decrypt** action.
3. If encrypting:
   - A new **Secret.key** file is generated.
   - The uploaded file is encrypted and available for download.
4. If decrypting:
   - The existing **Secret.key** is used to decrypt the file.
   - Decrypted file is available for download.

---

## ⚡ Important Points

- The encryption key is generated and saved as `Secret.key` when encrypting.
- Without the correct key, decryption will **fail**.
- Always keep the `Secret.key` file safe after encryption.
- The application automatically handles missing key errors or invalid file decryption.

---

## 📚 Requirements

- Python 3.x
- Flask
- Cryptography
- Werkzeug

Install them using:
```bash
pip install -r requirements.txt
```
*(You can create a `requirements.txt` with these names if needed.)*

---

## 🚀 Importance of this Tool

1. **Data Protection**  
   ➔ It ensures that sensitive files are protected by encryption, preventing unauthorized access.

2. **Confidentiality**  
   ➔ Only users with the correct secret key can decrypt and access the original file, maintaining privacy.

3. **User-Friendly**  
   ➔ Provides a simple web interface for non-technical users to easily encrypt and decrypt files without coding knowledge.

4. **Security Against Cyber Threats**  
   ➔ In case of data breaches or hacking attempts, encrypted files remain unreadable and safe.

5. **Key Management Awareness**  
   ➔ Educates users about the importance of managing and securing encryption keys properly.

6. **File Sharing Security**  
   ➔ Allows users to encrypt files before sharing them over insecure channels like email or cloud services.

7. **Real-World Application**  
   ➔ Similar encryption methods are used in industries like banking, healthcare, and government for protecting critical information.

8. **Lightweight and Fast**  
   ➔ The tool is lightweight, doesn't require a heavy setup, and processes encryption/decryption quickly.

9. **Local Processing**  
   ➔ Files are processed locally (on the user's system), ensuring no file is uploaded to any external server, enhancing privacy.

10. **Foundation for Larger Projects**  
    ➔ This project can be expanded into a full-fledged secure storage system or integrated into bigger applications requiring file security.

---

ensure to install all the libraries required before using!
