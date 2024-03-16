import telebot
from telebot import types
import random
my_num=random.randint(1,100)
Etries=0
number=10
#bot's token:
bot =telebot.TeleBot('6940712349:AAHY8qK9JF183gPPuQ-QXFYdKr95OtOJH2c')
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,'write /info to get some information about this bot')
#info about the bot:
@bot.message_handler(commands=['info'])
def send_welcome(message):
    bot.reply_to(message,'Hello there, my name is GuessTheNumb3erbot AKA GTNbot. lets play a game, i think about a number and you need to guess it. write /dif to choose a difficulty. enjoy :)')
@bot.message_handler(commands=['dif'])
def send_welcome(message):
    difb=types.ReplyKeyboardMarkup()
    b1=types.KeyboardButton('/Easy')
    b2=types.KeyboardButton('/Medium')
    b3=types.KeyboardButton('/Hard')
    difb.add(b1,b2,b3)
    bot.send_message(message.chat.id,'choose your difficulty.', reply_markup=difb)
@bot.message_handler(commands=['Hard'])
def send_welcome(message):
    global my_num
    global Etries
    global number
    number=5
    my_num = random.randint(1, 150)
    bot.send_message(message.chat.id, f'You chose easy, now you need to guess a number from 0-100 and you have {number} attempts to do so. guess a number')
    Etries=5
@bot.message_handler(commands=['Easy'])
def send_welcome(message):
    global my_num
    global Etries
    global number
    my_num = random.randint(1, 100)
    bot.send_message(message.chat.id, f'You chose easy, now you need to guess a number from 0-100 and you have {number} attempts to do so. guess a number')
    Etries=10
@bot.message_handler(commands=['Medium'])
def send_welcome(message):
    global my_num
    global Etries
    global number
    number=7
    my_num = random.randint(1, 100)
    bot.send_message(message.chat.id, f'You chose easy, now you need to guess a number from 0-100 and you have {number} attempts to do so. guess a number')
    Etries=7
@bot.message_handler(content_types=['text'])
def send_welcome(message):
    global Etries
    if message.text.isdigit() and Etries>0:
        bot.reply_to(message, f'You chose {message.text}', )
        if int(message.text)==my_num:
            bot.send_message(message.chat.id,'You won')
        else:
            Etries-=1
            bot.send_message(message.chat.id,f'That is not my number you have {Etries}/{number}')
            if int(message.text) < my_num:
                bot.send_message(message.chat.id,'My number is bigger than yours')
            if int(message.text) > my_num:
                bot.send_message(message.chat.id,'Your number is bigger than mine')
    else:
        bot.reply_to(message, 'Do not write letters! Numbers only',)
    if Etries==0:
        bot.reply_to(message, f'You lost', )





# @bot.message_handler(commands=['normal'])
# def send_welcome(message):
#     bot.send_message(message.chat.id, 'You chose normal, now you need to guess a number from 0-100 and you have 10 attempts to do so')
#





















































































































bot.infinity_polling()