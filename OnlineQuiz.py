import time

import telebot
from telebot import types
import json
import random
#we are asking for a random number
QSnum = random.randint(0, 95)
#we are making a def for player's buttons that will work 10 times
def makeArandomNUMber(player1,player2):
    QSnum = random.randint(0, 95)
    button_maker(player1, QSnum)
    button_maker(player2, QSnum)
# Функция для чтения данных из JSON-файла
def read_json(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return "Файл не найден"
    except json.JSONDecodeError:
        return "Ошибка при декодировании JSON"

# Функция для записи данных в JSON-файл
def write_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


# Функция для чтения записи из JSON-файла
def read_record(filename, index):
    data = read_json(filename)
    if isinstance(data, list) and 0 <= index < len(data):
        return data[index]
    else:
        return "Индекс за пределами диапазона или данные не являются списком"

# Функция для обновления записи в JSON-файле
def update_record(filename, key,data):
    d=read_json(filename)
    d[key]=data
    write_json(data=d,filename=filename)

# Функция для удаления записи из JSON-файла
def delete_record(filename, index):
    data = read_json(filename)
    if isinstance(data, list) and 0 <= index < len(data):
        del data[index]
        write_json(data, filename)
        return "Запись успешно удалена"
    else:
        return "Индекс за пределами диапазона или данные не являются списком"

# Replace 'YOUR_API_KEY' with your actual Telegram Bot API key
API_KEY = '7014750146:AAGOGdiE_9JRC7fhOecgN02sPAH8tNvTubU'

# Create a bot instance
bot = telebot.TeleBot(API_KEY)
write_json(filename='game.json',data={})
# we made the [start waiting for players] button
@bot.message_handler(commands=['start'])
def start(message):
    place = types.ReplyKeyboardMarkup(row_width=1)
    b1 = types.KeyboardButton('Start waiting for Players')
    place.add(b1)
    bot.send_message(message.chat.id, "Hello! Welcome to our online, press [ Waiting for players] to start.",reply_markup=place)

#we are making 4 buttons
def button_maker(player,QSnum):
    QSlist=read_json('QS.json')
    place=types.ReplyKeyboardMarkup()
    b1=types.KeyboardButton(QSlist[QSnum]['options'][0])
    b2 = types.KeyboardButton(QSlist[QSnum]['options'][1])
    b3 = types.KeyboardButton(QSlist[QSnum]['options'][2])
    b4 = types.KeyboardButton(QSlist[QSnum]['options'][3])
    place.add(b1,b2,b3,b4)
    bot.send_message(player,QSlist[QSnum]['question'],reply_markup=place)
#we are making a json file that has 10 questions for the game
def makeAgameQS():
    QSlist=read_json('questions_and_answers.json')
    gameQS=[]
    for i in range(10):
        QS=random.choice(QSlist)
        gameQS.append(QS)
    write_json(gameQS,'QS.json')
#we are catching the text of the buttons to check how many players are connected
@bot.message_handler(content_types=['text'])
def game(message):
    global player1,player2
    # we are checking how many players are connected to the game
    if message.text=='Start waiting for Players':

        update_record(filename='game.json', key=message.from_user.id,data={'name':message.from_user.username,'chatID':message.chat.id,'points':0,'round':0})
        if (len(read_json('game.json')))==2:
            makeAgameQS()
            player2=message.chat.id
            bot.send_message(player1,f'The game is starting you are playing against {read_json("game.json")[str(player2)]["name"]}')
            button_maker(player1, 0)
            bot.send_message(player2,f'The game is starting you are playing against {read_json("game.json")[str(player1)]["name"]}')
            button_maker(player2,0)
        #if only one player is connected to the game we are going to set him as player1
        else:
            player1=message.chat.id
            bot.send_message(message.chat.id,'Waiting for players...')
    else:
        #we are transfering QS.json and game.json into a list
        QSlist = read_json('QS.json')
        players=read_json('game.json')
        #we are checking if the player's text is in the options and in the same round number
        if message.text in QSlist[players[str(message.chat.id)]['round']]['options']:
            #we are making a commend for the key of the round so we can add one to it every round
            round=players[str(message.chat.id)]['round']
            # we made a comment for the json key of the in-game points so we can add one to it every right answer
            point=players[str(message.chat.id)]['points']
            #we are checking if players answer is right
            if message.text ==QSlist[players[str(message.chat.id)]['round']]['answer']:
            #we added one to points because it is right
                point+=1
            # we added one to round because we finished the round
            round+=1
            print(round)
            #we are updating the game.json with the new points and the round number
            update_record('game.json',message.chat.id,{'name':message.from_user.username,'chatID':message.chat.id,'points':point,'round':round})
            players = read_json('game.json')
            print(players[str(player1)]['round'], players[str(player2)]['round'])
            #we are checking if the players answered the 10 questions and if so we are going to write to them how much points they got and how much theyr opponent got
            if players[str(player1)]['round']==10 and players[str(player2)]['round']==10 :
                bot.send_message(player1,f'You got {players[str(player1)]['points']}, {players[str(player2)]['name']} got {players[str(player2)]['points']}', reply_markup=types.ReplyKeyboardRemove())
                bot.send_message(player2, f'You got {players[str(player2)]['points']}, {[players[str(player1)]['name']]} got {players[str(player1)]['points']}', reply_markup=types.ReplyKeyboardRemove())
                write_json(filename='game.json', data={})
                write_json(filename='QS.json', data={})
            #we are checking who answered all the questions
            elif round>=10:
                bot.send_message(message.chat.id,'You answered every question, wait for your opponent', reply_markup=types.ReplyKeyboardRemove())

            else:
                button_maker(message.chat.id,round)























#d={'UserID':{'name':'','chatID':'','points':''}}

























































bot.polling()
