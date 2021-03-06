# Import needed libraries:
from attr import __description__
import discord
from discord.utils import get
from discord.ext import commands
from time import sleep as sl
import os
import keep_alive

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
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"{client.command_prefix}help                                 also, type p!sex ;)"))
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

@client.command()
async def sex(ctx):
    nick_user = await client.fetch_user(458078088069251072)
    em = discord.Embed(
        title = "Sex!",
        description = f"{ctx.author.mention} has requested violent gay sex with {nick_user.mention}",
        color = default_color
    )
    em.set_footer(text=footer)
    await ctx.send(nick_user.mention, embed = em)

@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(
        title = "Help",
        description = f"Use {prefix}help <command> for more info on a specific command.",
        color = default_color
    )
    em.add_field(name=":gear:Config:gear:", value="change_prefix, shutdown", inline=False)
    em.add_field(name=":gem:General:gem:", value="test, ping, sex", inline=False)
    em.add_field(name=":hammer:Moderation:hammer:", value="mute, unmute, kick, ban, unban", inline=False)
    await ctx.send(embed=em)

@help.command()
async def sex(ctx):
    em = discord.Embed(
        title = "Sex",
        description = "See for yourself ;)",
        color = default_color
    )
    em.add_field(name="Syntax", value=f"{prefix}sex", inline=False)
    em.add_field(name="Required Permissions", value="None", inline=False)
    em.set_footer(text=footer)
    await ctx.send(embed=em)

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

@help.command()
async def server(ctx):
    em = discord.Embed(
        title = "Server",
        description = "Displays the server invite",
        color = default_color
    )
    em.add_field(name = "**Syntax**", value=f"{prefix}server", inline=False)
    em.add_field(name="**Required Permissions**", value="None", inline=False)
    em.set_footer(text=footer)
    await ctx.send(embed=em)

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

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Running and hosting

# Sends a ping to the repl.it server so that it doesn't get taken down
keep_alive.keep_alive()

# Runs the bot by its token
client.run(TOKEN)
