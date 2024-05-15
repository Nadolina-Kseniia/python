import telebot
import os
from dotenv import load_dotenv, find_dotenv
from datetime import datetime

load_dotenv(find_dotenv())

def marathons(message):
    load_dotenv(find_dotenv())
    bot = telebot.TeleBot(os.getenv('TOKEN'))
    with open('Marathons.txt', 'r', encoding='utf-8') as f:
        marathons = f.read()
    if not marathons:
        bot.send_message(message.chat.id, 'У меня пока нет данных о марафонах')
    else:
        bot.send_message(message.chat.id, marathons)

