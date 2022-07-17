import discord
from discord import Client
from discord import guild
from interactions import Intents
from threading import Thread
from functions import pomodoro


HARRY_TOKEN = "USE TOKEN DO NOT PUT ON GIT HUB"

bot_intents = discord.Intents.all()
bot = Client(intents=bot_intents)

@bot.event
async def on_ready():
    print("Bot has connected to discord.")

@bot.event
async def on_message(msg) :
    message_sender = msg.author
    if message_sender == bot.user : return
    message_string = msg.content
    if message_string.startswith("$study") :
            user_dm =  await message_sender.create_dm()
            pomodoro_thread = Thread(target=pomodoro, args=(user_dm,))
            pomodoro_thread.start() # brings an error up.....
            
            #for i in range(3) :
             #   await user_dm.send("Start studying.")
              #  sleep(STUDY_TIME) 
               # await user_dm.send("Break time.")
                #sleep(SHORT_BREAK)
            #await user_dm.send("Start studying.")
            #sleep(STUDY_TIME)
            #await user_dm.send("Break time.")

    
bot.run(HARRY_TOKEN)