import discord
from discord.ext import commands, tasks
import asyncio
import random

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='+', intents=intents)

OWNERID = 1295326028360585289
GIVEAWAY_CHANNEL_NAME = 'giveaways'
GUILD_ID = 1295324485292916758  
SPECIAL_CHANNEL_ID = 1295437345205780561 
ROLE_ID = 1295436489521500241 

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    print(f"Message received in channel {message.channel.id} from {message.author.display_name}: {message.content}")

    if message.channel.id == SPECIAL_CHANNEL_ID:
        if bot.user.mentioned_in(message) and "TER" in message.author.display_name:
            print("Bot mentioned and user has 'TER' in display name.")
            role = discord.utils.get(message.guild.roles, id=ROLE_ID)
            if role not in message.author.roles:
                try:
                    await message.author.add_roles(role)
                    await message.channel.send(f'{message.author.mention}, you have the {role.name} role!')
                    print(f"Role {role.name} assigned to {message.author.display_name}.")
                except discord.Forbidden:
                    await message.channel.send("I don't have permission to assign that role.")
                    print("Permission error when trying to assign role.")
                except discord.HTTPException as e:
                    await message.channel.send("An error occurred while assigning the role.")
                    print(f"HTTP error: {e}")
            else:
                await message.channel.send(f'{message.author.mention}, you already have the {role.name} role.')
                print(f"{message.author.display_name} already has the role {role.name}.")

    await bot.process_commands(message)

@bot.command()
@commands.has_role(OWNERID)
async def renew(ctx):
    if isinstance(ctx.channel, discord.TextChannel):
        channel_name = ctx.channel.name
        channel_category = ctx.channel.category

        overwrites = ctx.channel.overwrites

        await ctx.channel.delete()

        new_channel = await ctx.guild.create_text_channel(
            name=channel_name,
            category=channel_category,
            overwrites=overwrites,
        )

        await new_channel.send(f'renewed {new_channel.mention}.')

@renew.error
async def renew_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("u cant use this cmd boy")



bot.run('MTI5NTM5ODAxODg1MzM3MTk0NQ.G4SHxx.kQj6CH_SDAOLAXA_gH27jZczoIU00Tkpd8bj0Q')
