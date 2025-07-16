from transformers import AutoTokenizer, AutoModelForCausalLM, GPT2LMHeadModel, GPT2Tokenizer, LlamaTokenizer
import torch
import os

MODEL_NAME = "gpt2"
LOCAL_PATH = "./local_models/gpt2"

def download_model_locally() -> None:
    if not os.path.exists(LOCAL_PATH) or not os.listdir(LOCAL_PATH):
        print(f"Downloading {MODEL_NAME} to {LOCAL_PATH}")
        AutoTokenizer.from_pretrained(MODEL_NAME, cache_dir=LOCAL_PATH)
        AutoModelForCausalLM.from_pretrained(MODEL_NAME, cache_dir=LOCAL_PATH)
        print("Download complete")


def load_model():
    download_model_locally()
    tokenizer = GPT2Tokenizer.from_pretrained(MODEL_NAME)
    tokenizer.pad_token = tokenizer.eos_token

    model = GPT2LMHeadModel.from_pretrained(MODEL_NAME)
    model.to("cuda" if torch.cuda.is_available() else "cpu")
    model.eval()

    return tokenizer, model