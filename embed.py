import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game

Client = discord.client
client = commands.Bot(command_prefix = ".")
Clientdiscord = discord.Client()

@client.event
async def on_ready():
    print("Ready, freddy")

@client.event
async def on_message(message):
    if message.content.startswith("!description"):
        em = discord.Embed(title="Syna", description="This bot is a multi functional bot with cool commands.", colour=0x4262f4)
        em.set_author(name= message.author.nick, icon_url="https://pbs.twimg.com/profile_images/1067109121109852161/oWWL9D_8_400x400.jpg")
        em.set_image(url="https://pbs.twimg.com/profile_images/1067109121109852161/oWWL9D_8_400x400.jpg")
        em.set_thumbnail(url= message.server.icon_url)
        em.add_field(name= "Syna", value="Created by enderman slayerr#6740")
        await client.send_message(message.channel, embed=em)
    if message.content.startswith("!cmds"):
        em = discord.Embed(title="commands", description="!description - gives you a description.", colour=0x4262f4)
        em.set_author(name= message.author.nick, icon_url="https://pbs.twimg.com/profile_images/1067109121109852161/oWWL9D_8_400x400.jpg")
        em.set_image(url="https://pbs.twimg.com/profile_images/1067109121109852161/oWWL9D_8_400x400.jpg")
        em.set_thumbnail(url= message.server.icon_url)
        em.add_field(name= "Syna", value="Created by enderman slayerr#6740")
        await client.send_message(message.channel, embed=em)















client.run("NTMxNDU2NjgyNjEwMzkzMDk5.DxONYg.kqRUkcWUTzIiWZpwLt0Fgs0Iapg")
