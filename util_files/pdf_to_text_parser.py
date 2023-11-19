import PyPDF2
import os

filename = 'C:/Users/user/OneDrive - Files/Desktop/API Projects/exam_paper_to_API/data'
filepath = 'data/'




def pdf_to_word(folder):
  files = os.listdir(folder)
  output = ''
  for file in files:
    with open(''.join([filepath, file]), 'rb') as pdf_file:
      pdf_reader = PyPDF2.PdfReader(pdf_file)
      text = ''
      for i in range(len(pdf_reader.pages)):
        pages = pdf_reader.pages[i]
        text += pages.extract_text()
    output += text
  return output
  
print(pdf_to_word(filename))
