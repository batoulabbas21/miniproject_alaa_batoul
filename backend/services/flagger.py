from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("my_models/Bio_ClinicalBERT", local_files_only=True)
model = AutoModel.from_pretrained("my_models/Bio_ClinicalBERT", local_files_only=True)

def flag_risks(text):
    import re
    flags = []
    if re.search(r"\bsepsis\b", text, re.IGNORECASE):
        flags.append("Sepsis detected")
    if re.search(r"\bsystolic\b", text, re.IGNORECASE) and re.search(r"\b(1[8-9]\d|2\d\d)\b", text):
        flags.append("Hypertensive Crisis (systolic >= 180)")
    if re.search(r"\bHbA1c\b.*?(\d{2,})", text):
        flags.append("Possible diabetes (High HbA1c level)")
    return flags
