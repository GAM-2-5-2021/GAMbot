import discord
from discord.ext import commands
import io

rjecnik = dict()
with io.open('/files/lat.txt', 'r', encoding='utf8') as file:
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
	async def lat(self, ctx, str):
		"""
		Ponavljanje za odgovaranje iz latinskog - prijevod riječi iz hrvatskog u latinski
		"""
		if not str:
			embed=discord.Embed(description="Error", color=0x42F56C)
			embed.set_author(name="Moraš upisati riječ!")
			await ctx.send(embed=embed)
		embed = discord.Embed(description=f"8{'=' * length}D", color=0x42F56C)
		embed.set_author(name=f"{member.display_name}'s Dick", icon_url=member.avatar_url)
		await ctx.send(embed=embed)
		
def setup(bot):
	bot.add_cog(lat(bot))