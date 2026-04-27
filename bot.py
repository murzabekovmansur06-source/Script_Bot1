import discord
from discord.ext import commands

# Простейшие интенты
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Бот {bot.user} запущен!')

@bot.command()
async def привет(ctx):
    await ctx.send(f'Привет, {ctx.author.name}!')

@bot.command()
async def помощь(ctx):
    await ctx.send('Команды: !привет, !помощь')

bot.run('DISCORD_TOKEN')
