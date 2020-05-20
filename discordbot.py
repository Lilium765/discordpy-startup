from discord.ext import commands
import os
import traceback
import random
import discord
import nDnDICE

client = discord.Client()

bot = commands.Bot(command_prefix='*')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.command()
async def hello(ctx):
    await ctx.send('こんにちは、お兄ちゃん。')
	
@client.event
async def on_message(message):
    msg = message.content
    result = nDnDICE.nDn(msg)
    if result is not None:
        await client.send_message(message.channel, result)

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send('お兄ちゃん、それはわからないよ。')

bot.run(token)
client.run(token)
