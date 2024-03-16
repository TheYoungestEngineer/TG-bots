import telebot
import random

#token
bot = telebot.TeleBot('6873090961:AAF8rfc5dKsCCs11eOJzRvWJk7n6RgilGSY')
#phrases
phrases=open('chat frases.txt')
allphrases=phrases.read()
my_list=allphrases.split('\n')
print (my_list)
#start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,'Hello there')
#info about the bot
@bot.message_handler(commands=['info'])
def send_welcome(message):
    bot.reply_to(message,'My name is Anton, like Alisa but now in English!. To start just write /start')
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'the commands are: /help , /start , /info ')
#text
@bot.message_handler(content_types=['text'])
def send_welcome(message):
    bot.reply_to(message,my_list[random.randint(0,99)])









































































































































































bot.infinity_polling()