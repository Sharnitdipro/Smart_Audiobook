import pyttsx3
import PyPDF2
book = open('report.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
talk = pyttsx3.init()
page = pdfReader.getPage(9)
text = page.extractText()
talk.say(text)
talk.runAndWait()