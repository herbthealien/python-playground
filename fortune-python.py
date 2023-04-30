import tkinter as tk
from langchain.llms import OpenAI

llm=OpenAI(temperature=0.9)

text="Read me my i ching fortune and tell it to me as if you're Arnold Schwarzenegger, former governor of california."

window = tk.Tk()
greeting = tk.Label(text=llm(text))
greeting.pack()
window.mainloop()