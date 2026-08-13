# PII Redactor - Document Privacy Tool

A powerful tool to automatically detect and redact Personally Identifiable Information (PII) from Word documents using regex patterns and Named Entity Recognition (NER).

## Features

- **Automatic PII Detection**: Identifies and replaces:
  - Names & Organizations (using spaCy NER)
  - Email addresses
  - Phone numbers
  - Credit card numbers
  - SSN / PAN numbers
  - Aadhaar numbers
  - IP addresses
  - Dates of birth

- **Consistent Replacements**: Uses fake data that remains consistent throughout the document
- **In-place Modifications**: Overwrites the original file with redacted content
- **Web Interface**: Easy-to-use HTML interface with drag-and-drop support

## Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Setup

1. **Clone or download this repository**

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install python-docx spacy faker flask
python3 -m spacy download en_core_web_sm
```

## Usage

### Option 1: Web Interface (Recommended)

1. **Start the server**:
```bash
python3 server.py
```

2. **Open in browser**:
Visit `http://localhost:5000` in your web browser

3. **Upload and redact**:
   - Select or drag a .docx file
   - Click "Redact Document"
   - The file will be modified in-place

### Option 2: Command Line

```bash
python3 redactor.py "path/to/your/document.docx"
```

The document will be modified in-place with all PII redacted.

## Files

- **redactor.py**: Core redaction engine
- **server.py**: Flask web server
- **index.html**: Web interface
- **requirements.txt**: Python dependencies
- **README.md**: This file

## How It Works

1. **Regex-based Detection**: Matches common PII patterns (emails, phones, IPs, etc.)
2. **NER-based Detection**: Uses spaCy to identify named entities (persons, organizations, locations)
3. **Fake Data Generation**: Creates consistent fake replacements using the Faker library
4. **Document Processing**: 
   - Processes all paragraphs in the document
   - Processes all tables (including nested content)
   - Preserves document formatting

## Example

**Before:**
```
Contact John Smith at john.smith@company.com or +91-9876543210
His PAN is ABCDE1234F
Company: Acme Corporation, located in New York
```

**After:**
```
Contact Fernando Gómez at melissa87@example.net or +91-8765432109
His PAN is XYZAB5678M
Company: Greenfield Industries, located in Austin
```

## Performance Notes

- Processing time depends on document size and complexity
- Large documents with many tables may take a few minutes
- All processing is done locally (no cloud uploads)

## Security & Privacy

- No data is sent to external servers
- Original file is backed up (consider manual backups for important documents)
- All PII is replaced with synthetic data
- The replacement mapping is kept in memory during processing

## Requirements

See `requirements.txt` for full list:
- python-docx: For Word document handling
- spacy: For Named Entity Recognition
- faker: For generating fake data
- flask: For the web server (optional, only needed for web interface)

## Troubleshooting

### "Module not found" error
```bash
pip install -r requirements.txt
```

### spaCy model not found
```bash
python3 -m spacy download en_core_web_sm
```

### Port 5000 already in use
Edit `server.py` and change the port number in the last line:
```python
app.run(debug=True, host='127.0.0.1', port=5001)  # Change 5000 to 5001
```

### Document not modifying
- Ensure you have write permissions for the file
- Close the document if it's open in Word
- Try running from the command line to see error messages

## License

MIT License - Feel free to use and modify

## Author

Created as a privacy protection tool
