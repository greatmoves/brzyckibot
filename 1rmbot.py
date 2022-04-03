from discord.ext import commands
from brzycki import onearems

client = commands.Bot(command_prefix = '!', help_command = None, owner_id = '')

@client.event
async def on_ready():
	print('Bot is running.')

@client.command()
async def onerepmax(ctx, weight, reps):
	async with ctx.typing():
		embed = onearems(weight, reps)
	await ctx.send(embed = embed)

@onerepmax.error
async def test_on_error(ctx, error):
	await ctx.send('Enter a weight in Kilograms and a number of reps')


client.run('')