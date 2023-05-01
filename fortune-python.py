import tkinter as tk
from tkinter import *
from langchain.llms import OpenAI

llm=OpenAI(temperature=0.9)

text="Tell me my future while talking like Arnold Schwarzenegger, writing your text out in his thick austrian accent."

root=Tk()
root.title("The Fortunator")
root.geometry('640x480')

lbl = Label(root, text = llm(text), wraplength=500, justify="center")
lbl.grid()
 
root.mainloop()