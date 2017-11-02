# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot

API_TOKEN = '454898606:AAFwqtEeAqtj3Lca55wbg62rMsQ83Iz4of0'

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hola, esto es FlyFinderBot, tu buscador de vuelos! Ahora mismo estamos en construccion.\
""")

bot.polling()
