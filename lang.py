from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import pyfiglet

llm1 = OpenAI(temperature=0.9)

welcome = pyfiglet.figlet_format("Your Language Learning Consultant")

print(welcome)

print("Hello! I'm here to help you learn to read a foreign language.")

print("Please specify the number of learning exercises you'd like:")

num = int(input())

proompty = PromptTemplate(
    input_variables=["firstinput"],
    template="""I am a person that only speaks English who has come to you for guidance on how to speak another lanuage.
    You are a fluent speaker of the language and an expert instructor that can work around any individual challenges I
    might have as a beginner to help me learn the language. The language I want to learn is specified below.
    
    Language: {firstinput}
    
    Once you know the language I'm trying to learn, use that knowledge along with the knowledge that I'm only fluent in
    English to contruct a beginner exercise that you will instruct me to answer. When I answer, take my response and let me know
    if my response was correct or not, then give me another exercise based on fuzzy logic regarding how well I understood the
    exercise.
    
    Be sure to vary the exercise questions. Sometimes, offer multiple choices. Other times, ask a question and expect a response.
    Other times, provide a sentence for me to complete in the target language."""
)

convo = ConversationChain(
    llm=OpenAI(temperature=0),
    memory=ConversationBufferMemory()
)

print("Please specify what language you need help learning:")

print(convo.run(proompty.format(firstinput=input())))

for x in range(num):
    print((convo.run(input())))

print(convo.run("Thank me for my time and offer me encouragement to continue learning, while also mentioning two or three ways I could improve in fluency in my target language."))