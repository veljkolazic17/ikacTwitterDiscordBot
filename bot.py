from ikac_function import ikac_py
import time
import random
import csv
import datetime
from discord.ext import commands
#prefiks koji se koristi pri pozivu komande
#client = discord.Client()
client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    #    await client.change_presence(status=discord.Status.online,activity=discord.Game('Snorting Cocaine'))
    print('SPREMAN')

@client.event
async def on_member_join(member):
    with open('memberJoin.csv', 'w', newline='') as csvfile:
        now = datetime.datetime.now()
        fieldnames = ['member', 'time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  
        writer.writeheader()
        writer.writerow({'first_name': member, 'time': now.strftime("%Y-%m-%d %H:%M:%S")})
    print(f'{member}<-0')

@client.event
async def on_member_remove(member):
    with open('memberRemove.csv', 'w', newline='') as csvfile:
        now = datetime.datetime.now()
        fieldnames = ['member', 'time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  
        writer.writeheader()
        writer.writerow({'first_name': member, 'time': now.strftime("%Y-%m-%d %H:%M:%S")})
    print(f'{member}->0')

@client.command()
async def prnt(ctx):
    random.seed()
    s = 'https://prnt.sc/'
    for _ in range(2):
        s += 'abcdefghijklmnopqrstuvwxyz'[random.randrange(0, 26,1)]
    for _ in range(4):
        s += str(random.randrange(0, 10,1))
    await ctx.send(s)

@client.command()
async def tw_o(ctx,search_name):
    timeline = ikac_py(search_name)
    s = "```"
    s+= timeline[0].text
    s+= "```"
    await ctx.send(s)

@client.command()
async def tw_l(ctx,arg,search_name):
    
    if int(arg) < 10:   
        timeline = ikac_py(search_name)
        
        def count_dict(timeline):
            counter = 0
            for x in timeline:
                counter = counter+1
            return counter

        counter = count_dict(timeline)
        s = "Number of tweets: " +  str(counter)
        if int(arg) > counter:
            arg = counter
        for i in range(int(arg)):
            s+="```"
            s+="Created at: "+timeline[i].created_at
            s+='\n\n'
            s+= timeline[i].full_text
            s+='\n'
            s+= '\u2764\ufe0f' + ':' 
            s+= str(timeline[i].favorite_count) + '  '
            s+= '\U0001F504' + ':' + str(timeline[i].retweet_count) + '  '
            s+= "```"
            s+='\n'
        await ctx.send(s)
    else:
        await ctx.send("Mnogo karaktera")
    print(timeline[0])
@client.command()
async def timer(ctx,seconds):
    start = time.time()
    time.clock()
    elapsed = 0
    counter = int(seconds) 
    poruka = await ctx.send(str(counter) + 's')
    while True:
        if counter == 0:
            break
        elapsed = time.time() - start
        counter = counter - 1
        time.sleep(1)
        await poruka.edit(content = str(counter)+'s')
    await ctx.send("Vreme je istekolo")

client.run('')
