import discord
import time
import password as fonk

ozellik = discord.Intents.default()

ozellik.message_content = True

client = discord.Client(intents=ozellik)

@client.event
async def on_ready():
    print(f'{client.user} joined.')

@client.event
async def on_message(message):

    mesaj = message.content.lower()

    if message.author == client.user:
        return
    
    if mesaj.startswith('markerclient'):
        await message.channel.send("Hey! Its me! Write < help > to learn more.")

    elif mesaj.startswith('how are you'):
        await message.channel.send("I'm fine, serving humans as always -_-")

    elif mesaj.startswith('hey'):
        await message.channel.send("Whats up?")

    elif mesaj.startswith('bye'):
        await message.channel.send("Bye! \U0001f642")

    elif mesaj.startswith('hi'):
        await message.channel.send("Hey there!")

    elif mesaj.startswith('good morning'):
        await message.channel.send("good morning!")

    elif mesaj.startswith('good evening'):
        await message.channel.send("Thanks, good evening!")

    elif mesaj.startswith('good afternoon'):
        await message.channel.send("Good afternoon!")

    elif mesaj.startswith('good night'):
        await message.channel.send("Good night! By the way...its getting late, you should check your door...         *knock knock*")
        time.sleep(5)
        await message.channel.send("Hey, just kidding!")

    elif mesaj.startswith('help'):
        await message.channel.send("You can use: **client, help, how are you, hey, bye, hi, "
        "good morning, good afternoon, good evening, good night**")

    else:
        await message.channel.send(message.content)

client.run("token here")