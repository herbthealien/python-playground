mport tkinter as tk
from tkinter import *
from langchain.llms import OpenAI
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO

llm=OpenAI(temperature=0.9)

text="Tell me my future while talking like Arnold Schwarzenegger, writing your text out in his thick austrian accent."

root=Tk()
root.title("The Fortunator")
root.geometry('640x480')

url="https://upload.wikimedia.org/wikipedia/commons/c/cf/Schwarzenegger_Dec_2015.jpg"
u=urlopen(url)
raw_data=u.read()
u.close()

im = Image.open(BytesIO(raw_data))
imr = im.resize((150,200))
photo = ImageTk.PhotoImage(imr)

label=Label(root, wraplength=500, justify="center", image=photo)
label.image=photo
label.pack(pady=20)

arnold=Label(root, text="Arnold is more than happy to tell you your fortune, if you ask.", wraplength=500, justify="center")
arnold.pack(pady=20)

def fortune():
   arnold["text"] = llm(text)

B = Button(root, text='Ask Arnold For Your Fortune', command=fortune)
B.pack(pady=20)
root.mainloop()