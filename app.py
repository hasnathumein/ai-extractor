from flask import Flask, request, render_template, send_file
import os
import fitz
from PIL import Image
import pytesseract
from io import BytesIO
from datetime import datetime

# Tesseract config
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
Image.MAX_IMAGE_PIXELS = None

# Flask app
app = Flask(__name__)

# Folders
UPLOAD_FOLDER = 'uploads'
EMAIL_FOLDER = 'emails'
DOC_FOLDER = 'documents'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(EMAIL_FOLDER, exist_ok=True)
os.makedirs(DOC_FOLDER, exist_ok=True)

# Text extractors
def extract_text_from_pdf(filepath):
    doc = fitz.open(filepath)
    return "".join([page.get_text() for page in doc])

def extract_text_from_image(filepath):
    image = Image.open(filepath)
    return pytesseract.image_to_string(image)

@app.route('/', methods=['GET', 'POST'])
def index():
    extracted_text = None
    if request.method == 'POST':
        file = request.files['document']
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            ext = file.filename.lower().split('.')[-1]
            if ext == 'pdf':
                extracted_text = extract_text_from_pdf(filepath)
            elif ext in ['jpeg', 'jpg', 'png']:
                extracted_text = extract_text_from_image(filepath)
            else:
                extracted_text = "❌ Unsupported file format."
    return render_template('index.html', extracted_text=extracted_text)
@app.route('/api-docs')
def api_docs():
    return render_template('api-docs.html')

@app.route('/save_email_and_download', methods=['POST'])
def save_email_and_download():
    data = request.get_json()
    email = data.get('email')
    content = data.get('content')

    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

    # Save email
    with open(os.path.join(EMAIL_FOLDER, f"{timestamp}_{email.replace('@', '_at_')}.txt"), 'w') as f:
        f.write(email)

    # Save document
    with open(os.path.join(DOC_FOLDER, f"{timestamp}_document.txt"), 'w') as f:
        f.write(content)

    # Create DOC for download
    doc_stream = BytesIO()
    doc_stream.write(content.encode('utf-8'))
    doc_stream.seek(0)
    return send_file(doc_stream, mimetype='application/msword', as_attachment=True, download_name='extracted_text.doc')

if __name__ == '__main__':
    app.run(debug=True)
