import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content=True
intents.members=True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f"yoo what's good, mate? {bot.user.name}")

@bot.event
async def on_member_join(member):
    await member.send(f"It's great to see you here, sup {member.name}?")




#MESSAGE EVENTS


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "JayJay" in message.content.lower():
        await message.channel.send("Damian, is that you??? I've missed you...")
    if "mr.stabby" in message.content.lower():
        await message.channel.send("Dami doesn't like that nick >:c")
    if "damian" in message.content.lower():
        await message.channel.send("he hasn't contacted me for years now... I hope he is ok")
    await bot.process_commands(message)


#MESSAGE EVENTS END


@bot.command()
async def hello(ctx):
    await ctx.send(f"Sup mate?? It's cool to have you here, {ctx.author.mention}.")

@bot.command()
async def convert(ctx, amount: int, from_unit: str, to_unit:str):
    conversion_rates = {
        'usd' :1.0,
        'azn' : 1.7,
        'eur':0.86
    }
    if from_unit.lower() not in conversion_rates or to_unit.lower()not in conversion_rates:
        await ctx.send("Erm, could you take a look at the units again??")
        return
    converted_amount = amount*(conversion_rates[to_unit.lower()] / conversion_rates[from_unit.lower()])
    await ctx.send(f"{amount} {from_unit.upper()} is equal to {converted_amount} {to_unit.upper()}.")

@bot.command()
async def currency(ctx):
    await ctx.send("USD (usd), AZN (azn), EURO (eur)")



bot.run(token, log_handler=handler, log_level=logging.DEBUG)