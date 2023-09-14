import spacy

nlp = spacy.load("en_core_web_sm")

text = '''Supply and Installation of Facial Recognition and Biometric Attendance data RecordingSystem along with Printer, access cards, Ethernet Switch and cable as perSpecifications attached. NOTE: Firms shall provide clause wise compliance for theabove mentioned specification duly attaching the separate document and their offeredmake and model to be specified along with product details in the form of catalogue,otherwise offers will be summarily rejected.'''

#process the text
doc = nlp(text=text)

#extract sentences containing the desired keywords
desired_sentences = []
for sentence in doc.sents:
    if 'Facial Recognition' in sentence.text or 'Biometric Attendance' in sentence.text:
        desired_sentences.append(sentence)

#concatenate the desired sentences into summary text
summary_text = ''
for sentence in desired_sentences:
    summary_text += sentence.text + ' '

print(summary_text)
