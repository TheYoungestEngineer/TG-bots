import telebot
from telebot import types
import random
points=0
tries=0
bot=telebot.TeleBot('6965129588:AAG-uufFSHhq4RWAlO2dE2PjYyZ87aWmQqo')
@bot.message_handler(commands=['start'])
def send_welcome(message):
    global Qsts, Ans, Trueans,points
    Qsts, Ans, Trueans = Lvl()
    answerb=types.ReplyKeyboardMarkup(row_width=2)
    b1=types.KeyboardButton(Ans[0])
    b2=types.KeyboardButton(Ans[1])
    b3=types.KeyboardButton(Ans[2])
    b4=types.KeyboardButton(Ans[3])
    b5=types.KeyboardButton(f'You have {str(points)} points')
    answerb.add(b1,b2,b3,b4,b5)
    bot.send_message(message.chat.id,Qsts, reply_markup=answerb)


@bot.message_handler(content_types=['text'])
def send_welcome3(message):
    global Qsts,Ans,Trueans,points
    print(message.text, Trueans)
    if message.text == Trueans:
        bot.reply_to(message,'Good work, your answer is true. keep answering')
        points += 1
        send_welcome(message)


    else:
        bot.reply_to(message, f'Nice try, the answer to this question is {Trueans} ')
        send_welcome(message)



# print(my_list)
# #QsAns=random.choice(my_list)
# QsAns=my_list[1]
# QsAnsEL=QsAns.split()
# print(QsAnsEL)
def Lvl():
    global TrueAns
    QSAnsList = []
    QS = open('Chat QS.txt')
    allQs = QS.read()
    my_list = allQs.split('\n')
    minilist=[]
    for element in my_list:
        if element=="":
            if len(minilist)!=0:
                QSAnsList.append(minilist)
                minilist=[]
            else:
                minilist=[]
        else:
            minilist.append(element)
    QSANS=QSAnsList[random.randint(0,89)]
    qstion=QSANS[0]
    AllAns=[]
    #QSANS[1:]
    for element in QSANS:
        if 'True' in element:
            element=element[:-7]
            TrueAns = element[11:]
        if 'Variant' in element:
            AllAns.append(element[11:])

    return qstion, AllAns, TrueAns








































































































































bot.infinity_polling()