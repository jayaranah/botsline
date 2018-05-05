# encoding: utf-8
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('F3NdLQLM6iheiPNjdDWsuKrDT0wunJJ4bwSGymTmFfAFMHXIwdBLokRDGLrJyfStsS4wL47d6wEVL+ggW2a1jH93zDG4nrr+xb7Y0O3hh4GeT74xcd3j7vzw44vR3YoOHDjJvsL81kLofFEM/uiBDQdB04t89/1O/w1cDnyilFU=') #Your Channel Access Token
handler = WebhookHandler('879f79734443740f43162f854a641f29') #Your Channel Secret

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text #message from user

    if text == "test":
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(original_content_url="https://pre00.deviantart.net/6ba5/th/pre/f/2016/095/f/8/nekomimi_cute_render_by_keyzakarenina-d9xsjrq.png", preview_image_url="https://i.pinimg.com/originals/6b/d8/47/6bd84755083cde275c459ba73f7d95ec.jpg"))
    

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])
