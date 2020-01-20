import json

import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '...?')

config_file = 'config.json'
with open('config.json') as json_file:
    data = json.load(json_file)
    token = data['token']
    
@client.event
async def on_ready():
    print('Bot is ready.')

client.run(token)