2. Dodavanje komandi

GAMbot koristi cogove, tj. extensione na glavni kod, koji omogućuju odjeljivanje komandi bota u zasebne sekcije, što olakšava čitljivost i debugganje koda.

Cogovi se nalaze u folderu `/commands/`, dok se fileovi koje cogovi koriste spremaju u `/commands/files/`.

Preporučam koristiti ovaj template za cog, jer omogućava automatsko dodavanje, bez mijenjanja glavnog koda u `bot.py`

```py
import discord
from discord.ext import commands

class <ime>(commands.Cog, name="<ime>"):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command(name="<ime komande>")
	async def <ime komande>(self, ctx):
	'''
	Opis komande, za #help
	'''
		# Komanda ovdje

def setup(bot):
	bot.add_cog(<ime>(bot))
  ```

Sljedeći dio: 
[Obavijesti](https://github.com/GAM-2-5-2021/GAMbot/blob/main/Dokumentacija/obavijesti.md)
