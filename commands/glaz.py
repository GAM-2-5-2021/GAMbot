import discord
from discord.ext import commands

rjecnik = dict()
with open('commands/files/glaz.txt', 'r', encoding='utf8') as file:
	temp = file.read().splitlines()
	for i, line in enumerate(temp):
		if line.startswith('$'):
			x = '\n'
			y = ''
			j = 1
			while x != '':
				y += x + '\n'
				x = temp[i+j]
				j += 1
			rjecnik[line[1:]] = y

class glaz(commands.Cog, name='glaz'):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name='glaz')
	async def glaz(self, ctx, str=None):
		"""
		Ponavljanje za odgovaranje iz glazbenog - ispisuje natuknice za uneseno razdoblje
		"""
		if not str:
			embed=discord.Embed(description='Moraš upisati riječ', color=0x8B0000)
			embed.set_author(name='Greška!')
			await ctx.send(embed=embed)
		else:
			if rjecnik.get(str.lower(), ''):
				embed = discord.Embed(description='\n'.join(rjecnik.get(str.lower()).split('\n')[3:]), color=0x000089)
				embed.set_author(name=rjecnik.get(str.lower()).split('\n')[2])
				await ctx.send(embed=embed)
			else: 
				embed = discord.Embed(description='Razdoblje nije pronađeno', color=0x8B0000)
				embed.set_author(name='Greška')
				await ctx.send(embed=embed)
				
		
def setup(bot):
	bot.add_cog(glaz(bot))