from time import sleep

import discord
import sys

from src.main.python.roll.roll_util import parse_roll, get_roll_results

bot = discord.Client()
ready = False
token = None

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content
    if content.startswith('!activate'):
        bot.send_message(message.channel, "I am alive!")
    if content.startswith('!help'):
        __show_help(message.channel)
        player = message.author
        words = content.split(' ')
        # timeframe = parse_timeframe(words)
        # if(reminder_dao.add_reminder(player.id, player.name, int(words[1]))):
        await bot.send_message(message.channel, "Added a reminder for you, <@" + str(player.id) + ">.")
        # else:
        #     bot.send_message(message.channel, "I already a reminder for you at this time")
    if content.startswith('!roll'):
        parse_roll(message.content)
        await bot.send_message(message.channel, get_roll_results())


def __show_help(channel):
    bot.send_message(channel, "")



async def send_message_to_channel(message, text):
    await bot.wait_until_ready()
    bot.send_message(message.channel, text)
#
# async def send_reminder_direct_message():
#     await bot.wait_until_ready()
#     bot.send_message(person, text)


if __name__ == '__main__':
    args = sys.argv
    token = args[1]

    bot.run(token)