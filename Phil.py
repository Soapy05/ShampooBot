import discord
from discord.ext import commands

import random
from random import randint
numbers = ["5"]
rng = ["10"]

TOKEN = "NjExMjEzOTA4ODcwNTYxODA3.XVQjmA.5o67yhvyUc872iS8a7EuaelLV8s"
command_prefix = ""
client = commands.Bot(command_prefix + "=")
@client.event
async def on_ready():
    print("yeet")
@client.command()
async def ping(ctx):
    print("Pong!")
    await ctx.send("Pong!")

@client.command()
async def creeper(ctx):
    await ctx.send("Aww man")

@client.command()
async def cookie(ctx):
    await ctx.send("Thank you for the cookie :3")

@client.command()
async def coinflip(ctx):
    side = randint(1,2)
    if side == 1:
        embed = discord.Embed(
                colour = discord.Colour.green()
            )
        embed.add_field(name= 'Coin Flip' , value = 'Heads!', inline=False)
        await ctx.send(embed=embed)
    elif side == 2:
        embed = discord.Embed(
                colour = discord.Colour.green()
            )
        embed.add_field(name= 'Coin Flip' , value = 'Tails!', inline=False)
        await ctx.send(embed=embed)

@client.command()
async def roulette(ctx):
    roulettes = ["roulette1.jpg","roulette2.jpg","roulette3.jpg","roulette4.jpg","roulette5.jpg","roulette6.jpg"]
    choice = roulettes[randint(0,5)]
    file = discord.File(choice, filename="Roulette.jpg")
    await ctx.send(file=file)


    if choice == roulettes[0]:
        pick = []
        part = ["V:","W:","X:","Y:","Z:"]
        for x in range (5):
            pick = (randint(1,10))
            embed = discord.Embed(
                colour = discord.Colour.blue()
            )
            embed.add_field(name=part[x-1] , value = pick, inline=False)
            await ctx.send(embed=embed)
            
    elif choice == roulettes[1]:
        pick = []
        part = ["T:","U:","V:","W:","X","Y","Z"]
        for i in range (7):
            pick = (randint(0,9))
            embed = discord.Embed(
                colour = discord.Colour.blue()
            )
            embed.add_field(name=part[i-1] , value = pick, inline=False)
            await ctx.send(embed=embed)
            
    elif choice == roulettes[2]:
        pick = []
        part = ["X","Y"]
        for i in range (2):
            pick = (randint(1,6))
            embed = discord.Embed(
                colour = discord.Colour.blue()
            )
            embed.add_field(name=part[i-1] , value = pick, inline=False)
            await ctx.send(embed=embed)

    elif choice == roulettes[3]:
        pick = []
        part = ["W","X","Y","Z"]
        for i in range (4):
            pick = (randint(0,9))
            embed = discord.Embed(
                colour = discord.Colour.blue()
            )
            embed.add_field(name=part[i-1] , value = pick, inline=False)
            await ctx.send(embed=embed)        
        
        
    elif choice == roulettes[4]:
        pick = []
        part = ["W","X","Y","Z","V"]
        for i in range (5):
            pick = (randint(0,9))
            embed = discord.Embed(
                colour = discord.Colour.blue()
            )
            embed.add_field(name=part[i-1] , value = pick, inline=False)
            await ctx.send(embed=embed)
        
        
    elif choice == roulettes[5]:
        pick = []
        part = ["Y","Z"]
        for i in range (2):
            pick = (randint(0,9))
            embed = discord.Embed(
                colour = discord.Colour.blue()
            )
            embed.add_field(name=part[i-1] , value = pick, inline=False)
            await ctx.send(embed=embed)        


client.run(TOKEN)

