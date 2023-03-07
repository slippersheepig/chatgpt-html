import json
from revChatGPT.V1 import Chatbot
from flask import Flask, request, render_template, redirect

server = Flask(__name__)

# get config
with open("config.json", "r") as f: config = json.load(f)

# init chatbot
chatbot = Chatbot(config)

def generate_response(prompt):
    try:
        for data in chatbot.ask(prompt):
            response = data["message"]
        return response
    except Exception as e:
        return e

@server.route("/")
def home():
    chatbot.reset_chat()
    return render_template("chat.html")

@server.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    return str(generate_response(user_text))

if __name__ == '__main__':
    server.run(debug=False, host='0.0.0.0', port=8088)
