import spacy
from heapq import nlargest

nlp = spacy.load("en_core_web_sm")

def summarize_text(text):
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

    return summary_text

text = '''Supply and Installation of Facial Recognition and Biometric Attendance data RecordingSystem along with Printer, access cards, Ethernet Switch and cable as perSpecifications attached. NOTE: Firms shall provide clause wise compliance for theabove mentioned specification duly attaching the separate document and their offeredmake and model to be specified along with product details in the form of catalogue,otherwise offers will be summarily rejected.'''

summary = summarize_text(text)

print(summary)
