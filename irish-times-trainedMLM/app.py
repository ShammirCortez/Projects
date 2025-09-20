from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from transformers import BertTokenizerFast, BertForMaskedLM
import torch
import pathlib
import math

#uvicorn app:app --reload

app = FastAPI()

app.mount("/static", StaticFiles(directory="html"), name="static")

# html
@app.get("/", response_class=HTMLResponse)
async def read_root():
    index_path = pathlib.Path("./html/index.html") 
    return index_path.read_text(encoding="utf-8")

# load the fine-tuned bert model
tokenizer = BertTokenizerFast.from_pretrained("./bert-mlm")
model = BertForMaskedLM.from_pretrained("./bert-mlm")
model.eval()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# put in schema
class NewsItem(BaseModel):
    text: str

def compute_mlm_score(text: str) -> float:
    # computes MLM score, lower means more likely
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=64)
    input_ids = inputs["input_ids"].to(device)
    attention_mask = inputs["attention_mask"].to(device)

    # shift the inputs to create labels
    labels = input_ids.clone()

    with torch.no_grad():
        outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss
        score = loss.item()

    return score

@app.post("/predict")
def predict(news: NewsItem):
    score = compute_mlm_score(news.text.strip())
    return {"score": score}
