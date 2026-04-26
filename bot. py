import discord
from discord.ext import commands
import random
import asyncio

# Настройки
PREFIX = '!'
bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())

# ==========================================
# НАЗВАНИЕ СЕРВЕРА
# ==========================================
SERVER_NAME = "Script_Server"
SERVER_INVITE = "https://discord.gg/9qY2GJ3UQR"
GITHUB_LINK = "https://github.com/murzabekovmansur06-source"

# ==========================================
# БАЗА ЗНАНИЙ (ОТВЕЧАЕТ КАК ИИ)
# ==========================================
GREETINGS = ['Привет', 'Здарова', 'Хай', 'Приветствую', 'Здарово']
FAREWELLS = ['Пока', 'До связи', 'Удачи', 'Бывай']

ANSWERS = {
    'как дела': [
        'Отлично! Жду новых скриптов.',
        'Всё пучком. Сервер живёт!',
        'Работаю, не мешай :)',
        'Лучше всех!'
    ],
    'что делаешь': [
        'Слежу за сервером Script_Server.',
        'Думаю над новым античитом.',
        'Жду, когда Valentine Hub обновится.',
        'Проверяю чат на нарушения.'
    ],
    'кто ты': [
        'Я бот-помощник Script_Server. Создан чтобы помогать скриптерам.',
        'Я ассистент, созданный Мансуром. Могу объяснить скрипты, модерировать чат и отвечать на вопросы.',
    ],
    'спс': ['Всегда пожалуйста!', 'Обращайся.', 'Рад помочь!'],
    'спасибо': ['Не за что!', 'Пожалуйста.', 'Для тебя — всё что угодно.'],
    'как тебя зовут': ['Я Script_Bot, помощник на Script_Server.', 'Меня зовут Script_Bot.'],
    'кто тебя создал': ['Меня создал Мансур (TN_ZADOLBAL).', 'Мой создатель — Мансур, автор Valentine Hub и Sentinel Omega.'],
    'что ты умеешь': [
        'Я умею объяснять скрипты, модерировать чат, приветствовать новичков и отвечать на вопросы.',
        'Могу рассказать про GodMode, ESP, античиты и многое другое. Напиши `!помощь`.'
    ],
    'где взять скрипты': [
        f'Все скрипты на GitHub: {GITHUB_LINK}',
        'Загляни в канал #бесплатные-скрипты или на GitHub.',
        'Напиши `!скрипты` — я дам ссылку.'
    ],
    'как заказать скрипт': [
        'Напиши Мансуру в личку или создай тикет.',
        'Заказы принимаются через админа сервера.',
        'Пиши в #общий-чат, админ ответит.'
    ],
    'как стать скриптером': [
        'Начни с Lua. Вот план:\n1. Изучи основы Roblox Studio\n2. Научись работать с Players, Workspace, ReplicatedStorage\n3. Попробуй написать простой ESP\n4. Изучай чужие скрипты на нашем сервере',
        'В канале #разбор-кода есть гайды для новичков. Начни с них!'
    ],
    'lua': [
        'Lua — это язык скриптов в Roblox. На нём пишут читы, античиты и игровые механики.',
        'Lua прост в изучении. Если знаешь Python — Lua покажется лёгким.'
    ],
    'c++': [
        'C++ используется для серьёзного взлома: внешние читы, драйверы, обход Hyperion.',
        'На C++ пишут то, что нельзя сделать на Lua: чтение памяти, инжекты, kernel-level.'
    ],
    'hyperion': [
        'Hyperion (Byfron) — это античит Roblox на уровне ядра. Обойти его можно только через драйвер.',
        'Hyperion проверяет целостность процесса. Обычные инжекты он палит мгновенно.'
    ],
    'byfron': [
        'Byfron — то же самое что Hyperion. Защита от читеров на C++.',
        'Byfron сложно обойти. Для этого нужен kernel-level доступ.'
    ],
}

# ==========================================
# БАЗА ЗНАНИЙ ДЛЯ !объясни
# ==========================================
SCRIPT_EXPLANATIONS = {
    # GodMode
    'godmode': '**GodMode** делает персонажа бессмертным.\n\n'
               'Как работает:\n'
               '1. Находит Humanoid игрока\n'
               '2. Каждые 0.1 секунды устанавливает Health = MaxHealth\n'
               '3. Можно обойти, если сервер проверяет урон\n\n'
               'Пример кода: `hum.Health = hum.MaxHealth`',
    
    'god mode': 'Смотри объяснение GodMode.',
    
    'бессмертие': 'Смотри объяснение GodMode.',
    
    # ESP
    'esp': '**ESP (Extra Sensory Perception)** — подсветка объектов через стены.\n\n'
           'Как работает:\n'
           '1. Сканирует Workspace через GetDescendants()\n'
           '2. Находит игроков/мобов/предметы по имени\n'
           '3. Создаёт Highlight вокруг цели\n'
           '4. Обновляется каждые 0.5 секунд\n\n'
           'Цвета:\n'
           '• Красный — враги и сущности\n'
           '• Зелёный — предметы и лут\n'
           '• Жёлтый — ключевые объекты',
    
    'подсветка': 'Смотри объяснение ESP.',
    
    # AntiCheat
    'античит': '**Sentinel Omega** — серверный античит на Lua.\n\n'
               'Защищает от:\n'
               '• SpeedHack (проверка скорости)\n'
               '• Teleport (проверка позиции)\n'
               '• GodMode (проверка урона)\n'
               '• Metatable Hooks (хэш каждые 0.5с)\n'
               '• RemoteSpam (блокировка пакетов)\n\n'
               'Нельзя обойти на Lua. Только C++ с kernel-доступом.',
    
    'анти-чит': 'Смотри объяснение античит.',
    
    'sentinel': '**Sentinel Omega** — это серверный античит.\n\n'
                'Особенности:\n'
                '• Actor-копии для защиты от удаления\n'
                '• Авто-восстановление при уничтожении\n'
                '• Проверка метатаблиц по хэшу\n'
                '• AI-анализ скриптов (Backdoor Eliminator)\n'
                '• Серверная валидация позиции и скорости\n\n'
                'GitHub: https://github.com/murzabekovmansur06-source/Sentinel-Omega-v6',
    
    # Backdoor
    'бэкдор': '**Бэкдор** — скрытый вредоносный скрипт.\n\n'
              'Признаки:\n'
              '• Использует loadstring()\n'
              '• Отправляет данные на webhook\n'
              '• Прячется в CoreGui\n'
              '• Обфусцирован (string.char, getfenv)\n\n'
              '**Backdoor Eliminator** находит их через AI-анализ кода.',
    
    'backdoor': 'Смотри объяснение бэкдор.',
    
    # Farm
    'фарм': '**Автофарм** — автоматическая прокачка.\n\n'
            'Как работает:\n'
            '1. Ищет ближайших мобов\n'
            '2. Телепортируется к цели\n'
            '3. Атакует (клики или Aimbot)\n'
            '4. Собирает лут\n'
            '5. Повторяет\n\n'
            'В Blox Fruits фарм привязан к квестам по уровням.',
    
    'автофарм': 'Смотри объяснение фарм.',
    
    'auto farm': 'Смотри объяснение фарм.',
    
    # Aimbot
    'aimbot': '**Aimbot** — автоматическое прицеливание.\n\n'
              'Как работает:\n'
              '1. Находит ближайшего врага в FOV\n'
              '2. Рассчитывает угол между камерой и целью\n'
              '3. Плавно поворачивает камеру\n'
              '4. Автоматически стреляет\n\n'
              'На C++ работает через запись углов в память камеры.',
    
    # NoClip
    'noclip': '**NoClip** — хождение сквозь стены.\n\n'
              'Как работает:\n'
              '1. Находит все BasePart в Character\n'
              '2. Устанавливает CanCollide = false\n'
              '3. Можно также отключить коллизию у дверей\n\n'
              'Пример кода: `part.CanCollide = false`',
    
    # SpeedHack
    'speedhack': '**SpeedHack** — увеличение скорости.\n\n'
                 'На Lua:\n'
                 '• Установка hum.WalkSpeed = 50\n'
                 '• Сервер может проверить и забанить\n\n'
                 'На C++:\n'
                 '• Запись в память Humanoid.WalkSpeed\n'
                 '• Спуфинг позиции для обхода серверной проверки',
    
    'speed': 'Смотри объяснение speedhack.',
    
    # Fly
    'fly': '**Fly** — полёт.\n\n'
           'Методы:\n'
           '1. BodyVelocity — создать силу, толкающую вверх\n'
           '2. CFrame — телепортировать персонажа в воздух\n'
           '3. Память (C++) — записать скорость напрямую\n\n'
           'Сервер может задетектить через проверку Position.Y.',
    
    # Teleport
    'телепорт': '**Телепорт** — мгновенное перемещение.\n\n'
                'На Lua:\n'
                '• hrp.CFrame = CFrame.new(x, y, z)\n'
                '• Сервер видит скачок позиции\n\n'
                'На C++:\n'
                '• Запись в память HumanoidRootPart.Position\n'
                '• Спуфинг для скрытия от сервера',
    
    'tp': 'Смотри объяснение телепорт.',
    
    # Remote
    'remote': '**RemoteEvent** — способ общения клиента с сервером.\n\n'
              '• FireServer — отправить на сервер\n'
              '• OnClientEvent — получить от сервера\n\n'
              'Читы перехватывают ремоуты через __namecall или getconnections.',
    
    # Metatable
    'метатаблица': '**Метатаблицы** — основа Lua.\n\n'
                   'В Roblox через getrawmetatable можно:\n'
                   '• Хукнуть __index (чтение свойств)\n'
                   '• Хукнуть __namecall (вызов методов)\n'
                   '• Подменить Kick, Destroy, WalkSpeed\n\n'
                   'Sentinel Omega проверяет целостность метатаблиц каждые 0.5с.',
    
    # Kernel
    'kernel': '**Kernel-level** — уровень ядра Windows.\n\n'
              'Программы на kernel имеют полный доступ к памяти.\n\n'
              '• Sentinel Omega бессилен против kernel-чита\n'
              '• Hyperion/Byfron работает на kernel\n'
              '• Для обхода нужен драйвер (.sys)\n'
              '• Пишется на C++ с WDK',
}

# ==========================================
# ФУНКЦИЯ УМНОГО ПОИСКА
# ==========================================
def find_best_answer(question):
    """Ищет наиболее подходящий ответ по ключевым словам"""
    question_lower = question.lower()
    
    # Сначала точное совпадение
    for key, responses in ANSWERS.items():
        if key in question_lower:
            return random.choice(responses)
    
    # Частичное совпадение
    for key, responses in ANSWERS.items():
        words = key.split()
        if any(word in question_lower for word in words):
            return random.choice(responses)
    
    return None

def find_script_explanation(term):
    """Ищет объяснение скрипта с учётом синонимов"""
    term_lower = term.lower()
    
    for key, explanation in SCRIPT_EXPLANATIONS.items():
        if key in term_lower or term_lower in key:
            return explanation
    
    return None

# ==========================================
# СОБЫТИЯ БОТА
# ==========================================
@bot.event
async def on_ready():
    print(f'✅ {bot.user} запущен на {SERVER_NAME}!')
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=f'за {SERVER_NAME}'
        )
    )

@bot.event
async def on_member_join(member):
    """Приветствие нового участника"""
    channel = discord.utils.get(member.guild.text_channels, name='общий-чат')
    if channel:
        embed = discord.Embed(
            title=f'👋 Добро пожаловать, {member.name}!',
            description=f'Ты на сервере **{SERVER_NAME}**!\n\n'
                        '📜 Читай правила в #правила\n'
                        '📥 Бесплатные скрипты в #бесплатные-скрипты\n'
                        '⭐ Эксклюзивы в #эксклюзивы\n'
                        '🧠 Разбор кода в #разбор-кода\n'
                        '🛡️ Античиты в #античит-защита\n\n'
                        f'Напиши `!помощь` чтобы узнать команды.\n'
                        f'Напиши `!объясни [термин]` чтобы понять скрипты.',
            color=0x9B59B6
        )
        embed.set_thumbnail(url=member.avatar.url)
        embed.set_footer(text=f'{SERVER_NAME} • GitHub: {GITHUB_LINK}')
        await channel.send(embed=embed)

@bot.event
async def on_message(message):
    """Отвечает на обычные сообщения (как ИИ)"""
    if message.author.bot:
        return
    
    msg_lower = message.content.lower()
    
    # Приветствия
    if any(greeting.lower() in msg_lower for greeting in GREETINGS):
        greeting = random.choice(GREETINGS)
        await message.channel.send(f'{greeting}, {message.author.name}!')
        return
    
    # Прощания
    if any(farewell.lower() in msg_lower for farewell in FAREWELLS):
        await message.channel.send(f'{random.choice(FAREWELLS)}, {message.author.name}! Заходи ещё!')
        return
    
    # Упоминание сервера
    if 'script_server' in msg_lower or 'script server' in msg_lower:
        await message.channel.send(f'{SERVER_NAME} — лучший сервер для скриптеров Roblox!')
        return
    
    # Умный поиск ответа
    answer = find_best_answer(message.content)
    if answer:
        await message.channel.send(answer)
        return
    
    # Если ничего не нашли — НЕ отвечаем, чтобы не спамить
    # Но обрабатываем команды
    await bot.process_commands(message)

# ==========================================
# КОМАНДЫ БОТА
# ==========================================
@bot.command()
async def помощь(ctx):
    """Список всех команд"""
    embed = discord.Embed(
        title='🛠️ Команды Script_Bot',
        description=f'Бот сервера **{SERVER_NAME}**',
        color=0x9B59B6
    )
    embed.add_field(name='📖 Обучение', value='`!объясни [термин]` — объяснить работу скрипта\n`!скрипты` — ссылка на GitHub', inline=False)
    embed.add_field(name='🛡️ Модерация', value='`!очистить [кол-во]` — удалить сообщения\n`!бан [@юзер]` — забанить участника\n`!кик [@юзер]` — кикнуть участника', inline=False)
    embed.add_field(name='📢 Сервер', value='`!дискорд` — ссылка на сервер\n`!правила` — правила сервера', inline=False)
    embed.add_field(name='💡 Примеры', value='`!объясни godmode`\n`!объясни esp`\n`!объясни античит`\n`!объясни фарм`', inline=False)
    embed.set_footer(text=f'{SERVER_NAME} • GitHub: {GITHUB_LINK}')
    await ctx.send(embed=embed)

@bot.command()
async def объясни(ctx, *, term=None):
    """Объясняет работу скрипта"""
    if not term:
        await ctx.send('❌ Укажи термин. Пример: `!объясни godmode`\nНапиши `!помощь` для списка команд.')
        return
    
    explanation = find_script_explanation(term)
    
    if explanation:
        embed = discord.Embed(
            title=f'📖 {term.upper()}',
            description=explanation,
            color=0x3498DB
        )
        embed.set_footer(text=f'{SERVER_NAME} • Запросил: {ctx.author.name}')
        await ctx.send(embed=embed)
    else:
        await ctx.send(f'❌ Пока не знаю про **{term}**.\nМансур добавит это в базу знаний. Напиши ему!')

@bot.command()
async def скрипты(ctx):
    """Ссылка на скрипты"""
    embed = discord.Embed(
        title='📥 Бесплатные скрипты',
        description=f'Все скрипты доступны на GitHub:\n{GITHUB_LINK}\n\n'
                    'Также загляни в канал #бесплатные-скрипты',
        color=0x2ECC71
    )
    embed.set_footer(text=f'{SERVER_NAME}')
    await ctx.send(embed=embed)

@bot.command()
async def дискорд(ctx):
    """Ссылка на сервер"""
    await ctx.send(f'🔗 Приглашение на {SERVER_NAME}:\n{SERVER_INVITE}')

@bot.command()
async def правила(ctx):
    """Правила сервера"""
    embed = discord.Embed(
        title=f'📜 Правила {SERVER_NAME}',
        description='1. Не оскорблять участников\n'
                    '2. Не спамить и не флудить\n'
                    '3. Не рекламировать другие серверы\n'
                    '4. Не сливать эксклюзивные скрипты\n'
                    '5. Уважать модераторов\n'
                    '6. За нарушение — бан без предупреждения',
        color=0xE74C3C
    )
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def очистить(ctx, amount: int = 10):
    """Удаляет сообщения"""
    await ctx.channel.purge(limit=amount + 1)
    msg = await ctx.send(f'✅ {ctx.author.name}, удалено {amount} сообщений.')
    await asyncio.sleep(3)
    await msg.delete()

@bot.command()
@commands.has_permissions(ban_members=True)
async def бан(ctx, member: discord.Member, *, reason='Нарушение правил'):
    """Банит участника"""
    await member.ban(reason=reason)
    await ctx.send(f'💀 {member.name} забанен. Причина: {reason}')

@bot.command()
@commands.has_permissions(kick_members=True)
async def кик(ctx, member: discord.Member, *, reason='Нарушение правил'):
    """Кикает участника"""
    await member.kick(reason=reason)
    await ctx.send(f'👢 {member.name} кикнут. Причина: {reason}')

# ==========================================
# ОБРАБОТКА ОШИБОК
# ==========================================
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('❌ У тебя нет прав для этой команды.')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('❌ Не хватает аргументов. Напиши `!помощь`.')
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send('❌ Участник не найден.')
    else:
        await ctx.send(f'❌ Ошибка: {error}')

# ==========================================
# ЗАПУСК
# ==========================================
bot.run('YOUR_BOT_TOKEN')
