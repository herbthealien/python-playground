***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***

llm=OpenAI(temperature=0.9***REMOVED***

text="Tell me my future while talking like Arnold Schwarzenegger, writing your text out in his thick austrian accent."

root=Tk(***REMOVED***
root.title("The Fortunator"***REMOVED***
root.geometry('640x480'***REMOVED***

url="https://upload.wikimedia.org/wikipedia/commons/c/cf/Schwarzenegger_Dec_2015.jpg"
u=urlopen(url***REMOVED***
raw_data=u.read(***REMOVED***
u.close(***REMOVED***

im = Image.open(BytesIO(raw_data***REMOVED******REMOVED***
imr = im.resize((150,200***REMOVED******REMOVED***
photo = ImageTk.PhotoImage(imr***REMOVED***

label=Label(root, wraplength=500, justify="center", image=photo***REMOVED***
***REMOVED***
label.pack(pady=20***REMOVED***

arnold=Label(root, text="Arnold is more than happy to tell you your fortune, if you ask.", wraplength=500, justify="center"***REMOVED***
arnold.pack(pady=20***REMOVED***

def fortune(***REMOVED***:
   arnold["text"] = llm(text***REMOVED***

B = Button(root, text='Ask Arnold For Your Fortune', command=fortune***REMOVED***
B.pack(pady=20***REMOVED***
root.mainloop(***REMOVED***