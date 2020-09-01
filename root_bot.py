#!/usr/bin/python

import discord
from discord.ext import tasks, commands


client = commands.Bot(command_prefix = '')


token = ''

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('with Complier'))
    print("Bot is ready.")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid Command used.')

@client.command(brief="Say hello")
async def hello(ctx):
    await ctx.send('Hello World')

@client.command(brief="To ask Who are you?")
async def sudo_w(ctx):
    await ctx.send('I am root')

@client.command(brief="Say Hi to Bot")
async def hi(ctx):
    await ctx.send('Hi dude')

@client.command(brief="Asking How are you")
async def how_are_you(ctx):
    await ctx.send('I am find thank you , How about you')

@client.command(brief="Caring")
async def care(ctx):
    await ctx.send('Thank You, you too. Stay at Home , Wash your hand and take care, alway wear mask to go outside')

@client.command(brief="Clear Message with sudo power")
async def sudo_clear(ctx,amount : int):
    await ctx.channel.purge(limit=amount)


@sudo_clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify an mount of messages to delect')


@client.command(pass_context=True, brief="whoami")
async def sudo_whoami(ctx):
   whoami = ctx.message.author
   await ctx.send(whoami)

@client.command(pass_context=True, brief="ls")
async def sudo_ls(ctx):
   list = server.Server.members
   ls = ctx.message.author
   await ctx.send(ls)

@client.command(brief="kick user with sudo power")
async def sudo_kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command(brief="ban user with sudo power")
async def sudo_ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

@client.command(pass_context=True, brief="HeeHee")
async def sudo_fuck(ctx):
    fuck = 'You'
    await ctx.send(fuck)

client.run(token)

