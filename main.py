import os
import json
from revChatGPT.Unofficial import Chatbot
from flask import Flask, request, render_template, redirect

server = Flask(__name__)

# get config
with open("config.json", "r") as f: config = json.load(f)

# init chatbot
chatbot = Chatbot(config)

def send_gpt(message):
    response = chatbot.ask(message)
    return response["message"]

@server.route('/', methods=['GET', 'POST'])
def get_request_json():
    if request.method == 'POST':
        if len(request.form['question']) < 1:
            return render_template(
                'chat.html', question="null", res="问题不能为空")
        question = request.form['question']
        print("======================================")
        print("接到请求:", question)
        res = send_gpt(question)
        print("问题：\n", question)
        print("答案：\n", res)

        return render_template('chat.html', question=question, res=str(res))
    return render_template('chat.html', question=0)

if __name__ == '__main__':
    server.run(debug=True, host='0.0.0.0', port=80)
