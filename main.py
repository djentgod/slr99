import os

from discord.ext import commands

# import all the cogs
from help import help
from music import music

bot = commands.Bot(command_prefix='+')

# remove the default help command so that we can write out own
bot.remove_command('help')

# register the class with the bot
bot.add_cog(help(bot))
bot.add_cog(music(bot))

# start the bot with our token
bot.run('OTg4ODIxMDI2NDA4Mzc0MzIz.GsmJFP.QlC8QXt-8wZtI6vCtUDQq7xnNaTmqsSDE5idMM')
