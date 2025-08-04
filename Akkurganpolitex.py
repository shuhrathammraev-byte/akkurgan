
import telebot

TOKEN = 'SIZNING_BOT_TOKENINGIZ'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Салом! Мен ботман. Қандай ёрдам берай?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
