# https://realpython.com/how-to-make-a-discord-bot-python/
# Discord bot python

# General imports
import os
import random
import logging
# Discord imports
# from discord.errors import DiscordException
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN')
logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    # This event triggers once the bot is ready and connected
    logging.info("====================================================")
    logging.info(f'{bot.user.name} has connected to discord')


@bot.command(name='yo')
async def hello(ctx):
    greetings = [
            'Salutations',
            'Sup',
            'wazaaaap'
            ]

    response = random.choice(greetings)
    await ctx.send(response)

    # Error Handling - See GH-2 for progress
# async def on_error(self, event, *args, **kwargs):
#    # This event triggers when an error occurs, so we setup the
#    # error handlers here to log the error to a log file.
#    with open('err.log', 'a') as err_file:
#        if event == 'on_message':
#            logging.error(
#                    'Encountered error when reading a message: '
#                     f'{args[0]}'
#                     )
#             err_file.write(f'Unhandled message: {args[0]}\n')
#         else:
#             raise Exception

# What actually runs it
bot.run(TOKEN)
