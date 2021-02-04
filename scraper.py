import asyncio
import discord
import os
import requests


discord.Intents.all()
pref = '//'

async def grabpfp(id, message):
    server = message.guild
    for member in server.members:

        with open(f'stolenpfps\{member}s-pfp.png', 'wb+') as f:
            r = requests.get(member.avatar_url, stream=True)
            for block in r.iter_content(1024):
                if not block:
                    break
                f.write(block)
        print(f'Stole {member}\'s pfp')
    print('finished stealing profile pictures\n\n')
        
async def logusers(id, message):
    server = message.guild
    with open('INFO.txt', 'a') as f:
        for member in server.members:
            userid = member.id
            nickname = member.display_name
            try:
                f.write(f"Username and Discrim: {member}\nUser ID: {userid}\nDisplay Name: {nickname}\n\n\n")
                print(f'{member}s information has been logged')
            except:
                pass
        print('Finished logging user information')

class sex(discord.Client):
 
    async def on_message(self, message):
        content = message.content.split(' ')
        
        if (content[0] == "{0}scrape".format(pref)):
                server = message.guild
                await grabpfp(server, message)
                await logusers(server, message)


    async def on_connect(self):
        os.system('cls')
        print("bot online")
        botID = self.user.id
        

client = sex(intents=discord.Intents.all())
client.run('TOKEN HERE', bot=True)