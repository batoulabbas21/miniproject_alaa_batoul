import sys
import os
import fitz  # PyMuPDF
from rule_engine import evaluate_rules

def analyze_file(file_path):
    text = ""
    if file_path.lower().endswith(".pdf"):
        doc = fitz.open(file_path)
        for page in doc:
            text += page.get_text()
    elif file_path.lower().endswith(".txt"):
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
    else:
        return ["Unsupported file type. Use PDF or TXT."]
    
    return evaluate_rules(text)

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_txt(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python analyzer.py <file_path>")
        return

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print(f"File '{file_path}' not found.")
        return

    if file_path.lower().endswith('.pdf'):
        text = extract_text_from_pdf(file_path)
    elif file_path.lower().endswith('.txt'):
        text = extract_text_from_txt(file_path)
    else:
        print("Unsupported file type. Please use a PDF or TXT file.")
        return

    alerts = evaluate_rules(text)

    print("Generated Alerts:")
    if alerts:
        for alert in alerts:
            print("- " + alert)
    else:
        print("✅ No alerts triggered.")

if __name__ == "__main__":
    main()
