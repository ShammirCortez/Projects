from transformers import BertTokenizerFast

tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased')
file_path = "../training_data/new_IrishTimes_train_labeled.csv"

#code to find max tokens in a piece of data so i can configure my fine-tuning correctly and not overdo it and destroy my pc

longest_line = ""
max_token_len = 0
long_lines = 0

with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip("\n")
        tokens = tokenizer.tokenize(line)
        if len(tokens) > max_token_len:
            max_token_len = len(tokens)
            longest_line = line
        if len(tokens) > 16:
            long_lines += 1

print(f"Longest line length (tokens): {max_token_len}")
print(f"Longest line:\n{longest_line}")
print(f"Lines longer than 16 tokens: {long_lines}")
