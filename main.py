import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='sf!', intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Game(name = "sf!help - command of help", type = 3), status = discord.Status.idle)
    print('Start "Sudo Florest"...')
    print('Bot create by Florest, 28.01.2023')
    print('Bot launched successfully.')

@bot.command()
async def hi(ctx):
    await ctx.send('> Hi, dear user!\nhttps://tenor.com/bVNhY.gif')

@bot.command()
async def bye(ctx):
    await ctx.send('> Bye, dear user...\nhttps://tenor.com/Xp6Y.gif')

@bot.command()
async def help(ctx):
    await ctx.send('```Hey! This is the "Sudo Florest" bot help command.\nInteractions:\nsh!hi - say hello to everyone on the server\nsf!bye - say goodbye to everyone on the servers\nf!angry - be angry\nsf!happy - be happy.\nRest:\nsf!botinfo - information about the bot.```')

@bot.command()
async def botinfo(ctx):
    await ctx.send('```Information of bot:\nBot developer: FlorestOne4185 (ID: 822177174802006037)\nBot version: 1.0.1\nDate of create: the 28th of January 2023 year\nSupport server: https://discord.gg/Ww8XFWDdWd```')

@bot.command()
async def angry(ctx):
    await ctx.send('> User is very angry!\nhttps://tenor.com/bvKQU.gif')

@bot.command()
async def happy(ctx):
    await ctx.send('> User is very happy!\nhttps://tenor.com/bydBX.gif')

bot.run('token')