import discord

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
    
    elif mesaj.startswith('help'):
        await message.channel.send("Hey there! You can ask me about what needs to be done to protect nature. **(Ideas to protect the nature)**")

    elif mesaj.startswith('ideas to protect the nature') or mesaj.startswith('ıdeas to protect the nature'):
        await message.channel.send("Here are 10 ideas:\n"
                                   "-------------------------------------------------------------\n"
                                    "**1) Volunteer. Volunteer for cleanups in your community.**\n"
                                    "-------------------------------------------------------------\n"
                                    "**2) You can get involved in protecting your watershed, too.**\n"
                                    "-------------------------------------------------------------\n"
                                    "**3) Educate. When you further your own education, you can help others understand the importance and value of our natural resources.**\n"
                                    "-------------------------------------------------------------\n"
                                    "**4) Conserve water. The less water you use, the less runoff and wastewater that eventually end up in the ocean.**\n"
                                    "-------------------------------------------------------------\n"
                                    "**5) Shop wisely. Buy less plastic and bring a reusable shopping bag.**\n"
                                    "-------------------------------------------------------------\n"
                                    "**6) Use long-lasting light bulbs. Energy efficient light bulbs reduce greenhouse gas emissions. Also flip the light switch off when you leave the room!**\n"
                                    "-------------------------------------------------------------\n"
                                    "**7) Plant a tree. Trees provide food and oxygen. They help save energy, clean the air, and help combat climate change.**\n"
                                    "-------------------------------------------------------------\n"
                                    "**8) Don't send chemicals into our waterways. Choose non-toxic chemicals in the home and office.**\n"
                                    "-------------------------------------------------------------\n"
                                    "**9) Bike more. Drive less.**\n"
                                    "-------------------------------------------------------------\n"
                                    "**10) Use public transportation to prevent noise pollution.**")

    else:
        await message.channel.send(message.content)

client.run("token here")
