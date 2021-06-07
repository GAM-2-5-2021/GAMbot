import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True
intents.reactions = True
intents.members = True

bot = commands.Bot(command_prefix="#", intents=intents)


#nedam token
with open('token') as f:
	token = f.read()

@bot.event
async def on_ready():
	print("wassup, the bot is ready")
	await status_task()

async def status_task(): # Samo mijenja status
	await bot.change_presence(activity=discord.Game("GAMBot - #help"))
bot.remove_command("help")

@bot.event
async def on_command_completion(ctx): # Logging - ispisuje svaku aktiviranu komandu
	fullCommandName = ctx.command.qualified_name
	split = fullCommandName.split(" ")
	executedCommand = str(split[0])
	print(
		f"Executed {executedCommand} command in {ctx.guild.name} (ID: {ctx.message.guild.id}) by {ctx.message.author} (ID: {ctx.message.author.id})")

@bot.event # Automatsko handleanje čestih greški
async def on_command_error(context, error):
	if isinstance(error, commands.CommandOnCooldown):
		embed = discord.Embed(
			title="Error!",
			description="This command is on a %.2fs cool down" % error.retry_after,
			color='0xE02B2B'
		)
		await context.send(embed=embed)
	
	elif isinstance(error, commands.MissingPermissions):
		embed = discord.Embed(
			title="Error!",
			description="You are missing the permission `" + ", ".join(
				error.missing_perms) + "` to execute this command!",
			color=config["error"]
		)
		await context.send(embed=embed)
	
	raise error

if __name__ == "__main__": # Učitavanje cogova (komandi)
	for file in os.listdir("./commands"):
		if file.endswith(".py"):
			extension = file[:-3]
			try:
				bot.load_extension(f"commands.{extension}")
				print(f"Loaded extension '{extension}'")
			except Exception as e:
				exception = f"{type(e).__name__}: {e}"
				print(f"Failed to load extension {extension}\n{exception}")

bot.run(token)