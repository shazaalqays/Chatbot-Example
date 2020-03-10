# CHATBOT service with FLASK
Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.
# Getting Started
In order to build our chat bot we will use ChatterBot which is a machine learning, conversational dialog engine for creating chat bots.
## Prerequisites
First of all, we need to install both of ChatterBot and Flask packages; if you are using python environment just like me you only need to install the packages and import them into python file.
# Create chatbot
Create 'app.py' file. Inside this file create a chatbot importing chatterbot library.
'''
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from flask import Flask, render_template, request
from pickle
'''
