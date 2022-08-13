import discord
from discord.ext import commands
from discord import utils
import json

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', help_command=None, intents=intents)

@bot.event #On start
async def on_ready():
	print('Logged in as {0.user}!'.format(bot))
	game = discord.Game("Pau4ok#9629 to get bot like this")
	await bot.change_presence(status=discord.Status.idle, activity=game)

@bot.command()
async def mute(ctx,member: discord.Member,*,reason = None):
	await ctx.message.delete() #Delete message with command
	try:
		mutedRole = utils.get(member.guild.roles, name="Muted") #Gets muted role
	except:
		await ctx.guild.create_role(name="Muted") #If role isn't found, creates it
		mutedRole = utils.get(member.guild.roles, name="Muted") #Gets fresh muted role

	if mutedRole in member.roles: #Checks if muted role is in member roles
		embed=discord.Embed(color=0xa61206) #creates embed
		embed.set_author(name = f'{member.name} уже замучен', icon_url = member.avatar_url)
		emoji = '❌'
		bot_message = await ctx.send(embed=embed) #Sends embed
		await bot_message.add_reaction(emoji)

	else: #If muted role isn't in member roles
		await member.add_roles(mutedRole, reason=reason)

		if reason != None: #If mute has reason

			embed=discord.Embed( color=0xa61206) #Create embed
			embed.set_author(name = f'{member.name} замучен', icon_url = member.avatar_url)
			embed.add_field(name = 'По причине:', value=reason)
			emoji = '✅'
			bot_message = await ctx.send(embed=embed) #Send embed

			await bot_message.add_reaction(emoji)   

			print(f"Muted {member} for {reason}.") #Send logs

		else: #If mute hasn't reason
			embed=discord.Embed(color=0xa61206)
			embed.set_author(name = f'{member.name} замучен', icon_url = member.avatar_url)
			emoji = '✅'
			bot_message = await ctx.send(embed=embed)
			await bot_message.add_reaction(emoji)  
			#log
			print(f"Muted {member}.") 

@bot.command()
async def unmute(ctx, member: discord.Member):

	await ctx.message.delete() #Delete message with command
	try:
		mutedRole = utils.get(member.guild.roles, name="Muted")
	except:
		embed=discord.Embed(title = 'Role with name "Muted" was not found',description = 'Type !mute or create role "Muted"',color=0xa61206)
	#unmutes
	if mutedRole not in member.roles:
		embed=discord.Embed(color=0xa61206)
		embed.set_author(name = f'На {member.name} нет мута', icon_url = member.avatar_url)
		emoji = '❌'
		bot_message = await ctx.send(embed=embed)
		await bot_message.add_reaction(emoji)   
	else:
		await member.remove_roles(mutedRole)
		#creates embed
		embed=discord.Embed(color=0xa61206)
		embed.set_author(name = f'{member.name} размучен', icon_url = member.avatar_url) 
		emoji = '✅'
		bot_message = await ctx.send(embed=embed)
		await bot_message.add_reaction(emoji)
		#log
		print(f'Unmuted {member}.')    

@bot.command()
async def help(ctx):

	await ctx.message.delete()
	embed = discord.Embed(title = ":x: Это пробная версия бота",description="Чтобы открыть все функции обратитесь к Pau4ok#9629",color=0xa61206)
	embed.set_author(name = 'Pau4ok#9629',icon_url='https://sun9-84.userapi.com/impg/9ZDHpua9o5kFyG4z1iTgoIGw4wzdyLzXvxEIiQ/TSZ4-TrnNv4.jpg?size=494x493&quality=95&sign=5a43f5ca50a3747849537e0faab133b6&type=album')
	embed.add_field(name="Замутить участника", value="`!mute <@member>`")
	embed.add_field(name="Размутить участника",value="`!unmute <@member>`")
	embed.set_thumbnail(url='https://sun9-84.userapi.com/impg/9ZDHpua9o5kFyG4z1iTgoIGw4wzdyLzXvxEIiQ/TSZ4-TrnNv4.jpg?size=494x493&quality=95&sign=5a43f5ca50a3747849537e0faab133b6&type=album')
	await ctx.send(embed=embed)

bot.run('PUT YOUR TOKEN HERE')
