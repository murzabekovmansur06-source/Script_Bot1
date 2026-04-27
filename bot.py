import discord
from discord.ext import commands
import random
import asyncio
import os

PREFIX = '!'

# НАСТРОЙКИ ИНТЕНТОВ — БЕЗ ЛИШНИХ ПРИВИЛЕГИЙ, ТОЛЬКО БАЗА
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

SERVER_NAME = "Script_Server"
SERVER_INVITE = "https://discord.gg/9qY2GJ3UQR"
GITHUB_LINK = "https://github.com/murzabekovmansur06-source"

GREETINGS = ['Привет', 'Здарова', 'Хай', 'Приветствую', 'Здарово']
FAREWELLS = ['Пока', 'До связи', 'Удачи', 'Бывай']

ANSWERS = {
    'как дела': ['Отлично! Жду новых скриптов.', 'Всё пучком.', 'Работаю, не мешай :)'],
    'что делаешь': ['Слежу за сервером Script_Server.', 'Думаю над новым античитом.'],
    'кто ты': ['Я бот-помощник Script_Server. Создан чтобы помогать скриптерам.'],
    'спс': ['Всегда пожалуйста!', 'Обращайся.', 'Рад помочь!'],
}

SCRIPT_EXPLANATIONS = {
    'godmode': '**GodMode** делает персонажа бессмертным. Устанавливает Health = MaxHealth.',
    'esp': '**ESP** — подсветка игроков через стены с помощью Highlight.',
    'античит': '**Sentinel Omega** — серверный античит. Проверяет скорость, позицию, метатаблицы.',
    'фарм': '**Автофарм** — автоматическая прокачка. Ищет мобов, телепортируется, атакует.',
}

def find_best_answer(question):
    question_lower = question.lower()
    for key, responses in ANSWERS.items():
        if key in question_lower:
            return random.choice(responses)
    return None

def find_script_explanation(term):
    term_lower = term.lower()
    for key, explanation in SCRIPT_EXPLANATIONS.items():
        if key in term_lower or term_lower in key:
            return explanation
    return None

@bot.event
async def on_ready():
    print(f'✅ {bot.user} запущен на {SERVER_NAME}!')
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(type=discord.ActivityType.watching, name=f'за {SERVER_NAME}')
    )

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    msg_lower = message.content.lower()
    
    if any(greeting.lower() in msg_lower for greeting in GREETINGS):
        greeting = random.choice(GREETINGS)
        await message.channel.send(f'{greeting}, {message.author.name}!')
        return
    
    if any(farewell.lower() in msg_lower for farewell in FAREWELLS):
        await message.channel.send(f'{random.choice(FAREWELLS)}, {message.author.name}! Заходи ещё!')
        return
    
    answer = find_best_answer(message.content)
    if answer:
        await message.channel.send(answer)
        return
    
    await bot.process_commands(message)

@bot.command()
async def помощь(ctx):
    embed = discord.Embed(title='🛠️ Команды Script_Bot', description=f'Бот сервера **{SERVER_NAME}**', color=0x9B59B6)
    embed.add_field(name='📖 Обучение', value='`!объясни [термин]` — объяснить работу скрипта\n`!скрипты` — ссылка на GitHub', inline=False)
    embed.add_field(name='📢 Сервер', value='`!дискорд` — ссылка на сервер\n`!правила` — правила сервера', inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def объясни(ctx, *, term=None):
    if not term:
        await ctx.send('❌ Укажи термин. Пример: `!объясни godmode`')
        return
    explanation = find_script_explanation(term)
    if explanation:
        await ctx.send(embed=discord.Embed(title=term.upper(), description=explanation, color=0x3498DB))
    else:
        await ctx.send(f'❌ Пока не знаю про **{term}**.')

@bot.command()
async def скрипты(ctx):
    await ctx.send(f'📥 Все скрипты на GitHub: {GITHUB_LINK}')

@bot.command()
async def дискорд(ctx):
    await ctx.send(f'🔗 Приглашение на {SERVER_NAME}: {SERVER_INVITE}')

@bot.command()
async def правила(ctx):
    await ctx.send('📜 Правила: 1. Не оскорблять 2. Не спамить 3. Уважать модераторов')

bot.run(os.environ['DISCORD_TOKEN'])
