import spacy
from heapq import nlargest

nlp = spacy.load("en_core_web_sm")

text = '''Speed Sensor with cable (With connector [Speed Sensor with cable (With connector Newtype) to escort Drg no. 1J112000023 MAKE: ESCORTS ONLY.]'''

# process the text
doc = nlp(text)

# get the word count
word_dict = {}

for word in doc:
    word = word.text.lower()

    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

# score sentences
sentences = []

for i, sentence in enumerate(doc.sents):
    score = 0

    for word in sentence:
        word = word.text.lower()
        score += word_dict[word]

    sentences.append((i, sentence.text.replace("\n", " "), score/len(sentence)))

# sort sentences
sorted_sentences = nlargest(int(len(sentences)*0.5), sentences, key=lambda x: x[2])

# create summary
summary_text = ""

for sentence in sorted(sorted_sentences, key=lambda x: x[0]):
    summary_text += sentence[1] + " "

print(summary_text)
 