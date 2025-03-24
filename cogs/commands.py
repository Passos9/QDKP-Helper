from discord.ext import commands
from service import Service

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.service = Service()

    @commands.command(name='roster')
    async def roster(self, ctx):
        print("Roster command invoked")
        
        response = self.service.get_player_dkp()

        if isinstance(response, str): # An error occurred
            await ctx.send(f"❌ {response}")

        else: 
            await ctx.send(str(response))

        
    @commands.command(name='loot')
    async def loot(self, ctx, raid: str = None, date: str = None):
        print("Loot command invoked")

        response = self.service.get_player_loot(raid, date)

        if isinstance(response, str): # An error occurred
            await ctx.send(f"❌ {response}")

        else: 
            await ctx.send(str(response))
            

async def setup(bot):
    await bot.add_cog(Commands(bot))