import telebot
import requests
import json
import random

bot = telebot.TeleBot("6050853171:AAHt8d9iYg7suPvmT9QQMqnCUd-humQQGos")

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Отправить фото', 'Отправить геолокацию', 'Показать погоду', 'Показать рандомные фото макияжа с Pinterest', 'Тут скоро появится функция')
    bot.send_message(message.chat.id, 'Привет! Что вы хотите сделать?', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def show_weather(message):
    if message.text == 'Показать погоду':
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Moscow&appid=5a2684e910b748f0c0a1057f1d5585f5')
        data = r.json()
        temp = data['main']['temp'] - 273.15
        wind = data['wind']['speed']
        humidity = data['main']['humidity']
        bot.send_message(message.chat.id, '🤔 Давай посмотрим, что у нас сегодня за погода: {}°C, скорость ветра: {} м/с, влажность: {}%'.format(int(temp), wind, humidity))

bot.polling()

