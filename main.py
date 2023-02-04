import openai
from flask import Flask, request, render_template, redirect

server = Flask(__name__)

def get_completion(question):
    try:
        response = openai.Completion.create(
            engine="text-chat-davinci-002-20221122",
            prompt=f"{question}\n",
            temperature=0.5,
            max_tokens=4000,
            stop=None
        )
    except Exception as e:

        print(e)
        return e
    return response["choices"][0]["text"].rstrip("<|im_end|>")

@server.route('/', methods=['GET', 'POST'])
def get_request_json():
    if request.method == 'POST':
        if len(request.form['question']) < 1:
            return render_template(
                'chat.html', question="null", res="问题不能为空")
        question = request.form['question']
        print("======================================")
        print("接到请求:", question)
        res = get_completion(question)
        print("问题：\n", question)
        print("答案：\n", res)

        return render_template('chat.html', question=question, res=str(res))
    return render_template('chat.html', question=0)

if __name__ == '__main__':
    server.run(debug=True, host='0.0.0.0', port=80)
