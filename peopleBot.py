# Work with Python 3.6
import discord
import urllib.request as req
import random
import asyncio

TOKEN = 'NTUwNTAyNjgwNTM2MDIzMDQx.D1jiQQ.Y9f_MmsbsZcP8cdSVEaw18CFPyo'
blakes = open("blake.txt", "r")
proverbs = blakes.read().split('^')
blakes.close()
mentions = dict()
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
        """msg = "Farewell to thee, farewell to thee \nThou charming one who dwells in shaded bowers \nOne fond embrace ere I depart \nUntil we meet again." """
        
        msg = random.choice(proverbs)
        await client.send_message(message.channel, msg)
        await asyncio.sleep(2)
        await client.send_message(message.channel, "So it is written.")
    
    # Waits for '!friend' to resolve conflicts
    elif message.content.startswith('!friend'):
        try:
            youtube_url = 'https://www.youtube.com/watch?v=htcvoz8x_qY'
            channel = message.author.voice.voice_channel
            voice = await client.join_voice_channel(channel)
            player = voice.create_ffmpeg_player('friends.mp3', after=lambda: print('Song done'))
            player.start()
            while not player.is_done():
                await asyncio.sleep(1) # Will leave when the entire song is finished 
            player.stop()
            await voice.disconnect()
        except:
            await client.send_message(message.channel, "Must be in a voice channel to resolve conflicts.")

    # Allows for early conflict resolution
    elif message.content.startswith('!resolved'):
        for x in client.voice_clients:
            return await x.disconnect()

    elif message.content.startswith('@'):
        content = message.content[1:]
        content = content.split(' ', 1)
        if content[0] in mentions.keys():
            people = mentions.get(content[0])
            print(people)
            await client.send_message(message.channel, content[0] + " invoked.")
            final_mention = ""
            for person in people:
                person = person.split("#")
                print(person)
                user = discord.utils.get(message.server.members, name = person[0], discriminator = person[1])
                final_mention += user.mention + " "
            try:
                final_mention += "\n" + content[1]
            except:
                pass
            await client.send_message(message.channel, final_mention)

    elif message.content.startswith('!add'):
        await client.send_message(message.channel, "Creating new mention...")
        content = message.content[5:]
        content = content.split(" ", 1)
        mention = content[0]
        names = content[1].split("/")
        final_string = mention + ";"
        valid_names = True
        print(mention)
        print(names)
        for x in names:
            print(x)
            if not x[-5] == "#":
                await client.send_message(message.channel, "Invalid username: " + x)
                valid_names = False
            else:
                final_string += x + ","
        if valid_names:
            final_string = final_string.rstrip(",")
            fp = open("mentions.txt", "a")
            fp.write(final_string)
            fp.close
            mentions[mention] = names
            await client.send_message(message.channel, "Successfully created @" + mention)
        else:
            await client.send_message(message.channel, "Unable to create new mention")
 
    elif message.content.startswith('!mentions'):
        final = "Current custom mentions:\n"
        for mention, namesList in mentions.items():
            names = ''
            for x in namesList:
                names += x + ", "
            names = names.rstrip(",")
            final += "@" + mention + ": " + names + "\n" 
        await client.send_message(message.channel, final)

    elif message.content.startswith('!botHelp') or message.content.startswith('!bothelp'):
        final = """personBot is watching.
    !person - Will return a random poem written by English poet William Blake (1757-1827).
    !friend - Deploys emergency conflict resolution procedure. You must be in a voice channel for proper execution.
    !resolved - Ends emergency conflict resolution procedure. Procedure must already be in effect.
    @[custom] - Will execute the custom mention. You can write a message after the tag like normal, or leave no message.
    !add - Create a new custom mention. Command must be in the following format:

    '!add mentionName UserA#1234/UserB#1234/UserC#1234'"""
        await client.send_message(message.channel, final)

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
    fp = open("mentions.txt", "r")
    for x in fp:
        x = x.rstrip("\n")
        x = x.split(';')
        mentions[x[0]] = x[1].split(",")
    fp.close()



client.run(TOKEN)
