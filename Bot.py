import time
import discord
from discord.ext import commands, tasks
from discord.ext.tasks import loop
import asyncio
import sys
import random
check = 0
prefix = "."
sign = False

client = commands.Bot(command_prefix = '.')


@client.event
async def on_ready():
    global prefix
    global logchannel
    global startlogchannelid
    print("--------")
    print("Init Started...")
    print("--------")
    logchannel = client.get_channel(571239829715550208)
    startlogchannelid = 571239829715550208
    embed = discord.Embed(title="System Startup", color=0x00ff00)
    embed.add_field(name="System Startup", value="**System Ready**", inline=False)
    await logchannel.send(embed=embed)
    await client.change_presence(status = discord.Status.online, activity = discord.Game("My Prefix is ."))
    print("--------")
    print(f"Logged in as: {client.user.name}")
    print(f"User ID: {client.user.id}")
    print("--------")
    print("--------")
    print("Bot Ready")
    print("--------")
    print("--------")
    print(f"Starting Prefix set to {client.command_prefix}")
    print("--------")
    print("--------")
    print(f"Starting Log Channel set to #{logchannel}")
    print(f"Starting Log Channel ID: {startlogchannelid}")
    print("--------")


@client.event
async def on_message(message):
    if "<@!710853558828007447>" in message.content:
        channel = message.channel
        embed = discord.Embed(title="You @tted me!", color=0x00ff00)
        embed.add_field(name="Prefix", value=f"My Prefix is `{client.command_prefix}`", inline=False)
        embed.add_field(name="Help", value=f"My Help command is `{client.command_prefix}welp`", inline=False)
        await channel.send(embed=embed)
    await client.process_commands(message)

@client.event
async def on_command_error(ctx, error):
    global logchannel
    username = ctx.message.author.name
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title="Error", color=0xff0000)
        embed.add_field(name="Command Error", value="Command Not Found", inline=False)
        await ctx.send(embed=embed)
        embed = discord.Embed(title="Error", color=0xff0000)
        embed.add_field(name="Command Error", value="Command Not Found", inline=False)
        embed.add_field(name="Trigger", value=f"Username: {ctx.author}\nUser ID: {ctx.author.id}\nMessage / Command: {ctx.message.content}", inline=False)
        await logchannel.send(embed=embed)
    else:
        embed = discord.Embed(title="Error", color=0xff0000)
        embed.add_field(name="Error", value=error, inline=False)
        await ctx.send(embed=embed)

@client.command()
@commands.has_any_role('Staff Team')
async def announce(ctx, channel :discord.TextChannel, *, txt):
    global logchannel
    embed = discord.Embed(title="", color=0x00ff00)
    embed.add_field(name="Announcement", value=txt, inline=False)
    await channel.send(embed=embed)
    embed = discord.Embed(title="", color=0x00ff00)
    embed.add_field(name="Announcement", value=txt, inline=False)
    embed.add_field(name="Trigger", value=f"Username: {ctx.author}\nUser ID: {ctx.author.id}", inline=False)
    await logchannel.send(embed=embed)

@announce.error
async def announce_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="Error", color=0xff0000)
        embed.add_field(name="Error", value="Missing Argument(s)", inline=False)
        embed.add_field(name="Example", value=f"You would do: {client.command_prefix}announce <channel> <message>", inline=False)
        await ctx.send(embed=embed)
    else:
        print(error)

@client.command()
async def welp(ctx):
    embed = discord.Embed(title="Help", color=0x00ff00)
    embed.add_field(name="Prefix", value=f"The current prefix is `{client.command_prefix}`", inline=False)
    embed.add_field(name="Command List", value="**welp** - Shows this Message\n**source** - Shows you a link to the **AWESOME** code that runs me\n**logchannel** - Shows you the current Log Channel and allows you to change it\n**announce** - Allows you to use the bot to say something in any channel it is allowed to write messages in\n**prefix** - Used to change the bot's prefix\n**rules** - Used to show the channel for the Towny Guide\n**version** - Used to show the UI and Code Versions of the bot\n**ping** - Used to show the bot's ping\n**poll** - Used to create a poll in any channel\n**reset_status** - Used to set a custom status for the bot\n**purge** - Used to mass delete messages\n**ban** - Used to ban a user\n**unban** - Used to unban a user\n**kick** - Used to kick a user\n**exit** - used to shut down the bot (only Developer and Coddo#3210 can do so)", inline=False)
    await ctx.send(embed=embed)

@client.command()
@commands.has_any_role('Staff Team')
async def poll(ctx, channel:discord.TextChannel, *,args):
    embed = discord.Embed(title=f"Poll created by {ctx.author.name}", colour=0x00ff00)
    embed.add_field(name="Poll", value=f"**{args}**")
    embed.set_footer(text="React to vote!", )
    msg = await channel.send(embed=embed)
    await msg.add_reaction("👍")
    await msg.add_reaction("👎")

@poll.error
async def poll_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="Error", color=0xff0000)
        embed.add_field(name="Error", value="Missing Argument(s)", inline=False)
        embed.add_field(name="Example", value=f"You would do: {client.command_prefix}poll <channel> <message>", inline=False)
        await ctx.send(embed=embed)

@client.command()
@commands.has_any_role('Developer', 'Owner', 'BOTBOIS')
async def prefix(ctx, arg = "."):
    global prefix 
    global check
    check = 1
    prefix = arg
    embed = discord.Embed(title="Prefix", color=0x00ff00)
    embed.add_field(name="Prefix Changing", value=f"To change the prefix do: {client.command_prefix}confirmprefix", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def version(ctx):
    global logchannel
    embed = discord.Embed(title="Version", color=0x00ff00)
    embed.add_field(name="Version:", value="Current Version: **1.3** (BETA)", inline=False)
    embed.add_field(name="UI Version:", value="Current Version: **1.0**", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def rules(ctx):
    embed = discord.Embed(title="Rules", color=0x00ff00)
    embed.add_field(name="Towny Rules", value="Read the <#684407732853538828>", inline=False)
    await ctx.send(embed=embed)

@client.command()
@commands.has_any_role('Developer', 'Owner', 'BOTBOIS')
async def confirmprefix(ctx):
    global prefix 
    global check
    global logchannel
    if check == 1:
        client.command_prefix = prefix
        await client.change_presence(status = discord.Status.online, activity = discord.Game(f"My Prefix is {prefix}"))
        embed = discord.Embed(title="Prefix Changed", color=0x00ff00)
        embed.add_field(name="Prefix Change", value=f"Prefix Changed to {prefix}", inline=False)
        embed.add_field(name="Status Change", value=f"Status Reset to: ```My Prefix is {client.command_prefix}```", inline=False)
        await ctx.send(embed=embed)
        await logchannel.send(embed=embed)
        check = 0
    else:
        await ctx.send(f"Try using {client.command_prefix}<the prefix you want to change to> first!")

@client.command()
@commands.has_any_role('Developer', 'Owner', 'BOTBOIS')
async def reset_status(ctx, *, arg = "My Prefix is ."):
    global logchannel
    await client.change_presence(status = discord.Status.online, activity = discord.Game(arg))
    embed = discord.Embed(title="Status Reset", color=0x00ff00)
    embed.add_field(name="Status Reset", value="Status Reset to **{arg}**", inline=False)
    await ctx.send(embed=embed)
    await logchannel.send(embed=embed)
    await ctx.send(f"Status Reset to ```{arg}```")

@client.command()
async def ping(ctx):
    latency = round(client.latency, 2)
    await ctx.send(f'Pong! `{latency}ms`')

@client.command()
@commands.has_any_role('Staff Team')
async def purge(ctx, amount = 10):
    await ctx.channel.purge(limit = amount)

@client.command()
@commands.has_any_role('Developer', 'Owner', 'Admin')
async def kick(ctx, member : discord.Member, *, reason=None):
    print("Kick Command Activated")
    await member.kick(reason=reason)

@client.command()
@commands.has_any_role('Developer', 'Owner', 'Admin')
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

@client.command()
@commands.has_any_role('Developer', 'Owner', 'Admin')
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

@client.command()
async def source(ctx):
    embed = discord.Embed(title="Source", color=0x00ff00)
    embed.add_field(name="Source", value="**My code is open source, you can see it at https://github.com/Coddo-Python/TPNET-Server-Discord-Bot**", inline=False)
    await ctx.send(embed=embed)

@client.command()
@commands.has_any_role('Developer', 'Owner', 'BOTBOIS')
async def logchannel(ctx, channel:discord.TextChannel = 5):
    global logchannelcheck
    global startlogchannelid
    global lid
    if channel == 5:
        embed = discord.Embed(title="Log Channel", color=0x00ff00)
        embed.add_field(name="Log Channel", value=f"The Current Log Channel is <#{startlogchannelid}>", inline=False)
        embed.add_field(name="Log Channel Changing", value=f"To Change the Log Channel do {client.command_prefix}logchannel <channel>", inline=False)
        await ctx.send(embed=embed)
    else:
        lid = channel.id
        logchannelcheck = 1
        embed = discord.Embed(title="Log Channel Change", color=0x00ff00)
        embed.add_field(name="Log Channel Change", value=f"**Are you sure?**\nTo confirm so, please do {client.command_prefix}confirmlogchannel\nYou will have unlimited time to do so!", inline=False)
        await ctx.send(embed=embed)

@client.command()
@commands.has_any_role('Developer', 'Owner', 'BOTBOIS')
async def confirmlogchannel(ctx):
    global logchannel
    global logchannelcheck
    logchannelcheck = 0
    logchannel = client.get_channel(lid)
    embed = discord.Embed(title="Log Channel Change", color=0x00ff00)
    embed.add_field(name="Log Channel Change", value=f"Log Channel changed to <#{lid}>", inline=False)
    await ctx.send(embed=embed)
    embed = discord.Embed(title="Log Channel Change", color=0x00ff00)
    embed.add_field(name="Log Channel Change", value=f"This is My New Log Channel!", inline=False)
    await logchannel.send(embed=embed)

@client.command()
@commands.has_any_role('Developer', 'Owner', 'BOTBOIS')
async def exit(ctx):
    embed = discord.Embed(title="Force Stop", color=0xff0000)
    embed.add_field(name="Shut Down", value="**System Shutting Down**", inline=False)
    await ctx.send(embed=embed)
    await logchannel.send(embed=embed)
    await client.logout()


client.run('TOKEN')