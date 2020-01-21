import json

import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '...?')

with open('config.json') as config_file:

    data = json.load(config_file)
    token = data['token']
    
@client.event

async def on_ready():

    print('Bot is ready.')

@client.event

async def on_message(message):

    cond1 = 'i\'m in ' in message.content.lower()
    cond2 = 'i am in ' in message.content.lower()
    cond3 = 'im in ' in message.content.lower()
    output = message.content.lower()
    
    flushed = False
    
    while(cond1 or cond2 or cond3):   
        
        if cond1:

            j = output.find('i\'m in ') - len(output)
            output = output[j + 7:]
            if output.count('i\m in ') == 0:
                cond1 = False
                flushed = True
                
        if cond2:
        
            j = output.find('i am in ') - len(output)
            output = output[j + 8:]
            if output.count('i am in ') == 0:
                cond2 = False
                flushed = True
                
        if cond3:
        
            j = output.find('im in ') - len(output)
            output = output[j + 6:]
            if output.count('im in ') == 0:
                cond3 = False
                flushed = True
                 
    if flushed:
    
        channel = message.channel
        await channel.send(f'i\'m {output.lower()} :flushed::flushed:')

client.run(token)

