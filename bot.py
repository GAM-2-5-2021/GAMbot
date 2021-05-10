import discord
from discord.ext import commands
client = commands.Bot(command_prefix="#")

with open('token') as f:
	token = f.read()

@client.event
async def on_ready():
	print("wassup, the bot is ready")


@client.command()
async def ping(ctx):
	await ctx.message.channel.send(f'Pong! {round(client.latency, 1)}ms')

client.run(token)