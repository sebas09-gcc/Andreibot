import random
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>',description="This is a helper bot")

@bot.command()
async def andrei(ctx):
    await ctx.send('HOLA! Soy AndreiBot, el bot mas random de la PUCP')



@bot.command()
async def pucp(ctx):
    embed=discord.Embed(title="CAMPUS VIRTUAL Y PAIDEIA",description="Acceso directo al Campus Virtual y Paideia PUCP",color=discord.Color.blue())
    embed.add_field(name="CAMPUS VIRTUAL",value=f"https://campusvirtual.pucp.edu.pe")
    embed.add_field(name="PAIDEIA",value=f"https://paideia.pucp.edu.pe")
    await ctx.send(embed=embed)

@bot.command()
async def chiste(ctx):
    a=random.randint(10, 12)
    if a==10:
        await ctx.send('¿Qué le menciona una IP a otra? — ¿Qué tramas?.')
    if a==11:
        await ctx.send('¿Qué es un terapeuta? – 1024 Gigapeutas.')
    if a==12:
        await ctx.send('¿Que le habla un bit al otro? Nos vemos en el bus.')

@bot.command()
async def drive(ctx):
    embed=discord.Embed(title="Evaluaciones anteriores",description="Aqui podrán encontrar evaluaciones pasadas y algunos solucionarios",color=discord.Color.green())
    embed.add_field(name="DRIVE TP(creditos a Ezalor)",value=f"https://drive.google.com/drive/folders/1B8CUeylUA3swaLI-dxTcqGOOndSZIX9N?usp=sharing")
    embed.add_field(name="DRIVE INF(creditos a ODD)",value=f"https://drive.google.com/drive/folders/17CodwIiKFJxyPAxyo1PldZBKI1WMDpcO?usp=sharing")
    await ctx.send(embed=embed)

@bot.command()
async def descanso(ctx):
    await ctx.send('Estaré en mantenimiento. VOLVERE!')
#events
@bot.event
async def on_ready():
    game = discord.Game('dormir mas tiempo')
    await bot.change_presence(status=discord.Status.idle, activity=game)
    print('Andrei ha iniciado su trabajo')
    

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Holaaa {member.name}, bienvenido al Pool de Informatica version Discord!')

bot.run('ODI0ODgyMjYzNTE4NjA5NDA5.YF11eQ.uxwRy2KPNrYGIuV4YocInkMJPso')