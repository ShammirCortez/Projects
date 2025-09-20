#https://www.kaggle.com/datasets/manhdodz249/irish-times-dataset-for-topic-model/data?select=new_IrishTimes_train.txt

infile = '../training_data/new_IrishTimes_train.txt'
outfile = '../training_data/new_IrishTimes_train_labeled.csv'

#adding ",REAL" to the real dataset

def fix_encoding(line):
    try:
        return line.encode('latin1').decode('utf-8')
    except (UnicodeEncodeError, UnicodeDecodeError):
        return line

with open(infile, 'r', encoding='utf-8', errors='ignore') as fin, \
     open(outfile, 'w', encoding='utf-8') as fileout:
    fileout.write("text,label\n")
    for line in fin:
        line = line.strip()
        if line:
            fixed_line = fix_encoding(line)
            fileout.write(f"{fixed_line},REAL\n")
