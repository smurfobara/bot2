from openpyxl import load_workbook
import telebot
import os
from datetime import datetime
import time


bot = telebot.TeleBot("6494717982:AAFfdXGtztaOPpE_ZVHSCza1USLfvUf12rs")

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



now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"{now} analyzing missed messages")
    

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
    bot.send_message(message.chat.id, txt)
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
    








            
                


wb.close()

bot.infinity_polling()