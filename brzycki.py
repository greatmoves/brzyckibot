import discord
from math import ceil

def onearems(weight, reps):
    percentages = [100, 95, 90, 85, 80, 75, 70, 65, 60]
    try:
        weight = int(weight)
        reps = int(reps)
    except ValueError:
        return -1
    
    multi = (36/(37-reps))
    if(reps == 1):
        description = f"For {reps} rep at {weight} Kg".format(reps, weight)
    else:
        description = f"For {reps} reps at {weight} Kg".format(reps, weight)
    embed = discord.Embed(title = "One rep max percentages", description = description, colour = 0xFF00CC)
    embed.set_footer(text = 'Calculated using Brzycki formula')
    for percentage in percentages:
        value = ceil((percentage/100)*weight*multi)
        embed.add_field(name = str(percentage)+"%", value = str(value)+" Kg")
    return embed
