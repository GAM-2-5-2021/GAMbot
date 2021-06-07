import feedparser
import threading
import time
from datetime import timedelta, datetime
from dateutil import parser as timeparser

import discord
from discord.ext import commands
from discord.ext import tasks

timer_stuff = time.time()
# Vrijeme slanja prve komande (default o)


class rss(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.rss_event.start()
	@tasks.loop(minutes=20) # Timer, svakih 20min dohvaća feed
	async def rss_event(self):
		await self.bot.wait_until_ready()
		print('Provjeravam nove članke')
		print(f'vrijeme: {datetime.utcnow()}')
		feed = feedparser.parse('http://www.gimnazija-amohorovicica-ri.skole.hr/rss/rssfeeder.php?rss_kid=1&rss_ct=news&rss_uid=1')
		newstuff = 0 # Samo za logging
		for entry in feed.entries:
			datum1 = timeparser.parse(entry.published)
			datum1 = (datum1 - timedelta(hours=2)).replace(tzinfo=None) # Rješava problem vremenskih zona tako da sve prebaci u UTC
			now_date = datetime.utcnow()

			zadnjih20min = now_date - datum1 < timedelta(minutes=20) # Boolean; ako je članak objavljen u zadnjih 20min
			if zadnjih20min:
				print(entry.title) #
				print(entry.link)  # logging
				embed = discord.Embed(description=f'Nova objava na stranici škole\n{entry.link}', color=0x42F56C)
				embed.set_author(name='| ' + entry.title)
				with open('commands/files/subscribers.txt', 'r') as file:
					channels = file.read().splitlines()
				for channel in channels:
					if channel:
						channel = self.bot.get_channel(int(channel))
						await channel.send(embed=embed)
				newstuff += 1
		if newstuff:
			print(f'Učitanih članaka: {newstuff}')
		else:
			print('Nema novih članaka u feedu')

	@commands.command(name="testrss")
	async def testrss(self, ctx):
		'''
		Dohvaća najnoviju obavijest iz škole
		'''
		await self.bot.wait_until_ready()
		print('Provjeravam nove članke')
		print(f'vrijeme: {datetime.utcnow()}')
		feed = feedparser.parse('http://www.gimnazija-amohorovicica-ri.skole.hr/rss/rssfeeder.php?rss_kid=1&rss_ct=news&rss_uid=1')
		newstuff = 0
		entry = feed.entries[0]
		embed = discord.Embed(description=f'Nova objava na stranici škole\n{entry.link}', color=0x42F56C)
		embed.set_author(name='| ' + entry.title)
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(rss(bot))
