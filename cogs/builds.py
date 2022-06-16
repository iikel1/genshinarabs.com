import discord
from discord.ext import commands
import random
import pymongo

mongo = 'mongodb+srv://HMusic:ylmdDpyjyCv4XzMr@hutao.14vgh.mongodb.net/Hutao?retryWrites=true&w=majority'
myclient = pymongo.MongoClient(mongo)
mydb = myclient["commands"]
mycol = mydb["builds"]


class builds(commands.Cog):
    def __init__(self, client):

        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message : discord.Message):
        if not message.author.bot :
            if message.content[0] == '"':
                cmd = message.content[1:]
                pass

async def setup(client): 
    await client.add_cog(builds(client)) 