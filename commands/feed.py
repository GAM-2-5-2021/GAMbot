import discord
from discord.ext import commands

class obavijesti(commands.Cog, name="obavijesti"):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="obavijesti")
	async def obavijesti(self, ctx, thing=None):
		"""
		Automatski šalje obavijesti iz škole 
		u zadani kanal.
		
		Korištenje: "#obavijesti <on/off>"
		"""

		# ON
		if not thing:
			embed=discord.Embed(description="Obavijesti", color=0x42F56C)
			embed.set_author(name="Moraš upisati riječ!")
		elif thing.lower() in ['on','true','enable','da']:
			with open('commands/files/subscribers.txt', 'r+') as file:
				if str(ctx.channel.id) not in file.read():
					file.write(file.read() + str(ctx.channel.id)+ '\n')
					embed = discord.Embed(description=f'Obavijesti omogućene za kanal {ctx.channel.mention}', color=0x42F56C)
					embed.set_author(name='Obavijesti')
				else:
					embed = discord.Embed(description=f'Obavijesti već omogućene za kanal {ctx.channel.mention}', color=0x42F56C)
					embed.set_author(name='Obavijesti')
		# OFF
		elif thing.lower() in ['off','false','disable','ne']:
			with open('commands/files/subscribers.txt', 'r+') as file:
				temp1 = file.read()
				temp2 = ''
				if str(ctx.channel.id) in temp1:
					for line in temp1.splitlines():
						if str(ctx.channel.id) in line:
							pass
						else:
							temp2 += line + '\n'
					file.close()
					with open('commands/files/subscribers.txt', 'w') as file:
						# File se mora zatvoriti i otvoriti da bi rewrite uspio, također sprječava brisanje liste u slučaju crasha
						file.seek(0)
						file.write(temp2)
					embed = discord.Embed(description=f'Obavijesti onemogućene za kanal {ctx.channel.mention}', color=0x42F56C)
					embed.set_author(name='Obavijesti')

				else:
					embed = discord.Embed(description=f'Obavijesti već onemogućene za kanal {ctx.channel.mention}', color=0x42F56C)
					embed.set_author(name='Obavijesti')
												
		await ctx.send(embed=embed)
		
def setup(bot):
	bot.add_cog(obavijesti(bot))