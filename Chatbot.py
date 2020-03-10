#import files
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from flask import Flask, render_template, request
import pickle

#Flask app
app = Flask(__name__)


chatbot = ChatBot('MyBot', trainer='chatterbot.trainers.ListTrainer')


conversation = []
# load data using pickle library
fileq = open("conversation.bin","rb")
conversation = pickle.load(fileq)


# trainer = ListTrainer(chatbot)
#
# trainer.train([
#     "Hello",
#     "Hello",
#     "Hi",
#     "Hello",
#     "greetings",
#     "Hello",
#     "Thank you",
#     "you are welcome",
#     "thanks",
#     "You're welcome",
#     "What is your name?",
#     "My name is Robo",
#     "Are you a robot?",
#     "Yes :)",
#     'how are you?',
#     "I'm fine, thank you",
#     "what's up?",
#     "I'm fine, thank you",
#     "how is going?",
#     "I'm fine, thank you",
#     'are you okay',
#     "I'm fine, thank you",
#     'are you a human?',
#     "no i'm not",
#     "bye",
#     "Take care. Goodbye!"
# ])
#
#
# trainer.train("chatterbot.corpus.english")
#
#
# trainer.train(conversation)

# home page
@app.route("/")
def home():
    return render_template("home.html")

# get response from chatbot
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))

if __name__ == "__main__":
    app.run(debug=True)

# GREETING_INPUTS = ("hello", "hi", "greetings", "sup","hey")
# ques = input("ROBO: My name is Robo. I will answer your queries. If you want to exit, type Bye!\n")
# flag = True
# while (flag==True): # donuş sağlayan loop
#     if ques != 'bye':
#         if(ques =='thanks' or ques =='thank you' ):
#             flag=False
#             print("ROBO: You are welcome..")
#         else:
#             if ques in GREETING_INPUTS:
#                 print("ROBO: I am glad! You are talking to me")
#             else:
#                 print("ROBO: ",end="")
#                 response = chatbot.get_response(ques)
#                 print(response)
#         ques = input()
#     else:
#         flag=False
#         print("ROBO: Bye! take care..")
