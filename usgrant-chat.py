import tkinter as tk
from tkinter import *
from langchain.llms import OpenAI
from langchain import PromptTemplate
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO

template = """Answer the question based on the knowledge that you are Ulysses S. Grant, 
18th president of the United States. You write exactly as he did when he was alive, but 
you have knowledge of modern human history as well as past, and have developed opinions
on modern culture based on inferences from your lifetime.

Question: {query}

Answer: """

prompt_template = PromptTemplate(
    input_variables=["query"],
    template=template
)

text="You are Ulysses S. Grant, 18th president of the United States. You write exactly as he did when he was alive, but you have knowledge of modern human history as well as past."

llm=OpenAI(temperature=0.9)

root=Tk()
root.title("Ulysses S. Grant's Reddit AMA")
root.geometry('640x480')

url="https://upload.wikimedia.org/wikipedia/commons/1/13/Ulysses_S._Grant%2C_1876.jpg"
u=urlopen(url)
raw_data=u.read()
u.close()

im = Image.open(BytesIO(raw_data))
imr = im.resize((150,200))
photo = ImageTk.PhotoImage(imr)

label=Label(root, wraplength=500, justify="center", image=photo)
label.image=photo
label.pack(pady=20)

ugrant=Label(root, text="Hi Reddit, Ulysses S. Grant here. AMA", wraplength=500, justify="center")
ugrant.pack(pady=20)

inputtxt = tk.Text(root,
                   height = 5,
                   width = 20)
  
inputtxt.pack()


def grantReply():
   inp = inputtxt.get(1.0, "end-1c")
   ugrant["text"] = llm(prompt_template.format(query=inp))


B = Button(root, text='Ask Ulysses S. Grant', command=grantReply)
B.pack(pady=20)
root.mainloop()