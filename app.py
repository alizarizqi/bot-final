from pickle import GLOBAL
from tokenize import Token
import numpy as np
import spacy
# from englishDetect import language_detection
from flask import Flask, request
from autocorrect import Speller
# from positionChecker import position_checker
# from presentContinuous import present_continuous, correct_continuous
# from presentPerfect import present_perfect, correct_perfect
# from quest import quest
# from simplePast import simple_past
# from simpleFuture import simple_future
# from simplePresent import SVAPresent
from positive import positive
from quest import quest
# from negative import negative
import os
import telegram
import re
import pyinflect
from englishDetect import language_detection
from detectSentence import detect
from positionCheckerQuest import position_checker_quest
from simplePastQuest import VBD
from detsent import *
bot_token = "5536226022:AAHApTMSLbkg1xZQgjXSXfIN0_LNux4QKnc"

nlp = spacy.load("en_core_web_sm")


app = Flask(__name__)
PHOTO_PATH = 'img/logo_tenses.png'


@app.route("/", methods=['GET', 'POST'])
def webhook():
    bot = telegram.Bot(
        token=bot_token)
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.effective_chat.id
        user = update.message.from_user.username
        text = update.message.text
        # bot.send_message(chat_id, text)
        matches = re.split(regex, text)
        text2 = matches[0].lower()
        # bot.send_message(chat_id, text2)

        if text == "/start":
            bot.send_photo(chat_id, photo=open(PHOTO_PATH, 'rb'))
            bot.send_message(chat_id, "Halo " + user + ", welcome to *Tenses English Learning bot*! We hope you will get the best correction here." + "\n\n" +
                             "*Tenses English Learning bot* gives you access to detection and correction sentence in 5 tenses. The tenses are *Simple Present Tense*, *Simple Past Tense*, *Simple Future Tense*, *Present Continuous Tense*, and *Present Perfect Tense*." + "\n\n" + "Please enter *a simple sentence* and use *English language*." + "\n" + "For examples, click or type /help", parse_mode=telegram.ParseMode.MARKDOWN)
        elif text == "/help":
            bot.send_message(chat_id, "These are some examples of 5 tenses" + "\n\n" + "*Simple present tense:*" + "\n" + "_- He goes to the library every day_" + "\n" + "_- He does not go to the library every day_" + "\n" + "_- Does he go to the library every day?_" + "\n" + "_- When does he go to the library every day?_" + "\n\n" + "*Simple past tense:*" + "\n" + "_- He went to the library yesterday_" + "\n" + "_- He did not go to the library yesterday_" + "\n" + "_- Did he go to the library yesterday?_" + "\n" + "_- When did he go to the library yesterday?_" + "\n\n" + "*Simple future tense:*" +
                             "\n" + "_- He will go to the library_" + "\n" + "_- He will not go to the library_" + "\n" + "_- Will he go to the library?_" + "\n" + "_- Where will he go to the library?_" + "\n\n" + "*Present continuous tense:*" + "\n" + "_- He is going to the library_" + "\n" + "_- He is not going to the library_" + "\n" + "_- Is he going to the library?_" + "\n" + "_- Where is he going to the library?_" + "\n\n" + "*Present Perfect tense:*" + "\n" + "_- He has gone to the library_" + "\n" + "_- He has not gone to the library_" + "\n" + "_- Has he gone to the library?_", parse_mode=telegram.ParseMode.MARKDOWN)
        else:
            if "?" in text2:
                bot.send_message(chat_id, quest(text2),
                                 parse_mode=telegram.ParseMode.MARKDOWN)
            else:
                out = text2.replace(".", "")
                bot.send_message(chat_id, positive(
                    out, text), parse_mode=telegram.ParseMode.MARKDOWN)

        return 'ok'
    return 'error'


def index():
    return webhook()
