from PyPDF2 import PdfReader
import os


# Import the library
from tkinter import *
from tkinter import filedialog

from google.cloud import translate_v2

import threading

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"googlekey.json"
allar = ""


def transtlate(msg, sc="ar"):
    transtlate_client = translate_v2.Client()

    text = msg

    responce = transtlate_client.translate(text, target_language=sc)
    # print(responce["translatedText"])
    return responce["translatedText"]


def getAllTexts(pdf):
    text = ""
    pdf_reader = PdfReader(pdf)
    for page in pdf_reader.pages[31:300]:
        text += page.extract_text()
        allar = transtlate(text)
        write(allar + "\n")
        text = "\n"

    return text


def write(text):
    with open("text.txt", "a", encoding="utf-8") as f:
        f.write(text)
        f.close()


getAllTexts("Malfuzat-1.pdf")

# pdf_reader = PdfReader("Malfuzat-1.pdf")

# for page in pdf_reader.pages[31:300]:
#     print(page["/StructParents"])


# # Create an instance of window
# win = Tk()

# # Set the geometry of the window
# win.geometry("700x300")

# # Create a label
# Label(win, text="Click the button to open a dialog", font="Arial 16 bold").pack(pady=15)


# # Function to open a file in the system
# def open_file():
#     filepath = filedialog.askopenfilename(
#         title="Open a Text File",
#         filetypes=(("PDF File", "*.pdf"), ("All Files", "*.*")),
#     )
#     file = open(filepath, "rb")
#     getAllTexts(file)
#     file.close()
#     win.quit()


# # Create a button to trigger the dialog
# button = Button(win, text="Open", command=open_file)
# button.pack()

# win.mainloop()
