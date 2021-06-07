3. Obavijesti

Obavijesti su najkompleksniji dio koda, zato ću ih u ovom dijelu dokumentacije bolje objasniti.

Način na koji se obavijesti dohvaćaju je preko RSS feeda stranice http://www.gimnazija-amohorovicica-ri.skole.hr/, koji se može pronaći na linku http://www.gimnazija-amohorovicica-ri.skole.hr/rss/rssfeeder.php?rss_kid=1&rss_ct=news&rss_uid=1

Ovaj način je puno lakši i brži od ikakvog parseanja htmla stranice. 

Koristim package `feedparser` za automatsko dohvaćanje tog RSS feeda, te zatim preko alata `datetime` i `dateutil` izvlačim datume objave. Pomoću datuma i vremena objave, i globalne varijable `timer_stuff`, odvajam sve obavijesti objavljene u zadnjih 20min, i jednu po jednu ih šaljem u subscribeane kanale. Kanali su spremljeni u fileu [`subscribers.txt`](https://github.com/GAM-2-5-2021/GAMbot/blob/main/commands/files/subscribers.txt), a održavanje filea obavlja cog `feed.py`.

Automatsko slanje obavijesti se obavlja pomoću [discord.py taskova](https://discordpy.readthedocs.io/en/stable/ext/tasks/index.html), a kod se nalazi u cogu `rss.py`

**Kraj dokumentacije**