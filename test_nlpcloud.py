import nlpcloud
from time import time


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)


if __name__ == '__main__':
    client = nlpcloud.Client("finetuned-gpt-neox-20b", "TOKEN HERE", gpu=True, lang="en")  # dont forget to update your token
    functions = open_file('objective_functions.txt').splitlines()
    for f in functions:
        prompt = open_file('prompt_consequences.txt').replace('<<FUNCTION>>', f)
        result = client.generation(prompt,min_length=10,max_length=500,length_no_input=True,remove_input=False,end_sequence=None,top_p=1,temperature=0.7,top_k=50,repetition_penalty=1,length_penalty=1,do_sample=True,early_stopping=False,num_beams=1,no_repeat_ngram_size=0,num_return_sequences=1,bad_words=None,remove_end_sequence=False)
        print('\n\n',result['generated_text'])
        filename = 'neox_%s_%s.txt' % (f.replace('To','').replace(' ','')[0:16], time())
        save_file('results/%s' % filename, result['generated_text'])