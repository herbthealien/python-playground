import tkinter as tk
from tkinter import *
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
import pyfiglet

llm1=OpenAI(temperature=0.9)


root=Tk()
root.title("FluentAi")
root.geometry('640x480')

tag=Label(root, text="Your Language Learning Companion", wraplength=500, justify="center")
tag.pack(pady=20)

intro=Label(root, text="Please specify what language you want to practice", wraplength=500, justify="center")
intro.pack(pady=20)

inputtxt = tk.Text(root,
                   height = 5,
                   width = 20)
  
inputtxt.pack()

inp = inputtxt.get(1.0, "end-1c")

#firstinput=input()

#proompty = PromptTemplate(
#    input_variables=["firstinput"],
#    template="""You are """
#)

#convo = ConversationChain(
#    llm=OpenAI(temperature=0),
#    memory=ConversationBufferMemory()
#)

#convo.run(proompty.format(firstinput=input()))

#convo.run(input())

def lang1():
   tag["text"] = "Sure, I'm happy to help you practice " + inp + ". Please specify your competency level."

B = Button(root, text='Specify Language', command=lang1)
B.pack(pady=20)
root.mainloop()