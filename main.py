#test

import telebot
import requests
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = '6037834959:AAGyAKVEftK9yhE_iaQ9TM8_U694euvGuHA'
URL_ALL_CHARACTERS = 'https://swapi.dev/api/people'
URL_GIF_CAT = 'https://cataas.com/cat/gif'
URL_DOG = 'https://dog.ceo/api/breeds/image/random'
bot = telebot.TeleBot(TOKEN)
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Characters'))



def get_all_characters():
    response = requests.get(URL_ALL_CHARACTERS)
    An = []
    nex = response.json()['next']
    while nex:
        response = requests.get(nex)
        for i in response.json()['results']:
            An.append(i['name'])
        nex = response.json()['next']
    return sorted(An)



@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "I'm a star wars bot", reply_markup=keyboard)


@bot.message_handler(regexp='Characters')
def all_characters_message(message):
    chr = get_all_characters()
    text = "\n".join(chr)
    bot.send_message(message.chat.id, 'Choose a character:\n' + text)




bot.infinity_polling()