import discord
from discord.ext import commands
import password as fonk
import random
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} logined.')

@bot.command()
async def markerbot(ctx):
    await ctx.send(f'Hey there, its Marker, a discord bot! Type bothelp to learn more.')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} Joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def subtract(ctx, left: int, right: int):
    """Subtracts two numbers together."""
    await ctx.send(left - right)

@bot.command()
async def multiple(ctx, left: int, right: int):
    """Multiples two numbers together."""
    await ctx.send(left * right)

@bot.command()
async def divide(ctx, left: int, right: int):
    """Divides two numbers together."""
    await ctx.send(left / right)

@bot.command()
async def password(ctx):
    şifre = fonk.parola()
    await ctx.send(şifre)

@bot.command()
async def mathelp(ctx):
    await ctx.send(f'Let me explain it to you with an example. If you want to add numbers, you have to use **/add 1 1** command. So you have to type the command first then type the numbers you want to add.')

@bot.command()
async def meme(ctx):
    a = random.randint(1, 3)
    if a == 1:
        with open('C:\\Users\\acer Aspire 3\\Desktop\\Python Pro\\images\\meme1.png.png', 'rb') as f:
            picture = discord.File(f)
    elif a == 2:
        with open('C:\\Users\\acer Aspire 3\\Desktop\\Python Pro\\images\\meme2.png.png', 'rb') as f:
            picture = discord.File(f)
    elif a == 3:
        with open('C:\\Users\\acer Aspire 3\\Desktop\\Python Pro\\images\\meme3.png.png', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def bothelp(ctx):
    await ctx.send(f'These are my commands that you can use:   **bothelp, mathelp, markerbot, meme, heh, password, add, subtract, multiple, divide**')

bot.run("token here")