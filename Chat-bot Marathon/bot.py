import telebot
import os
from dotenv import load_dotenv, find_dotenv
from telebot import types
from datetime import datetime
from Regist import regist
from Marathons import marathons
load_dotenv(find_dotenv())
bot = telebot.TeleBot(os.getenv('TOKEN'))
@bot.message_handler(commands=['start'])
def start_message(message):
    print(str(datetime.now()) + "  " + str(message.from_user.id) + "  " + str(message.from_user.username) + " || " +
          message.text)
    bot.send_message(message.chat.id, text = 'Привет, я бот, который, поможет записаться на марафон')
    markup = types.ReplyKeyboardMarkup()
    item1 = types.KeyboardButton("Начать")
    markup.add(item1)
    bot.send_message(message.chat.id, text = "Нажмите начать", reply_markup=markup)
@bot.message_handler(content_types='text')
def button_message(message):
    if message.text == "Начать" or message.text == "Назад":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Запись")
        markup1.add(item1)
        item2 = types.KeyboardButton("Забеги")
        markup1.add(item2)
        item3 = types.KeyboardButton("Мои записи")
        markup1.add(item3)
        item4 = types.KeyboardButton("Информация")
        markup1.add(item4)
        item5 = types.KeyboardButton("Об авторе")
        markup1.add(item5)
        bot.send_message(message.chat.id, 'Выберите что хотите узнать или сделать', reply_markup=markup1)
    elif message.text == "Запись":
        bot.send_message(message.chat.id, text = "Введите данные: Дата(дд.мм.гг)|Название забега|ФИО|")
        bot.register_next_step_handler(message,regist)
    elif message.text == "Забеги":
        bot.send_message(message.chat.id, text="Данные о забегах:")
        bot.register_next_step_handler(message,marathons)
    elif message.text == "Мои записи":
        bot.send_message(message.chat.id, text="Ваши записи на забеги:")
        marath = open('Registration.txt', 'r')
        if not marath:
            bot.send_message(message.chat.id, 'У меня пока нет данных о марафонах')
        else:
            bot.send_message(message.chat.id, marath)
    elif message.text == "Информация":
        bot.send_message(message.chat.id, text="Номер телефона: *******\nemail: *****@***.ru")
    else:
        bot.send_message(message.chat.id, text="Надолина Ксения Руслановна ИВТ-233")
bot.infinity_polling()