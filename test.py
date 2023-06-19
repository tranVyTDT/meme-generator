from docx import Document
file_path = "_data\DogQuotes\DogQuotesDOCX.docx"

doc = Document(file_path)

for paragraph in doc.paragraphs:
    text = paragraph.text
    print(text)
  