from flask import Flask, request, redirect, url_for, render_template
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # Folder where files are saved

# Ensure upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def upload_form():
    return render_template('upload.html')  # HTML page with a file upload form

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return "File uploaded successfully"

if __name__ == "__main__":
    app.run(debug=True)
