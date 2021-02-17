#    This file is part of the ChannelAutoForwarder distribution (https://github.com/xditya/ChannelAutoForwarder).
#    Copyright (c) 2021 Adiya
#    
#    This program is free software: you can redistribute it and/or modify  
#    it under the terms of the GNU General Public License as published by  
#    the Free Software Foundation, version 3.
# 
#    This program is distributed in the hope that it will be useful, but 
#    WITHOUT ANY WARRANTY; without even the implied warranty of 
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
#    General Public License for more details.
# 
#    License can be found in < https://github.com/xditya/ChannelAutoForwarder/blob/main/License> .

import logging
import asyncio
from telethon import TelegramClient, events, Button
from decouple import config
from telethon.tl.functions.users import GetFullUserRequest

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.INFO)

# start the bot
print("Starting...")
try:
    apiid = config("APP_ID", cast=int)
    apihash = config("API_HASH")
    bottoken = config("BOT_TOKEN")
    frm = config("FROM_CHANNEL", cast=int)
    tochnl = config("TO_CHANNEL", cast=int)
    datgbot = TelegramClient('bot', apiid, apihash).start(bot_token=bottoken)
except:
    print("Environment vars are missing! Kindly recheck.")
    print("Bot is quiting...")
    exit()


@datgbot.on(events.NewMessage(pattern="/start"))
async def _(event):
    ok = await datgbot(GetFullUserRequest(event.sender_id))
    await event.reply(f"നോക്കണ്ട `{ok.user.first_name}` ഇതിൽ ഒന്നും ഇല്ല\n", buttons=[Button.url("Owner", url="https://t.me/OO7ROBOT")], link_preview=False)




@datgbot.on(events.NewMessage(incoming=True, chats=frm)) 
async def _(event): 
    if not event.is_private:
        try:
            await event.client.send_message(tochnl, event.message)
        except:
            print("TO_CHANNEL ID is wrong or I can't send messages there (make me admin).")


print("Bot has started.")
print("Do visit @OO7ROBOT..")
datgbot.run_until_disconnected()
