import tkinter as tk
from langchain.llms import OpenAI

llm=OpenAI(temperature=0.9)

text="Divine the fortune of the user running this program and tell it in a poetic manner."

window = tk.Tk()
greeting = tk.Label(text=llm(text))
greeting.pack()
window.mainloop()