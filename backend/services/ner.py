from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch

BASE = "my_models/biomedical-ner-all"

tokenizer = AutoTokenizer.from_pretrained(BASE, local_files_only=True)
model = AutoModelForTokenClassification.from_pretrained(BASE, local_files_only=True)
model.eval()

def extract_entities(text: str):
    tokens = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        logits = model(**tokens).logits
    preds = torch.argmax(logits, dim=-1)[0]
    input_ids = tokens["input_ids"][0]
    words = tokenizer.convert_ids_to_tokens(input_ids)
    labels = [model.config.id2label[p.item()] for p in preds]
    results = []
    for word, label in zip(words, labels):
        if label != "O" and not word.startswith("▁"):
            continue  # Skip non-entity subwords
        results.append({"token": word, "label": label})
    return results
