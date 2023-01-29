import requests
import json
from weather import *
from keys import *

client = discord.Client(intents=discord.Intents.all())
command_prefix = 'w.'


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name=f'{command_prefix}[location]'))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(command_prefix):
        location = message.content.replace(command_prefix, '').lower()
        if len(location) >= 1:
            url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=imperial'
            data = json.loads(requests.get(url).content)
            data = parse_data(data)
            try:
                await message.channel.send(embed=weather_message(data, location))
            except KeyError:
                await message.channel.send(embed=error_message(location))

client.run(TOKEN)