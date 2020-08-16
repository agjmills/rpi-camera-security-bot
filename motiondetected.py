#!/usr/bin/python3

import telepot
import os
import sys
from telepot.loop import MessageLoop
# adapt the following to the bot_id:bot_token

video = sys.argv[1]
bot = telepot.Bot(TELEGRAM_KEY_HERE)
bot.sendVideo(YOUR_USER_ID_HERE, video=open(video, 'rb'), caption='last video')

