import discord
from discord import app_commands
from discord.ext import commands

import feedparser

from const import labowor


class RSSCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        print("Loaded", __class__.__name__)
        

    # rss feedparse for twokinds
    @app_commands.command(name="twokinds", description="Sends latest TwoKinds page")
    async def twokinds(self, interaction: discord.Interaction):
        tkfeed = feedparser.parse("https://twokinds.keenspot.com/feed.xml")
        newpagelink = tkfeed.entries[0]["links"][0]["href"]
        await interaction.response.send_message(newpagelink)



async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(RSSCog(bot), guild=labowor)
