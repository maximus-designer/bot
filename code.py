ines (286 sloc)  8.79 KB
   
from Truth & Dare import Truth & Dare

import discord
from discord.ext import commands,tasks
from itertools import cycle
import random

intents = discord.Intents(messages = True , guilds = True ,  reactions = True , members = True , presences = True)
client  = commands.Bot(command_prefix = '+', intents = intents)


@client.event 
async def on_ready():
  change_status.start()
  print("I am turned on!!")

status = cycle(['With Friends','With Parents','With Love','With Yourself'])


@tasks.loop(seconds=5)
async def change_status():
  await client.change_presence(activity=discord.Game(f'{next(status)} | .help'))  

  
@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send('Invalid Command Used. Type .help to know the commands')
                       
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Give proper values to the command an argument is missing')
  
  
@client.command()
async def clean(ctx, num = 1):
  await ctx.channel.purge(limit = num+1)  


truths = ["What’s the last lie you told?",

"Whose chats/calls do you ignore the most in this room?"
,
"What’s your most bizarre nickname?"
,
"What’s been your most physically painful experience?"
,
"What’s the craziest thing you’ve done on public transportation?"
,
"If you met a genie, what would your three wishes be?/n You cannot say 'n' more wishes."
,
"What’s one thing you’d do if you knew there no consequences?"
,
"What’s the craziest thing you’ve done in front of a mirror?"
,
"What’s the meanest thing you’ve ever said about someone else?"
,
"Who are you most jealous of?"
,
"What's the type of cloth your partner to wears that turns you on?"
,
"What's your most embarrasing incident in front of your college professor?"
,
"Would you date your high school crush today?"
,
"Do you believe in any superstitions? If so, which ones and why?"
,
"What’s your most embarrassing habit?"
,
"Have you ever considered cheating on a partner? If yes then why?"
,
"If you were guaranteed to never get caught, who on Earth would you murder?"
,
"What’s the cheapest gift you’ve ever gotten for someone else?"
,
"Which of your family members annoys you the most and why?"
,
"What’s your biggest regret in life?"
,
"Have you ever regretted something you did to get a crush or partner’s attention?"
,
"What’s one not so common job you could never do?"
,
"If you switched genders for a day, what would you do?"
,
"When’s the last time you made someone else cry and how?"
,
"What’s the most embarrassing thing you’ve done in front of a crowd?"
,
"If you could become invisible, what’s the worst thing you’d do?"
,
"Have you ever farted and blamed it on someone else and to whom?"
,
"What’s something you would die if your mom found out about?"
,
"If you had one week to live and you had to marry someone in this room, who would it be?\nImagine everyone in your list is single."
,
"List one negative thing about anyone in the room."
,
"What’s the most sinful thing you’ve done in a house of worship?"
,
"Who would you call to help bury a body?"
,
"What’s the most embarrassing thing your parents have caught you doing?\nAhem ahem!"
,
"When’s the last time you peed your pants?"
,
"What’s your biggest insecurity?"
,
"What’s your wildest fantasy?"
,
"If you could hire someone to do one thing for you, what would it be?"
,
"What’s the best lie/brag you’ve ever told anyone?"
,
"What’s the weirdest thing you’ve ever done in a bathroom? Ahem Ahem!"
,
"What’s the biggest secret you’ve kept from your parents?"
,
"If you were rescuing people from a burning building and you had to leave one person behind from this room, who would it be?\nCruel isn't it :p"  
,
"When did you first started watching p*rn?"
,
"Why are you still addicted to something that you know is bad?"
,
"Have you ever hit on anyone's private part?What's their worst reaction"
,
"Do you think any girl loves you?"
,
"Why is melody chocolate melody?"
,
"If you could get a bf from this room assuming everyone's single, who would it be?"
,
"Who do you think hits on you the most in this room?"
,
"What is your biggest fantasy?"
,
"When was the last time you lied?"
,
"When was the last time you cried?"
,
"What's your biggest fantasy?"
,
"What's something you're glad your mum doesn't know about you?"
,
"what's your last web search history"
]





dares = ["Call your crush or any random person you never talk and start a random talk."
,
"Belly dance, twerk or do the moonwalk in front of everyone."
,
"Quote or enact your favourite Bollywood celebrity!"
,
"Try putting your entire fist in your mouth!"
,
"Call a person(opposite sex) and tell him that he/she is the most handsome/beatuiful person you have ever seen."
,
"Sing a romantic song."
,
"Share an old, embarrassing picture from your FB album on your timeline."
,
"Talk in a different accent for one hour."
,
"Apply soap on your face and don’t wash it for 10 minutes."
,
"Call up a restaurant and ask them the contact number of another restaurant."
,
"Post a random long status on Facebook/Instagram/Whatsapp Status."
,
"Remove your socks with your teeth."
,
"Do jumping jacks for one minute."
,
"Dial a random number and sing ‘Happy Birthday!’"
,
"Talk like a robot for the next 15 minutes of the game."
,
"Call up your friend and tell him/her how much you love his/her boyfriend/girlfriend."
,
"Tell your siblings that you just found out they are adopted."
,
"Fill your mouth with water and sing a song."
,
"Sing a song in a sexy voice."
,
"Try to turn someone on in the room."
,
"Kiss a stuffed toy/object passionately."
,
"Treat me with 3 plates of momo whenever we meet next."
,
"Pick up a random book and read a chapter in the most seductive voice you can manage."
,
"Say atleast one honest thing about every player in the room."
,
"Do 20 push-ups."
,
"Eat 2-7 green chillies."
,
"Roast the person below you."
,
"Shave a small portion of your head with a trimmer."
,
"Do your best impression of someone in the room and keep going until someone correctly guesses who it is."
,
"Fake a pregnancy on social media."
,
"Take a selfie and upload it now, without any filters on your whatsapp status without hiding anymore person."
,
"Show us how you cry alone."
,
"Go to Facebook or Instagram profile of the girl and comment romantic line(s) on her pic."
,
"Sing like you are an opera singer."
,
"Call the last person you texted and shout on him/her."
,
"Make the first five emoji faces that you have used recently."
,
"Call an old friend of yours and tell him/her that they were your first crush."
,
"Make a call to your teacher. Ask, when will be the next class?"
,
"Predict the future of every person in this room. "
,
"Call/text someone randomly and say, You have a crush on them. (wait for their response)"
,
"Call/text someone randomly and say, You want to have a threesome with them. (wait for their response)"
,
"Confess something, that no one knows."
,
"Draw something on your forehead."
,
"Talk like Alexa or Siri."
,
"Call your partner and inform. “It’s over.”"
,
"Share your thoughts on relationships and marriage, like an expert."
,
"Go out and shout “I don't want to die.” Three times."
,
"Cry as if you just broke up with your loving partner. "
,
"Lick your shoe/slipper."
,
"Apply dettol to your face mask."
,
"How would you react if your partner says, let's have s*x."
,
"Act as if your parents caught you m@$turb@t!ng."
,
"Drink 1L of water right now."
,
"Dance but no one should record."
,
"Try doing a bottle flip but everytime you fail you scream."
,
"Shout song lyrics for next 10 seconds."
,
"Roast a person here."
,
"Draw something on your cheek with marker."
,
"Send a message in the chat about your sexual fantasies."
,
"Moan for next 30 seconds."
,
"Say O with your mouth closed."
,
"Start talking in babu shona totla language for the next 30minutes."
,
"Go on a date with your gf oops sorry your single lmao"
,
"Solve a question from any given assignment right now."
,
"Post this in your insta story the pic of your first crush"
,
"Solve JEE Advance 2021 Physics first question?"
,
"Do 100 squats"
,
"Show the most embarrasing photo on your phone"
,
"Show your last 5 chats"
,
"Order a zomato delivery for your friend!"
,
"Watch Boku no Pico with your crush"]



@client.command(aliases = ['t'])

async def truth(ctx):

  await ctx.send(random.choice(truths))


@client.command(aliases = ['d'])

async def dare(ctx):
  
  await ctx.send(random.choice(dares))



keep_alive()
client.run('ODQyODY3NDewrsaDY1.YJ7jcg.wWLwkaBA_SsfhsosfaXROuQlU')
© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
