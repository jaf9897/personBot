# Work with Python 3.6
import discord
import urllib.request as req
                                            
TOKEN = 'NTUwNTAyNjgwNTM2MDIzMDQx.D1jiQQ.Y9f_MmsbsZcP8cdSVEaw18CFPyo'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!person'):
        msg = 'Generating image...'.format(message)
        await client.send_message(message.channel, msg)
        imgurl ="https://thispersondoesnotexist.com/image"
        req.urlretrieve(imgurl, "image.jpg")
        with open('image.jpg', 'rb') as f:
            msg = 'This person does not exist: '.format(message)
            await client.send_message(message.channel, msg)
            await client.send_file(message.channel, f)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    #url = 'https://thispersondoesnotexist.com/image'
    #response = requests.get(url)
    #img = Image.open(BytesIO(response.content))
    #img.show

client.run(TOKEN)
