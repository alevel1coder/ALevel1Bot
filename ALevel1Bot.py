# https://realpython.com/how-to-make-a-discord-bot-python/
# Discord bot python

# General imports
import os
import random
import logging
# Discord imports
from discord import Client, Message
from discord.errors import DiscordException
from dotenv import load_dotenv

load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN')
logging.basicConfig(level=logging.INFO)

class CustomClient(Client):
    async def on_ready(self):
        # This event triggers once the bot is ready and connected
        logging.info("====================================================")
        logging.info(f'{self.user} has connected to discord')

    async def on_message(self, Message):
        # This event should trigger when a message is posted in channel the
        # bot has access to. Currently it responds to specific messages.
        if Message.author == client.user:
            return

        random_responses = [
                'Bongo',
                'Banana',
                'Monke',
                ]

        if Message.content == 'bingo':
            response = random.choice(random_responses)
            await Message.channel.send(response)
        if Message.content == 'raise-exception':
            raise DiscordException

    async def on_error(self, event, *args, **kwargs):
        # This event triggers when an error occurs, so we setup the
        # error handlers here to log the error to a log file.
        with open('err.log', 'a') as err_file:
            if event == 'on_message':
                logging.error(
                        'Encountered error when reading a message: '
                        f'{args[0]}'
                        )
                err_file.write(f'Unhandled message: {args[0]}\n')
            else:
                raise Exception

# What actually runs it
client = CustomClient()
client.run(TOKEN)
