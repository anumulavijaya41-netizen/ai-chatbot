from flask import Flask, render_template, request, jsonify
from google import genai
import os

# Flask App

app = Flask(__name__)
# Gemini API Key
os.environ["GOOGLE_API_KEY"] = "MY_API_KEY"

# Gemini Client
client = genai.Client()  #creatre connection with Gemini Ai

# Chat Creation
chat = client.chats.create(   # for creation and storing the chat in memory 
    model="gemini-2.5-flash"
)


# Homepage
@app.route("/")   # if user open the page then it will call the home function the  flask opens index.html
def home():
    return render_template("index.html")


# Chat Route
@app.route("/chat", methods=["POST"])   #frontend sends message to chat using post to send the data
def chatbot():

    user_message = request.json["message"]   

    response = chat.send_message(user_message)

    return jsonify({  #converting the python code data to json formate and sending the data to the frontend
        "reply": response.text   
    })


# Run Server
if __name__ == "__main__":  #Run only if this file is executed directly
    app.run(debug=True)