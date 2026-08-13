#!/usr/bin/env python3
"""
Simple Flask server for the PII Redactor tool.
Run this with: python3 server.py
Then open http://localhost:5000 in your browser.
"""

from flask import Flask, render_template_string, request, jsonify
import os
import sys
from pathlib import Path
from redactor import process_word_document

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB max file size
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'uploads')

# Create uploads folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Read the HTML file
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(SCRIPT_DIR, 'index.html')

@app.route('/')
def index():
    """Serve the main HTML page."""
    try:
        with open(HTML_FILE, 'r') as f:
            html_content = f.read()
        return html_content
    except FileNotFoundError:
        return "Error: index.html not found", 404

@app.route('/redact', methods=['POST'])
def redact():
    """Handle file upload and redaction."""
    try:
        # Check if file is in request
        if 'file' not in request.files:
            return "No file provided", 400
        
        file = request.files['file']
        
        if file.filename == '':
            return "No file selected", 400
        
        if not file.filename.endswith('.docx'):
            return "Only .docx files are supported", 400
        
        # Save uploaded file
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # If file exists, create a backup or overwrite
        file.save(filepath)
        
        # Process the document (modifies in-place)
        success = process_word_document(filepath)
        
        if success:
            return jsonify({
                'status': 'success',
                'message': f'Document redacted successfully',
                'file': filename
            }), 200
        else:
            return "Error processing document", 500
            
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return f"Error: {str(e)}", 500

@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    print("=" * 50)
    print("PII Redactor Server")
    print("=" * 50)
    print(f"Server running at: http://localhost:5000")
    print(f"Upload folder: {os.path.abspath(app.config['UPLOAD_FOLDER'])}")
    print("\nPress CTRL+C to stop the server")
    print("=" * 50)
    
    app.run(debug=True, host='127.0.0.1', port=5000)
