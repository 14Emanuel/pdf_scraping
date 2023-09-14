import spacy

nlp = spacy.load("en_core_web_sm")

text = '''Supply and Installation of Facial Recognition and Biometric Attendance data RecordingSystem along with Printer, access cards, Ethernet Switch and cable as perSpecifications attached. NOTE: Firms shall provide clause wise compliance for theabove mentioned specification duly attaching the separate document and their offeredmake and model to be specified along with product details in the form of catalogue,otherwise offers will be summarily rejected.'''

#process the text
doc = nlp(text=text)

#get the word count
word_dict = {}

for word in doc:
    word = word.text.lower()

    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1


#print(word_dict)

#Score sentences

# (index, sentence, score)
sentences = []

sentence_score = 0

for i, sentence in enumerate(doc.sents):
    for word in sentence:
        word = word.text.lower()
        sentence_score += word_dict[word]

    sentences.append((i, sentence.text.replace("\n", " "), sentence_score/len(sentence)))

#print(sentences)

#sort sentences
sorted_sentence = sorted(sentences, key=lambda x: -x[2])

top_three = sorted(sorted_sentence[:3], key=lambda x: x[0])

summary_text = ""

for sentence in top_three:
    summary_text += sentence[1] + " "

print(summary_text)

