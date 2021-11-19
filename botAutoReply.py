import discord
from discord.ext import tasks

# Send a message every 60 minutes
x = 1
channel = "challenges"

@tasks.loop(minutes=x)
async def send():
    response = "Holiwiwi"
    channel.send(response)

@send.before_loop
async def before():
    await bot.wait_until_ready()

send.start()