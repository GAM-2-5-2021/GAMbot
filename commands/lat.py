import discord
from discord.ext import commands

rjecnik = dict()
with open('commands/files/lat.txt', 'r', encoding='utf8') as file:
	for line in file.read().splitlines():
		p1, p2 = line.split('$')
		if ',' in p1:
			p1 = [x.strip() for x in p1.split(',')]
		else:
			p1 = [p1]
		for i in p1:
			rjecnik[i] = rjecnik.get(i,'') + p2 + '\n'

class lat(commands.Cog, name="lat"):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="lat")
	async def lat(self, ctx, str=None):
		"""
		Ponavljanje za odgovaranje iz latinskog - prijevod riječi iz hrvatskog u latinski
		"""
		if not str:
			embed=discord.Embed(description="Error", color=0x42F56C)
			embed.set_author(name="Moraš upisati riječ!")
			await ctx.send(embed=embed)
		else:
			embed = discord.Embed(description=rjecnik.get(str.lower(), 'Riječ nije pronađena'), color=0x42F56C)
			embed.set_author(name=str.title())
			await ctx.send(embed=embed)
		
def setup(bot):
	bot.add_cog(lat(bot))