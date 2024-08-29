import discord, asyncio, os, time, platform
from discord.ext import commands
from datetime import timedelta
from discord import app_commands
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from colorama import Fore, Style

# Note :- Do not try to optimize the code if you think it can be made faster. This code is running at its best.
# Made by antixdev
# Discord username :- antixdev
############################################
tkn =  os.getenv('token')
x = 2419200 # Do not change
############################################
hehe = "\x1b[38;5;56m"
w = "\033[1;37m"
red="\x1b[38;5;196m"
g="\x1b[38;5;34m"
r = Style.RESET_ALL

def cls():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

intents = discord.Intents.all()
client = commands.Bot(command_prefix='$', intents=intents)

@client.event
async def on_ready():
    cls()
    print(f'{hehe}[{g}+{hehe}] Logged in as {client.user.name}{r}')
    time.sleep(3)

@client.command()
async def scrape(ctx):
    guild = ctx.guild
    with open('members.txt', 'w') as file:
        count = 0 
        for m in guild.members:
            if not m.bot:
                file.write(f'{m.id}\n')
                count += 1
                cls()
                print(f'{hehe}[{g}+{hehe}]{hehe}Scraped : {count}{r}')
                
@client.command()
async def timeout(ctx):
    cls()
    sc = 0
    fc = 0
    guild = ctx.guild
    d = timedelta(seconds=x)
    semaphore = asyncio.Semaphore(5)
    with open('members.txt', 'r') as file:
        ids = [line.strip() for line in file.readlines()]
    async def fuck(idk):
        nonlocal sc, fc
        m = guild.get_member(int(idk))
        if m:
            try:
                await m.timeout(d, reason="Slap By Switch")
                print(f'{hehe}[{g}+{hehe}]{hehe} Successfully timed out {m.name} for 28 Days.{r}')
                sc += 1
            except Exception as e:
                print(f'{hehe}[{red}-{hehe}]{hehe} Cannot timeout {m.name}{r}')
                fc += 1
        else:
            print(f'{hehe}[{r}!{hehe}]{hehe} Member with ID {idk} not found.{r}')
            fc += 1
    async def stfu(idk):
        async with semaphore:
            await fuck(idk)
    await asyncio.gather(*(stfu(idk) for idk in ids))
    time.sleep(3)
    cls()
    print(f'{hehe}[{g}+{hehe}]{hehe} Successfully timed out {sc} members{r}\n{hehe}[{red}-{hehe}]{hehe} Failed to timeout {fc} members.{r}')

client.run(tkn)
