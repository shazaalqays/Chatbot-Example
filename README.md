# CHATBOT service with FLASK
Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.
# Getting Started
In order to build our chat bot we will use ChatterBot which is a machine learning, conversational dialog engine for creating chat bots.
## Prerequisites
First of all, we need to install both of ChatterBot and Flask packages; if you are using python environment just like me you only need to install the packages and import them into python file.
# Build chatbot
Create ` app.py ` file. Inside this file import the packages below.
```
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from flask import Flask, render_template, request
from pickle
```
Create flask app

` app = Flask(__name__) `

Create a new chat bot with the name of your choice for me I will use myBot.

` chatbot = ChatBot('MyBot', trainer='chatterbot.trainers.ListTrainer') `

*Notice,* I added the trainer type when I created the chat bot.

After creating the chat bot now we have to train it on some data. Also, by default the ChatterBot library will create a sqlite database to build up statements of chats.
In my case I downloaded `WikiQA-dev.txt` to use it as a training data; you can find it here [WikiQA](https://www.microsoft.com/en-us/download/details.aspx?id=52419&from=http%3A%2F%2Fresearch.microsoft.com%2Fapps%2Fmobile%2Fdownload.aspx%3Fp%3D4495da01-db8c-4041-a7f6-7984a4f6a905). But also I will train different simple data as well. 

Before transferring the data for training it have to be prepared. So, we will create `reader.py` in order to prepare the data.

*Note:* `WikiQA-dev.txt` is a text file that’s why I’m using pickle library in order to deal with txt file. If you have another type of data file you need to look for a suitable library to deal with that kind of file.

```
import pickle

# create a conversation list
conversation = []

# Reaning the file 
file = open('WikiQA-dev.txt', 'r',encoding="utf-8")

# split data into lines
Lines = file.readlines() 

for line in Lines:
    # split each line into strings of question and answer pairs
    line = line.split("0")[0] 
    try:
        # split the question answer pair string into question string
        # and add it to question list
        question = line.split("\t")[0] 
        # add the answer to answer list
        answer = line.split("\t")[1]
        # combine the question and the answer into a conversation
        conversation.append(question)
        conversation.append(answer)
    except:
        pass

# create a conersation file
fileQ = open("conversation.bin","wb")
pickle.dump(conversation,fileQ)

```
In this way we have created a conversation file holds a question - answer pairs.

After getting our data ready, we can continue with training the data. Return to app.py file and load the data into conversation list using pickle library.
```
conversation = []
# load data using pickle library
fileq = open("conversation.bin","rb")
conversation = pickle.load(fileq) 
```

Let’s start by training a conversation of our own creation. We call ListTrainer to train our chat bot. Notice, the data I give to trainer is a list of question and answer, first line is question while second line is an answer, and so on.

```
trainer = ListTrainer(chatbot)

trainer.train([
    "Hello",
    "Hello",
    "Hi",
    "Hello",
    "greetings",
    "Hello",
    "Thank you",
    "you are welcome",
    "thanks",
    "You're welcome",
    "What is your name?",
    "My name is Robo",
    "Are you a robot?",
    "Yes :)",
    'how are you?',
    "I'm fine, thank you",
    "what's up?",
    "I'm fine, thank you",
    "how is going?",
    "I'm fine, thank you",
    'are you okay',
    "I'm fine, thank you",
    'are you a human?',
    "no i'm not",
    "bye",
    "Take care. Goodbye!"
])
 ```
 
Next we will train a corpus that is already defined in ChatterBot package which is English corpus.

`trainer.train("chatterbot.corpus.english")`

Finally, we will train our conversation which we loaded before into conversation list.

`trainer.train(conversation)`

After we have our chat bot trained with multiple data let’s start with flask.

Firstly, we will create a home page which is home.html and a function to get response from chat bot
```
@app.route("/")
def home():
    return render_template("home.html")

# get response from chatbot
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))


if __name__ == "__main__":
    app.run()
```

So, as we can see we need to create a home.html file as a frontend.

Within your project create a folder “templates” and inside that create a file `home.html`.

Open `home.html`, you can write whatever you want between <h1> </h1> in html this is called header. As well as <p></p> which means paragraph.
```
<!DOCTYPE html>
<html>
  <title>MyBot</title>
  <body>
    <center>
      <h1>
  	Your Personal ChatBot
      </h1>
    </center>
    <div>
      <p>
         Hi! I'm Robo your personal ChatBot
      </p>
    </div>
    <div id="userInput">
      <input id="textInput" type="text" name="msg" placeholder="Message" />
    </div>
  </body>
</html>
```

So, this is just a basic structure let’s add some css to it. We can create a new file for css but in my case I just add style into home.html. In style you can change a lot of things such as colors, display and font size, etc. for each singular header or other defined feature.
```
<head>
  <link
    rel="shortcut icon"
    type="image/x-icon"
    href="https://user-images.githubusercontent.com/20112458/49326597-773b7280-f57a-11e8-853d-20ed61d18b0d.png"
  />
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <style>
    body {
      font-family: monospace;
    }
    h1 {
      background-color: yellow;
      display: inline-block;
      font-size: 3em;
      margin: 0;
      padding: 14px;
    }
    h3 {
      color: black;
      font-size: 20px;
      margin-top: 3px;
      text-align: center;
    }
    #chatbox {
      margin-left: auto;
      margin-right: auto;
      width: 40%;
      margin-top: 60px;
    }
    #userInput {
      margin-left: auto;
      margin-right: auto;
      width: 40%;
      margin-top: 60px;
    }
    #textInput {
      width: 90%;
      border: none;
      border-bottom: 3px solid black;
      font-family: monospace;
      font-size: 17px;
    }
    .userText {
      color: white;
      font-family: monospace;
      font-size: 17px;
      text-align: right;
      line-height: 30px;
    }
    .userText span {
      background-color: #808080;
      padding: 10px;
      border-radius: 2px;
    }
    .botText {
      color: white;
      font-family: monospace;
      font-size: 17px;
      text-align: left;
      line-height: 30px;
    }
    .botText span {
      background-color: #4169e1;
      padding: 10px;
      border-radius: 2px;
    }
    #tidbit {
      position: absolute;
      bottom: 0;
      right: 0;
      width: 300px;
    }
    .boxed {
      margin-left: auto;
      margin-right: auto;
      width: 78%;
      margin-top: 60px;
      border: 1px solid green;
    }
    .box {
      border: 2px solid black;
    }
  </style>
</head>
```

Now, after that let’s change body structure to be consistent with style part.
```
<body>
  <img />
  <center>
    <h1>
      <img
        src="https://user-images.githubusercontent.com/20112458/49326597-773b7280-f57a-11e8-853d-20ed61d18b0d.png"
        alt="MyBot"
        style="width:40px;height:40px;"
      />Your Personal ChatBot
    </h1>
  </center>
  <div class="box"></div>
  <div class="boxed">
    <div>
      <div id="chatbox">
        <img
          src="https://user-images.githubusercontent.com/20112458/49326597-773b7280-f57a-11e8-853d-20ed61d18b0d.png"
          alt="MyBot"
          style="width:40px;height:40px;"
        />
        <p class="botText">
          <span>Hi! I'm Robo your personal ChatBot ❤️</span>
        </p>
      </div>
      <div id="userInput">
        <input id="textInput" type="text" name="msg" placeholder="Message" />
      </div>
    </div>
  </div>
</body>
```

Until now, we didn’t define any function to get response from chat bot the reason why if we type something nothing will happen. So, we need to add some script. 
```
<script>
  function getBotResponse() {
    var rawText = $("#textInput").val();
    var userHtml = '<p class="userText"><span>' + rawText + "</span></p>";
    $("#textInput").val("");
    $("#chatbox").append(userHtml);
    document
      .getElementById("userInput")
      .scrollIntoView({ block: "start", behavior: "smooth" });
    $.get("/get", { msg: rawText }).done(function(data) {
      var botHtml = '<p class="botText"><span>' + data + "</span></p>";
      $("#chatbox").append(botHtml);
      document
        .getElementById("userInput")
        .scrollIntoView({ block: "start", behavior: "smooth" });
    });
  }
  $("#textInput").keypress(function(e) {
    if (e.which == 13) {
      getBotResponse();
    }
  });
</script>
```
