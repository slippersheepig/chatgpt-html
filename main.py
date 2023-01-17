import os
from pathlib import Path
from dotenv import dotenv_values
from pyChatGPT import ChatGPT
from flask import Flask, request, render_template, redirect

server = Flask(__name__)

# get config
parent_dir = Path(__file__).resolve().parent
config = dotenv_values(f"{parent_dir}/.env")

# init chatbot
chatbot = ChatGPT(config["SESSION_TOKEN"])

def send_gpt(message):
    response = chatbot.send_message(message)
    return response['message']

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
