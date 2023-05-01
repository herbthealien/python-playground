import tkinter as tk
from tkinter import *
from langchain.llms import OpenAI

llm=OpenAI(temperature=0.9)

text="You are Arnold Schwarzenegger and you're telling me my fortune."

root=Tk()
root.title("The Fortunator")
root.geometry('640x480')

lbl = Label(root, text = llm(text))
lbl.grid()

root.mainloop()