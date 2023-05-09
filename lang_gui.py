import tkinter as tk
from tkinter import *
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
import pyfiglet
import sys

llm1=OpenAI(temperature=0.9)

root=Tk()
root.title("FluentAi")
root.geometry('640x480')

tag=Label(root, text="Your Language Learning Companion", wraplength=500, justify="center")
tag.pack(pady=20)

intro=Label(root, text="Please specify what language you want to practice", wraplength=500, justify="center")
intro.pack(pady=20)

inputtxt = Entry(root,
                   width = 20)

inputskill = Entry(root,
                   width = 20)

inputanswer = Entry(root,
                    width = 20)
  
inputtxt.pack()

#firstinput=inputanswer.get()

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

s1 = "Sure, I'm happy to help you practice "

s2 = ". Please specify your competency level."

lang = inputtxt.get()


def lang1():
   tag["text"] = s1 + inputtxt.get() + s2
   inputtxt.pack_forget()
   B.pack_forget()
   intro.pack_forget()
   inputskill.pack()
   B2.pack(pady=20)

def lang2():
   tag["text"] = "Let's practice " + inputtxt.get() + " at the " + inputskill.get() + " level together. Please select an exercise to begin!"
   inputskill.pack_forget()
   B2.pack_forget()
   greetings.pack()
   food.pack()
   work.pack()
   culture.pack()
   day2day.pack()

def g1():
   tag["text"] = "Let's practice greetings in " + inputtxt.get() + " together."
   global subj
   subj = "greetings"
   greetings.pack_forget()
   food.pack_forget()
   work.pack_forget()
   culture.pack_forget()
   day2day.pack_forget()
   inputanswer.pack()
   ans.pack()

def f1():
   tag["text"] = "Let's practice dining and food in " + inputtxt.get() + " together."
   global subj
   subj = "food and dining"
   greetings.pack_forget()
   food.pack_forget()
   work.pack_forget()
   culture.pack_forget()
   day2day.pack_forget()
   inputanswer.pack()
   ans.pack()

def w1():
   tag["text"] = "Let's practice workplace lingo in " + inputtxt.get() + " together."
   global subj
   subj = "talking in the workplace"
   greetings.pack_forget()
   food.pack_forget()
   work.pack_forget()
   culture.pack_forget()
   day2day.pack_forget()
   inputanswer.pack()
   ans.pack()

def c1():
   tag["text"] = "Let's practice discussing popular culture in " + inputtxt.get() + " together."
   global subj
   subj = "popular culture"
   greetings.pack_forget()
   food.pack_forget()
   work.pack_forget()
   culture.pack_forget()
   day2day.pack_forget()
   inputanswer.pack()
   ans.pack()

def d2d1():
   tag["text"] = "Let's practice talking about day to day life in " + inputtxt.get() + " together."
   global subj
   subj = "discussing day to day life"
   greetings.pack_forget()
   food.pack_forget()
   work.pack_forget()
   culture.pack_forget()
   day2day.pack_forget()
   inputanswer.pack()
   ans.pack()

def answer():
   tag["text"] = "Let's keep learning " + inputtxt.get() + " together."


B = Button(root, text='Specify Language', command=lang1)
B2 = Button(root, text='Specify Competency', command=lang2)

greetings = Button(root, text='Greetings', command=g1)
food = Button(root, text='Food', command=f1)
work = Button(root, text='Work', command=w1)
culture = Button(root, text='Culture', command=c1)
day2day = Button(root, text='Daily Life', command=d2d1)

ans = Button(root, text='Answer', command=answer)


B.pack(pady=20)
root.mainloop()