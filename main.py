import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

API_TOKEN = '7706578873:AAHeThjzgtL9YR6toT97zGDk34AnRxnL43s'

bot = telebot.TeleBot(API_TOKEN)

# === YOUR WEBAPP LINK ===
WEBAPP_URL = "https://www.youtube.com/"  # Replace with your real hosted page

# /start command
@bot.message_handler(commands=['start'])
def start(message):
    send_button(message.chat.id)

# When user sends any text/symbol/etc.
@bot.message_handler(func=lambda message: True)
def send_on_every_message(message):
    send_button(message.chat.id)

# Function to send the button with Telegram WebApp
def send_button(chat_id):
    markup = InlineKeyboardMarkup()
    webapp = WebAppInfo(url=WEBAPP_URL)
    btn = InlineKeyboardButton("▶️ Open Game", web_app=webapp)
    markup.add(btn)
    bot.send_message(chat_id, "тут будет что то?\n посылать тебе", reply_markup=markup)

bot.polling(none_stop=True)
