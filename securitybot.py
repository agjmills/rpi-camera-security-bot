#!/usr/bin/python3

import datetime
import telepot
import time
import requests
import os
import glob
from telepot.loop import MessageLoop

def webcontrol(chat_id, type, cmd):
    req = 'http://localhost:8080/0/'+type+'/'+cmd
    res = requests.get(req)
    bot.sendMessage(chat_id, res.text)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    #should work thanks to Winston
    print(msg['from']['id'])
    if msg['from']['id'] != YOUR_TELEGRAM_ID:
        bot.sendMessage(chat_id, "Sorry this is a personal bot. Access Denied!")
        exit(1)

    print('Got command: %s' % command)

    if command == '/time':
        bot.sendMessage(chat_id, 'The current time is: '+str(datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')))
    elif command == '/disarm':
        bot.sendMessage(chat_id, 'Disarming motion detection')
        os.system('sudo supervisorctl stop motion')
        bot.sendMessage(chat_id, 'Motion detection disarmed')
    elif command == '/arm':
        bot.sendMessage(chat_id, 'Arming motion detection')
        os.system('sudo supervisorctl start motion')
        bot.sendMessage(chat_id, 'Motion detection armed')
    else:
        bot.sendMessage(chat_id, "sorry, I don't know the command "+command)
# adapt the following to the bot_id:bot_token
bot = telepot.Bot(YOUR_TELEGRAM_KEY)
MessageLoop(bot, handle).run_as_thread()
print('I am listening ...')

while 1:
    time.sleep(10)
