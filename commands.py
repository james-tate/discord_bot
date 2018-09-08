import discord
from discord.ext import commands
import datetime

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def time(ctx):
    time = datetime.datetime.now() - datetime.timedelta(hours=5)
    await ctx.send("Date: " + str(time))

@bot.command()
async def back(ctx):
    await ctx.send("https://media.giphy.com/media/l0ExuiqMllbZywd8s/giphy.gif")

@bot.command()
async def nowork(ctx):
    await ctx.send("https://goo.gl/G5Lkq2")

@bot.command()
async def hi(ctx):
    await ctx.send(":smiley: :wave: Hello, there " + "{0.author.mention} !".format(ctx.message))

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="lunch_bot_beep_boop", description="I bring Tacos to the masses!", color=0xeee657)
    # give info about you here
    embed.add_field(name="Author", value="@realJamesTate")
   
    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="good bot", description="List of commands are:", color=0xeee657)

    embed.add_field(name="!makepoll", value="Creates new poll (in testing)", inline=False)
    embed.add_field(name="!link", value="Gives link to polls", inline=False)
    embed.add_field(name="!hi", value="Hello", inline=False)
    embed.add_field(name="!cat", value="Everyone likes cats!", inline=False)
    embed.add_field(name="!info", value="Gives info about me", inline=False)
    embed.add_field(name="!help", value="Gives this message", inline=False)
    embed.add_field(name="!list", value="List this weeks poll choices", inline=False)
    embed.add_field(name="!vote {choice}", value="allows you to vote right here (not working)", inline=False)
    embed.add_field(name="!add {choice}", value="add a choice to the poll this week", inline=False)
    embed.add_field(name="!time", value="time", inline=False)

    await ctx.send(embed=embed)


