from discord.ext import commands
import os
import traceback
import random
import discord
import nDnDICE

bot = commands.Bot(command_prefix='*')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.command()
async def hello(ctx):
    await ctx.send('こんにちは、お兄ちゃん。')
	
@bot.event
async def on_message(ctx):
    msg = ctx.content
    result = nDnDICE.nDn(msg)
    if result is not None:
        await client.send_message(ctx.channel, result)

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send('お兄ちゃん、それはわからないよ。')

bot.run(token)
