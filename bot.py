# Import needed libraries:
import discord
from replit import db
from discord.utils import get
from discord.ext import commands
from time import sleep as sl
import os
import datetime
import keep_alive
import SEvent

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Variables:
prefix = 'p!'
DIRNAME = os.path.dirname(__file__)
PREFIX_PATH = os.path.join(DIRNAME, 'data', 'prefix.txt')

TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=str(prefix), case_insensitive=True, intents=intents)
client.remove_command('help')

footer = "Paradiso | Made by: athalon#8654 and Walton The Walrus#5844"

default_color = 0xd085ed

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# config

# Starts up the bot and tells me when it's ready
@client.event
async def on_ready():
    try:
        prefix_file = open(PREFIX_PATH, "r")
        client.command_prefix = prefix_file.read()
        prefix_file.close()
    except:
        pass
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"{client.command_prefix}help"))
    print('Bot is ready!')

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        embed = discord.Embed(
            #title = "Hello!",
            description = f"You can type `{client.command_prefix}help` for more info",
            color = default_color
        )
        embed.set_footer(text=footer)
        embed.set_author(name="Hello!")
        await message.channel.send(embed=embed)
    await client.process_commands(message)

@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(
        title = "Help",
        description = f"Use {prefix}help <command> for more info on a specific command.",
        color = default_color
    )
    em.add_field(name=":gear:Config:gear:", value="change_prefix, shutdown", inline=False)
    em.add_field(name=":gem:General:gem:", value="test, ping", inline=False)
    em.add_field(name=":hammer:Moderation:hammer:", value="mute, unmute, kick, ban, unban", inline=False)
    await ctx.send(embed=em)

# Changes the prefix of the bot and writes it to the prefix file
@client.command(description="Changes the prefix (Admin only)")
@commands.has_permissions(administrator=True)
async def change_prefix(ctx, new_prefix='p!'):
    try:
        try:
            prefix_file = open(PREFIX_PATH, "w")
            client.command_prefix = prefix_file.write(new_prefix)
        finally:
            prefix_file.close()
        client.command_prefix = new_prefix
        await ctx.guild.me.edit(nickf=f"Paradiso [{client.command_prefix}]")
        embed = discord.Embed(
            title = "Prefix changed",
            description = f"The prefix was changed to {prefix}",
            color = default_color
        )
        embed.set_footer(text=footer)
        await ctx.send(embed=embed)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"{prefix}help"))
        print(f'The prefix was changed to {prefix}')
    except:
        embed = discord.Embed(
            title = "Error!",
            description = f"You may not have the needed permissions to run this command!",
            color = discord.Colour.red()
        )
        embed.set_footer(text=footer)

@help.command()
async def change_prefix(ctx):
    em = discord.Embed(
        title = "Change prefix",
        description = "Changes the prefix",
        color = default_color
    )
    em.add_field(name = "**Syntax**", value=f"{prefix}change_prefix <prefix>", inline=False)
    em.add_field(name="**Required Permissions**", value="Admin", inline=False)
    em.set_footer(text=footer)
    await ctx.send(embed=em)

# Shuts the bot down
@client.command(description="Shuts the bot off (Admin only)")
@commands.has_permissions(administrator=True)
async def shutdown(ctx):
    try:
        print("Shutting down the bot...")
        embed = discord.Embed(
            title = "Shutting down...",
            description = "Shutting down the bot...\n(This might take a few seconds)\nMessage athalon#8654 to get it back up!",
            color = default_color
        )
        embed.set_footer(text=footer)
        await ctx.send(embed=embed)
        sl(1)
        await ctx.bot.logout()
        print("Goodbye! :)")
        sl(2)
    except:
        embed = discord.Embed(
            title = "Error!",
            description = "You may not have the needed permissions to run this command!",
            color = discord.Colour.red()
        )
        embed.set_footer(text=footer)
        await ctx.send(embed=embed)

@help.command()
async def shutdown(ctx):
    em = discord.Embed(
        title = "Shutdown",
        description = "Shuts the bot off",
        color = default_color
    )
    em.add_field(name = "**Syntax**", value=f"{prefix}shutdown", inline=False)
    em.add_field(name="**Required Permissions**", value="Admin", inline=False)
    em.set_footer(text=footer)
    await ctx.send(embed=em)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Commands

# General testing command
@client.command(description="General testing command")
async def test(ctx):
    embed = discord.Embed(
        title = "Test",
        description = "Test successful!",
        color = default_color
    )
    embed.set_footer(text=footer)
    await ctx.send(embed=embed)
    await ctx.send('Test successful!')

@help.command()
async def test(ctx):
    em = discord.Embed(
        title = "Test",
        description = "General testing command",
        color = default_color
    )
    em.add_field(name = "**Syntax**", value=f"{prefix}test", inline=False)
    em.add_field(name="**Required Permissions**", value="None", inline=False)
    em.set_footer(text=footer)
    await ctx.send(embed=em)

# Command to get the latency(ping) of the bot/api
@client.command(description="Displays the bot's latency(ping)")
async def ping(ctx):
    embed = discord.Embed(
        title = "Ping",
        description = f':ping_pong:Pong!\n```ini\n[{round(client.latency * 1000)}ms]\n```',
        color = default_color
    )
    embed.set_footer(text=footer)
    await ctx.send(embed=embed)

@help.command()
async def ping(ctx):
    em = discord.Embed(
        title = "Ping",
        description = "Displays the bots latency(ping)",
        color = default_color
    )
    em.add_field(name = "**Syntax**", value=f"{prefix}ping", inline=False)
    em.add_field(name="**Required Permissions**", value="None", inline=False)
    em.set_footer(text=footer)
    await ctx.send(embed=em)

@client.event
async def on_member_join(member):
    embed = discord.Embed(
        title = "Welcome!",
        description = f"Welcome {str(member)} to Paradise! We hope you have a great stay",
        color = default_color
    )
    embed.set_footer(text="Paradiso Bot | Made by: athalon#8654")
    await client.get_channel(763093985110786088).send(embed=embed)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Moderation Commands

# Mutes a member
@client.command(description="Mutes a member (Moderator only)")
@commands.has_guild_permissions(manage_roles=True)
async def mute(ctx, member : discord.Member, *, reason='Not specified'):
    if not member.bot:
        muted_role = get(ctx.message.guild.roles, name='Muted')
        await member.add_roles(muted_role, reason="Mute")
        embed = discord.Embed(
            title = "Mute",
            description = f"Muted {str(member)} for {reason}",
            color = default_color
        )
        embed.set_footer(text=footer)
        await ctx.send(embed=embed)
        embed_dm = discord.Embed(
            title = "Mute",
            description = f"You have been muted by a moderator for: {reason}\nServer: Paradise",
            color = default_color
        )
        embed_dm.set_footer(text="Paradiso Bot | Made by: athalon#8654")
        await member.send(embed=embed_dm)
    else:
        embed = discord.Embed(
            title = "Error!",
            description = f"I can't mute bots :smile:",
            color = discord.Colour.red()
        )
        embed.set_footer(text=footer)
        await ctx.send(embed=embed)
        await ctx.send("I can't mute bots :smile:")

@help.command()
async def mute(ctx):
    em = discord.Embed(
        title = "Mute",
        description = "Mutes a member",
        color = default_color
    )
    em.add_field(name = "**Syntax**", value=f"{prefix}mute <member> [reason]", inline=False)
    em.add_field(name="**Required Permissions**", value="Manage Roles", inline=False)
    em.set_footer(text=footer)
    await ctx.send(embed=em)

# Unmutes a member
@client.command(description="Unmutes a member (Moderator only)")
@commands.has_guild_permissions(manage_roles=True)
async def unmute(ctx, member : discord.Member):
    if not member.bot:
        muted_role = get(ctx.message.guild.roles, name='Muted')
        if muted_role in member.roles:
            await member.remove_roles(muted_role)
            embed = discord.Embed(
                title = "Unmute",
                description = f"Unmuted {str(member)}",
                color = default_color
            )
            embed.set_footer(text=footer)
            await ctx.send(embed=embed)
            embed_dm = discord.Embed(
                title = "Mute",
                description = f"You have been unmuted by a moderator!\nServer: Paradise",
                color = default_color
            )
            embed_dm.set_footer(text="Paradiso Bot | Made by: athalon#8654")
            await member.send(embed=embed_dm)
        else:
            embed = discord.Embed(
                title = "Error!",
                description = f"The member isn't muted",
                color = discord.Colour.red()
            )
            embed.set_footer(text=footer)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title = "Error!",
            description = f"I can't unmute bots because they can't be muted either :smile:",
            color = discord.Colour.red()
        )
        embed.set_footer(text=footer)
        await ctx.send(embed=embed)

@help.command()
async def unmute(ctx):
    em = discord.Embed(
        title = "Unmute",
        description = "Unmutes a member",
        color = default_color
    )
    em.add_field(name = "**Syntax**", value=f"{prefix}unmute <member>", inline=False)
    em.add_field(name="**Required Permissions**", value="Manage Roles", inline=False)
    em.set_footer(text=footer)
    await ctx.send(embed=em)

# Kicks a member
@client.command(description="Kicks a member (Moderator only)")
@commands.has_guild_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason="Not specified"):
    if not member.bot:
        embed = discord.Embed(
            title = "Kick",
            description = f"Kicked {str(member)} for {reason}",
            color = default_color
        )
        embed.set_footer(text=footer)
        await ctx.send(embed=embed)
        embed_dm = discord.Embed(
            title = "Kick",
            description = f"You have been kicked by a moderator for: {reason}\nServer: Paradise",
            color = default_color
        )
        embed.set_footer(text=footer)
        await member.send(embed=embed_dm)
        await member.kick(reason=reason)
    else:
        embed = discord.Embed(
            title = "Error!",
            description = "I can't kick bots :smile:",
            color = discord.Colour.red()
        )
        embed.set_footer(text=footer)
        await ctx.send(embed=embed)
        await ctx.send("I can't kick bots :smile:")

@help.command()
async def kick(ctx):
    em = discord.Embed(
        title = "Kick",
        description = "Kicks a member",
        color = default_color
    )
    em.add_field(name = "**Syntax**", value=f"{prefix}kick <member> [reason]", inline=False)
    em.add_field(name="**Required Permissions**", value="Kick members", inline=False)
    em.set_footer(text=footer)
    await ctx.send(embed=em)

# Kicks a member
@client.command(description="Bans a member (Moderator only)")
@commands.has_guild_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason="Not specified"):
    if not member.bot:
        embed = discord.Embed(
            title = "Ban",
            description = f"Banned {str(member)} for {reason}",
            color = default_color
        )
        embed.set_footer(text=footer)
        await ctx.send(embed=embed)
        embed_dm = discord.Embed(
            title = "Ban",
            description = f"You have been banned by a moderator for: {reason}\nServer: Paradise",
            color = default_color
        )
        embed.set_footer(text=footer)
        await member.send(embed=embed_dm)
        await member.ban(reason=reason)
    else:
        embed = discord.Embed(
            title = "Error!",
            description = "I can't kick bots :smile:",
            color = discord.Colour.red()
        )
        embed.set_footer(text=footer)
        await ctx.send(embed=embed)
        await ctx.send("I can't kick bots :smile:")

@help.command()
async def ban(ctx):
    em = discord.Embed(
        title = "Ban",
        description = "Bans a member",
        color = default_color
    )
    em.add_field(name = "**Syntax**", value=f"{prefix}ban <member> [reason]", inline=False)
    em.add_field(name="**Required Permissions**", value="Ban members", inline=False)
    em.set_footer(text=footer)
    await ctx.send(embed=em)

# Unbanns a user
@client.command(description="Unbans a member (Moderator only)")
@commands.has_guild_permissions(ban_members=True)
async def unban(ctx, id: int):
    try:
        user = await client.fetch_user(id)
        await ctx.guild.unban(user)
        embed = discord.Embed(
            title = "Unban",
            description = f"Unbanned {str(user)}",
            color = default_color
        )
        embed.set_footer(text=footer)
        await ctx.send(embed=embed)
    except:
        embed = discord.Embed(
            title = "Error!",
            description = "That user is not banned",
            color = discord.Colour.red()
        )
        embed.set_footer(text=footer)
        await ctx.send(embed=embed)

@help.command()
async def unban(ctx):
    em = discord.Embed(
        title = "Unban",
        description = "Unbans a member",
        color = default_color
    )
    em.add_field(name = "**Syntax**", value=f"{prefix}unban <member_id>", inline=False)
    em.add_field(name="**Required Permissions**", value="Ban Members", inline=False)
    em.set_footer(text=footer)
    await ctx.send(embed=em)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

''' Event
- _id: int PRIMARY KEY
- startTime : datetime (str)
- endTime : datetime (str)
- host : userId (int) FOREIGN KEY
- auxillaryMembers : [userId] FOREIGN KEYS
- name : string
- joinedMembers : [userId] FOREIGN KEYS
- description : string '''

@client.command()
@commands.has_role(763128748786450514) # Check if user is staff
async def create_event(ctx, name, *, description):
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel
    
    em = discord.Embed(
        title = "Please enter the starting date for the event (yyyy-mm-dd)",
        description = f"Name: {name}\nDescription: {description}\nStarting datetime: ",
        color = default_color
    )
    em.set_author(name="Event Creation")
    em.set_footer(text=footer)
    msg_embed = await ctx.send(embed=em)
    msg = await client.wait_for('message', check=check)
    year, month, day = msg.content.split('-')
    await msg.delete()
    em = discord.Embed(
        title = "Please enter the starting time for the event (hh:mm)",
        description = f"Name: {name}\nDescription: {description}\nStarting datetime: ",
        color = default_color
    )
    em.set_author(name="Event Creation")
    em.set_footer(text=footer)
    await msg_embed.edit(embed = em)
    msg = await client.wait_for('message', check=check)
    hours, minutes = msg.content.split(':')
    
    startTime = datetime.datetime(int(year), int(month), int(day), int(hours), int(minutes))
    startTime = startTime.strftime("%m-%d-%Y %H:%M:%S")

    em = discord.Embed(
        title = "Please enter the ending date for the event (yyyy-mm-dd)",
        description = f"Name: {name}\nDescription: {description}\nStarting datetime: {startTime}\nEnding datetime: ",
        color = default_color
    )
    em.set_author(name="Event Creation")
    em.set_footer(text=footer)
    msg_embed = await ctx.send(embed=em)
    msg = await client.wait_for('message', check=check)
    year, month, day = msg.content.split('-')
    await msg.delete()
    em = discord.Embed(
        title = "Please enter the ending time for the event (hh:mm)",
        description = f"Name: {name}\nDescription: {description}\nStarting datetime: {startTime}\nEnding datetime: ",
        color = default_color
    )
    em.set_author(name="Event Creation")
    em.set_footer(text=footer)
    await msg_embed.edit(embed = em)
    msg = await client.wait_for('message', check=check)
    hours, minutes = msg.content.split(':')
    await msg.delete()
    
    endTime = datetime.datetime(int(year), int(month), int(day), int(hours), int(minutes))
    endTime = endTime.strftime("%m-%d-%Y %H:%M:%S")

    em = discord.Embed(
        title = "Setup complete!",
        description = f"Name: {name}\nDescription: {description}\nStarting datetime: {startTime}\nEnding datetime: {endTime}\nHost: {ctx.message.author.mention}",
        color = default_color
    )
    em.set_author(name="Event Creation")
    em.set_footer(text=footer)
    await msg_embed.edit(embed = em)
    event = SEvent.SEvent(startTime, endTime, ctx.message.author.id, name, db, ctx.message.mentions, [], description)
    event.updateDBEntry()

@client.command()
@commands.has_role(808424137357787136) # Check if user is Bot dev
async def db_dump(ctx):
    msg = ""
    for key in db.keys():
        msg += f"{key} : {db[key]}\n"
    await ctx.send(msg)

def isFloat(key):
    try:
        float(key)
        return True
    except ValueError:
        return False

def get_event(key):
    if isFloat(key): return SEvent.SEvent.getEventFromDBById(db, float(key))
    else: return SEvent.SEvent.getEventFromDBByName(db, key)

@client.command()
async def event(ctx, key):
    event_obj = get_event(key)
    host = client.get_user(event_obj.host)
    auxMembers = ""
    for member in event_obj.auxillaryMembers:
        auxMembers += str(client.get_user(member)) + ','
    em = discord.Embed(
        title = "Event Details",
        description = f"""Name: {event_obj.name}
        Description: {event_obj.description}
        Host: {host}
        Auxillary Members: {auxMembers}
        Joined Members: {len(event_obj.joinedMembers)}
        Starting datetime: {event_obj.startTime}
        Ending datetime: {event_obj.endTime}
        ID: {event_obj._id}""",
        color = default_color
    )
    em.set_footer(text=footer)
    await ctx.send(embed=em)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Running and hosting

# Sends a ping to the repl.it server so that it doesn't get taken down
keep_alive.keep_alive()

# Runs the bot by its token
client.run(TOKEN)
