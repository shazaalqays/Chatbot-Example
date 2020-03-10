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
In my case I downloaded WikiQA-dev.txt to use it as a training data; you can find it here [WikiQA](https://www.microsoft.com/en-us/download/details.aspx?id=52419&from=http%3A%2F%2Fresearch.microsoft.com%2Fapps%2Fmobile%2Fdownload.aspx%3Fp%3D4495da01-db8c-4041-a7f6-7984a4f6a905). But also I will train different simple data as well. 

Before transferring the data for training it have to be prepared. So, we will create reader.py in order to prepare the data.

*Note:* WikiQA-dev.txt is a text file that’s why I’m using pickle library in order to deal with txt file. If you have another type of data file you need to look for a suitable library to deal with that kind of file.
