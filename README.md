🧠 AI Document Extractor

A clean and modern Flask-based tool for extracting text from uploaded PDF or image documents. Users can upload files, extract and preview text, download results as a .doc file, and even log their email.

🚀 Features

📄 Upload files (PDF, JPG, JPEG, PNG)

🔍 Extract text using PyMuPDF and Tesseract OCR

👁️ Preview extracted text in the browser

⬇️ Download extracted text as .doc

📧 Popup email capture before download

🔥 Real-time toast messages & animations

🗂 Auto-delete files older than 7 days

🛡️ Session logging with IP & timestamp

📸 Preview



⚙️ Tech Stack

Python 3.10

Flask

PyMuPDF (fitz) for PDFs

Tesseract OCR via pytesseract for images

HTML5 + Vanilla JS + CSS Animations

📂 Folder Structure

ai-document-extractor/
├── app.py                   # Flask backend
├── templates/
│   └── index.html           # Frontend UI
├── uploads/                 # Temporary user uploads
├── emails/                  # Captured email logs
├── documents/               # Extracted .doc logs
├── session_logs.txt         # IP & file upload logs
├── .gitignore
└── README.md

🛠️ Setup Instructions

git clone https://github.com/your-username/ai-document-extractor.git
cd ai-document-extractor
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py

Visit: http://127.0.0.1:5000

⚠️ Requires Tesseract OCR installed locally. Download from: https://github.com/tesseract-ocr/tesseract

🧪 Example Files

sample.pdf – basic PDF test

invoice.png – OCR image test

🏷 Badges





📄 License

This project is licensed under the MIT License.

👨‍💻 Author

Built with ❤️ by Hasnat Ali Ibrar

