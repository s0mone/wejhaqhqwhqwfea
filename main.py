import discord
import asyncio
import aiohttp

client = discord.Client(intents=discord.Intents.all())

update_log = "added nukes & deadly disasters"

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content == "!server":
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.mcsrvstat.us/2/168.119.146.57:26505") as resp:
                data = await resp.json()

        if data["online"]:
            version = data["version"]
            ip = data["ip"]

            embed = discord.Embed(title="The server is online", color=0x00FF00)
            embed.add_field(name="IP", value=ip)
            embed.add_field(name="Port", value="26505")
            embed.add_field(name="Version", value=version)
            embed.add_field(name="Latest update", value=update_log)
            
            await message.channel.send(f"{message.author.mention}, if you have any problems joining please open a ticket we will try to help you")
          
            await message.channel.send(embed=embed)
        else:
            await message.channel.send("wait what.. why is the server offline.... @ERR404 go fix it tf you doin man")
          
client.run('MTA1OTQwODM4MjMzNjk1ODUzNA.Gu9HDa.BM4So83Zl0Y4k6RkJ4dHijx1yp0CTCiI5cQUMk')
