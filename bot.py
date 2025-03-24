import discord
from cogs.commands import Commands
from discord.ext import commands
from file_readers.json_reader import JsonReader
from file_readers.env_reader import EnvReader

# Extracts discord token from ".env" file
env_reader = EnvReader()
TOKEN = env_reader.get_discord_token()

# Extracts command prefix from "config.json"
json_reader = JsonReader()
prefix = json_reader.get_command_prefix()

# Creates intents with message content reading permission
intents = discord.Intents.default()
intents.message_content = True  

# Initializes bot with prefix and intents
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def setup_hook():
    await bot.add_cog(Commands(bot))
    print(f'Logged in as {bot.user.name}. Cog has been added.')

bot.run(TOKEN)


