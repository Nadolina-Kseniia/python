import telebot
import os
from dotenv import load_dotenv, find_dotenv
from datetime import datetime

load_dotenv(find_dotenv())

def regist(message):
    Date = datetime.now()
    UserId = message.from_user.id
    list = message.text
    list = list + "|"+str(UserId)
    list = list + "|"+str(Date)

    with open("Registration.txt", "a") as a:
        a.writelines("\n"+list)

def RegistOut(message):
    load_dotenv(find_dotenv())
    bot = telebot.TeleBot(os.getenv('TOKEN'))
    with open('Registration.txt', 'r', encoding='utf-8') as f:
        marath = f.read()
        print(marath)
    if not marath:
        bot.send_message(message.chat.id, 'У меня пока нет данных о марафонах')
    else:
        bot.send_message(message.chat.id, marath)


