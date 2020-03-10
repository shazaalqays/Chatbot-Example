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
