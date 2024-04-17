from openpyxl import load_workbook
import telebot
import os
from datetime import datetime
import time


bot = telebot.TeleBot("6494717982:AAFfdXGtztaOPpE_ZVHSCza1USLfvUf12rs")

#bot = telebot.TeleBot("7107331036:AAF0-AgnOPA5_UTEprnfQ3YznRFau15sLdE")

now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"{now} starting")


fn = "baseusers.xlsx"
wb = load_workbook(fn)
ws = wb["data"]
f = open("userstxt.txt")
now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"{now} opened xlsx")
contenttxt = f.read()
f.close()
wb.save(fn)

iscensormats = False

now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"{now} analyzing missed messages")
    

@bot.message_handler(commands=["mats", "switchmats"])
def mats(message):
    if message.from_user.id == 5893427261 or 6312217343:
        global iscensormats
        if iscensormats == True:
            iscensormats = False
            time.sleep(1)
            bot.send_message(message.chat.id, f"Переключено на {iscensormats}")
        elif iscensormats == False:
            iscensormats = True
            time.sleep(1)
            bot.send_message(message.chat.id, f"Переключено на {iscensormats}")

@bot.message_handler(commands=["statusmats"])
def statusmats(message):
    if message.from_user.id == 5893427261 or 6312217343:
        if iscensormats == True:
            bot.send_message(message.chat.id, "Сейчас цензура матов включена!")
        elif iscensormats == False:
            bot.send_message(message.chat.id, "Сейчас цензура матов выключена!")

@bot.message_handler(commands=["list", "table"])
def sendtable(message):
    bot.send_message(message.chat.id, "Ожидайте")
    table = open("baseusers.xlsx", "rb")
    time.sleep(1)
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    bot.send_document(message.chat.id, table)
    bot.send_message(message.chat.id, f"Актуально на {now}")

@bot.message_handler(commands=["amount"])
def amount(message):
    with open("userstxt.txt") as m:
        txttexttoamount = m.read()
        volume = txttexttoamount.count(",") - 1
        bot.send_message(message.chat.id, f"Всего в таблице {volume} пользователей.")
        m.close()

@bot.message_handler(commands=["userstxt"])
def sendusers(message):
    txt = open("userstxt.txt", "rb")
    bot.send_document(message.chat.id, txt)
    txt.close()

@bot.message_handler()
def messagehandlers(message):
    with open("userstxt.txt", "a") as k:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        chattitle = message.chat.title
        if chattitle == None:
            chattitle = "lschat"
        print(f"{now} From {chattitle}: ~~~ {message.text} ~~~ n:{message.from_user.first_name} sn:{message.from_user.last_name} us:{message.from_user.username} id:{message.from_user.id} p:{message.from_user.is_premium}")
        with open("userstxt.txt") as s:
            contenttxt = s.read()
            finding = contenttxt.find(str(message.from_user.id))
            if int(finding) == -1:
                print("↑↑↑ New User ↑↑↑")
                now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                ws.append([now, message.from_user.first_name, message.from_user.last_name, message.from_user.username, message.from_user.is_premium, message.from_user.id])
                k.write(f"{message.from_user.id}, ")
                print(f"appended!")
                wb.save(fn)
    messageid = message.message_id
    if message.chat.id == 2087495860:
        if message.from_user.id == 5893427261 or 6312217343 or 1087968824 or 7074448544:
            pass
        else:
            if iscensormats == True:
                with open("words.txt", "r", encoding="utf-8") as t:
                    wordstext = t.read()
                    textmsg = message.text
                    textmsglowwords = textmsg.split()
                    print(textmsglowwords)
                    i = 0
                    while i < len(textmsglowwords):
                        textmsg = textmsglowwords[i]
                        textmsglow = textmsg.lower()
                        isinwords = wordstext.find(textmsglow)
                        if len(textmsglow) > 1:
                            if isinwords != -1:
                                bot.delete_message(message.chat.id, messageid)
                                print(textmsglow)
                                break
                    i+=1

                    
            t.close()
    








            
                


wb.close()

bot.infinity_polling()