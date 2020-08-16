#!/usr/bin/python3

import datetime
import telepot
import time
import requests
import os
import glob
from telepot.loop import MessageLoop
from picamera import PiCamera

def webcontrol(chat_id, type, cmd):
    req = 'http://localhost:8080/0/'+type+'/'+cmd
    res = requests.get(req)
    bot.sendMessage(chat_id, res.text)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    #should work thanks to Winston
    print(msg['from']['id'])
    if msg['from']['id'] != YOUR_TELEGRAM_ID_HERE:
        bot.sendMessage(chat_id, "Sorry this is a personal bot. Access Denied!")
        exit(1)

    print('Got command: %s' % command)

    if command == '/photo':
        filename = '/tmp/' + str(datetime.datetime.now()) + '.jpg'
        camera.capture(filename)
        bot.sendPhoto(YOUR_TELEGRAM_ID_HERE, photo=open(filename, 'rb'))
    elif command == '/time':
        bot.sendMessage(chat_id, 'The current time is: '+str(datetime.datetime.now()))
    elif command == '/video':
        # the most recent video in this particular folder of complete vids
        video = max(glob.iglob('/home/pi/motion/detected/vids/*.mp4'), key=os.path.getctime)
        # send video, adapt the the first argument to your own telegram id
        bot.sendVideo(YOUR_TELEGRAM_ID_HERE, video=open(video, 'rb'), caption='last video')
    else:
        bot.sendMessage(chat_id, "sorry, I don't know the command "+command)
# adapt the following to the bot_id:bot_token
bot = telepot.Bot(YOUR_TELEGRAM_KEY_HERE)
camera = PiCamera()
MessageLoop(bot, handle).run_as_thread()
print('I am listening ...')

while 1:
    time.sleep(10)
