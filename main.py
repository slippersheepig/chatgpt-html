import os
import json
from revChatGPT.V1 import Chatbot
from flask import Flask, request, render_template, redirect

server = Flask(__name__)

# get config
with open("config.json", "r") as f: config = json.load(f)

# init chatbot
chatbot = Chatbot(config)

def send_gpt(message):
    prev_text = ""
    for data in chatbot.ask(message):
        prev_text = prev_text + data["message"][len(prev_text) :]
    return prev_text

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
