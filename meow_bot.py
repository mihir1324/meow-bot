import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

OWNER_ID = 1318322658882093069
HER_ID = 1110476803790880769

def is_authorized(ctx):
    return ctx.author.id in [OWNER_ID, HER_ID]

@bot.event
async def on_ready():
    print(f"We're live as {bot.user}")

@bot.command()
async def fightfix(ctx):
    if not is_authorized(ctx): return await ctx.send("meow only speaks 2 words — yours and hers 💘")
    await ctx.send("fights don't mean the end... they mean you both care enough to feel. patch up soon? 🌧❤️")

@bot.command()
async def motivateme(ctx):
    if not is_authorized(ctx): return await ctx.send("meow only speaks 2 words — yours and hers 💘")
    motivation = [
        "tu best h bs thoda aur ruk, phir sb tera hoga",
        "haar sirf tab hoti h jab tu chhod deta h... tu rukta nhi toh jeet confirm h",
        "khaas log der se chamkte h, but ek baar jo shine kre toh sab dekhte h"
    ]
    await ctx.send(random.choice(motivation))

@bot.command()
async def weirdo(ctx):
    if not is_authorized(ctx): return await ctx.send("meow only speaks 2 words — yours and hers 💘")
    await ctx.send(
        "weirdo? naah... more like:
1. the rarest soul
2. the kindest vibe
3. meri soft queen
4. the one who makes me smile without reason
5. nd the reason meow flirts with danger daily 😹"
    )

@bot.command()
async def hugher(ctx):
    if not is_authorized(ctx): return await ctx.send("meow only speaks 2 words — yours and hers 💘")
    await ctx.send("sending a soft fluffy hug to madam ji 💖 wrapped with care... and slight mischief 😼")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.author.id in [OWNER_ID, HER_ID] and "flirt" in message.content.lower():
        await message.channel.send("arre yrr owner dekh lega... uski madam se flirt krra hu, i'll be dead 😭")
    await bot.process_commands(message)
