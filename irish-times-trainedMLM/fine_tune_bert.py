import pandas as pd
from datasets import Dataset
from transformers import BertTokenizerFast, BertForMaskedLM, Trainer, TrainingArguments
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# when im actually fine tuning it
# cd E:\work\fake-news-bert
# C:\Users\shamm\AppData\Local\Programs\Python\Python312\python.exe fine_tune_bert.py
# uvicorn app:app --reload
# uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

# get the irishtimes csv and put in the headers
df = pd.read_csv("training_data/new_IrishTimes_train_labeled.csv", names=["text", "label"])

# analyse the first 10k rows because my gpu will explode otherwise
subset_df = df.head(10000)

# get rid rows with missing text
subset_df = subset_df.dropna(subset=["text"])

# keep only the left text column, "REAL" was added when i was planning to do a real vs fake headline checker
texts_only_df = subset_df[["text"]]

# convert to HuggingFace dataset
dataset = Dataset.from_pandas(texts_only_df)

# load tokenizer and model (BERT base uncased)
tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased')
model = BertForMaskedLM.from_pretrained('bert-base-uncased')

# tokenize function with masking for MLM
def tokenize_function(examples):
    # tokenize input texts
    outputs = tokenizer(examples["text"], truncation=True, padding="max_length", max_length=64)
    # prepare masked language modeling labels using tokenizer mask function
    inputs = outputs["input_ids"]
    labels = inputs.copy()

    # ?use the tokenizer's built-in data collator for MLM masking in Trainer?
    return outputs

# tokenize the dataset
tokenized_dataset = dataset.map(tokenize_function, batched=True, remove_columns=["text"])

# split train / validation (optional)
train_size = int(0.9 * len(tokenized_dataset))
train_dataset = tokenized_dataset.select(range(train_size))
eval_dataset = tokenized_dataset.select(range(train_size, len(tokenized_dataset)))

# training arguments (lowered because my pc would freeze)
training_args = TrainingArguments(
    output_dir="./bert-mlm",
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    eval_strategy="epoch",
    save_strategy="epoch",
    logging_dir="./logs",
    logging_steps=1000,
    save_total_limit=2,
    load_best_model_at_end=True,
    report_to="none",
)

from transformers import DataCollatorForLanguageModeling

# ?data collator will handle masking tokens dynamically?
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=True, mlm_probability=0.15)

# initialize the trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    data_collator=data_collator,
)

# run the trainer
trainer.train()

# save the model + tokenizer
model.save_pretrained("./bert-mlm")
tokenizer.save_pretrained("./bert-mlm")

print("trainings done")
