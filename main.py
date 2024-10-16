import discord
from discord.ext import commands
import os, random
from get_model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            nama_file = file.filename
            url_fil = file.url
            await file.save(f'./{nama_file}')
            await ctx.send(f'file telah disimpan dengan nama {nama_file}')

            nama, skor = get_class(image=nama_file, model='keras_model.h5', label='labels.txt')

            #inferensi
            if nama == 'tom_hiddleston\n' and skor >= 0.65:
                await ctx.send('Orang ini lebih mirip dengan Tom Hiddleston')
                await ctx.send('Kamu tampak keren sekali hari ini!')
            elif nama == 'logan_marshall\n' and skor >= 0.65:
                await ctx.send('Orang ini lebih mirip dengan Logan Marshall')
                await ctx.send('Kamu terlihat ganteng di foto itu!')
            else:
                await ctx.send('hmm, aku bingung menentukan orang ini lebih mirip siapa')       
    else:
        await ctx.send("gambarnya mana woi")

bot.run("token here :)")
