import os
import discord
from discord.ext import commands 
from dotenv import load_dotenv
from start_server import start_server


intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')
SCRIPT_PATH = os.getenv('SCRIPT_PATH')

client = commands.Bot(command_prefix="$", intents=intents)
client.remove_command("help")

# When bot logs in 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# Start server  
@client.command()
async def start(ctx):  # starts server 
    start_server(SCRIPT_PATH)
    await ctx.send("Starting Server")

# Stop server  
@client.command()
async def stop(ctx):  # starts server 
    await ctx.send("Stopping Server")

client.run(TOKEN)