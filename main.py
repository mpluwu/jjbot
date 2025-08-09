import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

#######################

import requests


# Where USD is the base currency you want to use
url = 'https://v6.exchangerate-api.com/v6/593f8bebf6f46f51ff3cb380/latest/USD'

# Making our request
response = requests.get(url)
data = response.json()

# Your JSON object

#########################


load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content=True
intents.members=True


#bot = commands.Bot(command_prefix='/', intents=intents)
bot=commands.Bot("/", intents=intents)

@bot.event
async def on_ready():
    print(f"yoo what's good, mate? {bot.user.name}")
    await bot.tree.sync()

@bot.event
async def on_member_join(member):
    await member.send(f"It's great to see you here, sup {member.name}?")




#MESSAGE EVENTS


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "jayjay" in message.content.lower():
        await message.channel.send("Damian, is that you??? I've missed you...")
    if "mr.stabby" in message.content.lower():
        await message.channel.send("Dami doesn't like that nick >:c")
    if "damian" in message.content.lower():
        await message.channel.send("he hasn't contacted me for years now... I hope he is ok")
    await bot.process_commands(message)


#MESSAGE EVENTS END


############################helpppppppppppppppppppppppppppppp

@bot.tree.command(name="help",description="Helps you with commands")
async def slash_command(interaction:discord.Interaction):
    await interaction.channel.send(file=discord.File('hey.jpg'))
    await interaction.response.send_message("Hi and thanks for using me! Here are the commands you can use: \n\n**/hello** - Greet any member\n**/convert** - Convert currency\n**/currency** - Check if you can convert between two currencies \n\n*STILL IN DEVELOPMENT!!!*")

#############################helppppppppppppppppppppppppppppppppp


@bot.tree.command(name="hello",description="Hello-es you")
async def slash_command(interaction:discord.Interaction, user:discord.Member):
    await interaction.response.send_message(f"Sup mate?? It's cool to have you here, {user.mention}.")

@bot.tree.command(name="convert",description="Convert your money")
async def convert(interaction: discord.Interaction, amount: int, from_unit: str, to_unit: str):
    conversion_rates = data.get('conversion_rates',{})
    if from_unit.upper() not in conversion_rates or to_unit.upper() not in conversion_rates:
        await interaction.response.send_message("Erm, could you take a look at the units again??")
        return
    converted_amount = amount * (conversion_rates[to_unit.upper()] / conversion_rates[from_unit.upper()])
    await interaction.response.send_message(f"{amount} {from_unit.upper()} is equal to {converted_amount} {to_unit.upper()}.")

@bot.tree.command(name="currency", description="Get a list of available currency units")
async def currency(interaction: discord.Interaction, from_unit: str, to_unit: str):
    conversion_rates = data.get('conversion_rates',{})
    if from_unit.upper() not in conversion_rates or to_unit.upper() not in conversion_rates:
        await interaction.response.send_message("Erm, could you take a look at the units again??")
        return
    else:
        await interaction.response.send_message(f"Yes, you can convert from {from_unit.upper()} to {to_unit.upper()}.")


bot.run(token, log_handler=handler, log_level=logging.DEBUG)
