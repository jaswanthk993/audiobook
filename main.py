import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename

# Ask the user to select a PDF file
book = askopenfilename()

# Initialize the PDF reader
pdfreader = PyPDF2.PdfReader(open(book, 'rb'))

# Get the number of pages in the PDF
pages = len(pdfreader.pages)

# Initialize the text-to-speech engine
player = pyttsx3.init()

# Iterate through each page and extract text
for num in range(pages):
    page = pdfreader.pages[num]
    text = page.extract_text()

    # Read the extracted text
    player.say(text)
    player.runAndWait()

# Close the PDF file
pdfreader.stream.close()
