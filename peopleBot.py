# Work with Python 3.6
import discord
import urllib.request as req
import random
import asyncio

TOKEN = 'NTUwNTAyNjgwNTM2MDIzMDQx.D1jiQQ.Y9f_MmsbsZcP8cdSVEaw18CFPyo'
blakes = open("blake.txt", "r")
proverbs = blakes.read().split('^')
blakes.close()

client = discord.Client()

# Awaits commands and executes accordingly
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    # If person is sent
    if message.content.startswith('!person'):

        # Old code from when it sent TPDNE images.
        """ msg = 'Generating image...'.format(message)
        await client.send_message(message.channel, msg)
        imgurl ="https://thispersondoesnotexist.com/image"
        res = req.urlopen(imgurl)  # Download TPDNE image
        output = open("image.jpg","wb")
        output.write(res.read())
        output.close()
        with open('image.jpg', 'rb') as f:
            msg = 'This person does not exist: '.format(message)
            await client.send_message(message.channel, msg)
            await client.send_file(message.channel, f) 
        """

        # Old code from when it was presumed dead.
        #msg = "Farewell to thee, farewell to thee \nThou charming one who dwells in shaded bowers \nOne fond embrace ere I depart \nUntil we meet again." 
        
        msg = random.choice(proverbs)
        await client.send_message(message.channel, msg)
        await asyncio.sleep(2)
        await client.send_message(message.channel, "So it is written.")
    
    # Waits for '!friend' to resolve conflicts
    elif message.content.startswith('!friend'):
        youtube_url = 'https://www.youtube.com/watch?v=htcvoz8x_qY'
        channel = message.author.voice.voice_channel
        voice = await client.join_voice_channel(channel)
        player = await voice.create_ytdl_player(youtube_url)
        player.start()
        await asyncio.sleep(227) # Will leave when the entire song is finished 
        await voice.disconnect()

    # Allows for early conflict resolution
    elif message.content.startswith('!resolved'):
        for x in client.voice_clients:
            return await x.disconnect()

# Respond to small brain reaction.
@client.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    emoji = reaction.emoji
    author = reaction.message.author
    if isinstance(emoji, discord.Emoji):
        name = emoji.name
    elif isinstance(emoji, str):
        name = emoji
    else:
        raise ValueError("Unknown emoji of type:", type(emoji))

    if author == client.user and name == "20":
        await client.send_message(channel, "There is nothing more small brained than small braining a machine, you coward.")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    





client.run(TOKEN)
