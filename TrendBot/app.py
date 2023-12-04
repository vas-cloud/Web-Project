from flask import Flask, render_template, request
from bardapi import BardCookies 

app = Flask(__name__)

cookie_dict = {
    "__Secure-1PSID": "cwgAH0UelQ67hFZU97f784UgndgZrpC_17Ln8uxBxil4W3orgrjNbRsBKz6C019Zr2csvA.",
    "__Secure-1PSIDTS": "sidts-CjEBNiGH7liCy2hDVZJ836JO1BOIULIQ5Ls-IA4bOrPt4eWhxbQ7YeiTCz01zgWZ3n34EAA",
    "__Secure-1PSIDCC": "ACA-OxO0qKFXt27hEUWOPSvr7Ici7yMEgNrpAAJb7KhNjXk0TmtthuKuQAVZxW95hrBbXamPV9E"
}

bard = BardCookies(cookie_dict=cookie_dict)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    user_msg = request.form['msg']
    bot_msg = get_bot_reply(user_msg)
    return render_template('index.html', user_msg=user_msg, bot_msg=bot_msg)


def get_bot_reply(user_msg):
    query = user_msg
    reply = bard.get_answer(query)['content']
    return reply


if __name__ == '__main__':
    app.run(debug=True)

