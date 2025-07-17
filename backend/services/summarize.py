from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import warnings
import torch
import re

warnings.filterwarnings("ignore", category=UserWarning)

try:
    tokenizer = AutoTokenizer.from_pretrained("my_models/bart-large-cnn", local_files_only=True)
    model = AutoModelForSeq2SeqLM.from_pretrained("my_models/bart-large-cnn", local_files_only=True)
    model.config.forced_bos_token_id = model.config.bos_token_id
except Exception as e:
    raise RuntimeError(f"Summarization model load failed: {e}")

def clean_input(text: str) -> str:
    text = text.strip()
    text = text.replace("\n", " ").replace("•", "-")
    text = re.sub(r"http\S+", "", text)  # remove URLs
    text = re.sub(r"\s+", " ", text)     # normalize whitespace
    return text

def summarize_text(text: str, min_length=50, max_length=250) -> str:
    text = clean_input(text)

    if len(text.split()) < 50:
        return text  # Too short to summarize

    inputs = tokenizer.encode(text, return_tensors="pt", truncation=True, max_length=1024)
    summary_ids = model.generate(
        inputs,
        max_length=max_length,
        min_length=min_length,
        length_penalty=1.0,             # Less aggressive shortening
        num_beams=5,                    # More diverse output
        early_stopping=True,
        no_repeat_ngram_size=3          # Avoid repeating phrases
    )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary.strip()
