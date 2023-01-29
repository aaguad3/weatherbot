import discord

key_features = {
    'temp': 'Temperature',
    'feels_like': 'Feels Like',
    'temp_min': 'Low',
    'temp_max': 'High'
}


def parse_data(data):
    data = data['main']
    del data['pressure']
    del data['humidity']
    return data


def weather_message(data, location):
    location = location.title()
    message = discord.Embed(
        title=f'{location} Weather',
        description=f'Here is the weather data for {location}.',
        color=0x4F5D73  # navyblue
    )
    for key in data:
        message.add_field(name=key_features[key], value=str(data[key]), inline=False)
    return message


def error_message(location):
    location = location.title()
    return discord.Embed(title='Error,', description=f'There was an error retrieving weather data for {location}',
                         color=0xDB2323)
