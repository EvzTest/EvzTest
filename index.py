import discord
from discord.ext import commands
from discord.ext.commands import context
import datetime

bot = commands.Bot(command_prefix= '>', description= 'This is a helper bot')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f'Información', description= 'Hola buenas, si escribise este comando seguramente seas alguien interesado por IsHectron, bueno pues toda la info la tienes en sus respectivos canales', timestamp=datetime.datetime.utcnow())
    await ctx.send(embed=embed)

@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send('**El resultado de la suma es**'),
    await ctx.send(numOne + numTwo)

@bot.command()
async def rest(ctx, numOne: int, numTwo: int):
    await ctx.send('**El resultado de la resta es**')
    await ctx.send(numOne - numTwo)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name='IsHectron',
    url= "https://www.twitch.tv/ishectron"))
    print('My bot is ready')

bot.run('ODQyODI3MjY2ODc3ODE2OTIy.YJ6-Dw.65qdI2S8VWsPFgs9O1NkEt8BQ0Q')
