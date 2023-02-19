import json
from revChatGPT.V1 import Chatbot
from flask import Flask, request, render_template, redirect

server = Flask(__name__)

# get config
with open("config.json", "r") as f: config = json.load(f)

# init chatbot
chatbot = Chatbot(config)

def generate_response(prompt):
    prev_text = ""
    for data in chatbot.ask(prompt):
        prev_text = prev_text + data["message"][len(prev_text) :]
    return prev_text

@server.route("/")
def home():
    return render_template("chat.html")

@server.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    return str(generate_response(user_text))

if __name__ == '__main__':
    server.run(debug=False, host='0.0.0.0', port=8088)
