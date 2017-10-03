import telebot
from array import array

class origen:
    
class Vuelos:
    def __init__(self, origen, destino):
        self.origen = origen
        self.destino = destino

## Crear array de precios, origenes y destinos

precios = []

API_TOKEN = '454898606:AAFwqtEeAqtj3Lca55wbg62rMsQ83Iz4of0'

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am FlyFinderBot.
I will help you to find the best fly where\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message,"Eres to fea.")

bot.polling()
