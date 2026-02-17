import telebot
import os

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Olá! Seu bot está funcionando 🚀")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, "Recebi sua mensagem: " + message.text)

bot.polling()
