
from discord.ext import commands
from help import help
from music import music

bot = commands.Bot(command_prefix='+')
bot.remove_command('help')


bot.add_cog(help(bot))
bot.add_cog(music(bot))

bot.run('TOKEN')
