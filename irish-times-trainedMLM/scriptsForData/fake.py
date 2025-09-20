infile = '../training_data/irish_fake_news.csv'
outfile = '../training_data/irish_fake_news_labeled.csv'

#when i was originally doing a REAL or FAKE headline test, code to add ",Fake" to the fake dataset, not used anymore

with open(infile, 'r', encoding='utf-8') as fin, open(outfile, 'w', encoding='utf-8') as fout:
    for i, line in enumerate(fin, 1):
        line = line.strip()

        if not line.endswith(',FAKE'):
            print(f"Line {i} does not end with ',FAKE': {line}")
            #optionally skip or handle differently here
            continue

        text = line[:-5]

        text_cleaned = text.replace(',', '')

        fout.write(f"{text_cleaned},FAKE\n")
