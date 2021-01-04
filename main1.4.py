import discord, time, math,random
from discord.ext import commands
from discord.utils import get
from pytube import YouTube
import os
import json
import requests
from bs4 import BeautifulSoup
import re
import imageio
import shutil
import nacl
import re
import youtube_dl
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import by


name = "Plumpbot"




nounList = [' people', 'history', 'way', 'art', 'world', 'information', 'map', 'two', 'family', 'government', 'health', 'system', 'computer', 'meat', 'year', 'thanks', 'music', 'person', 'reading', 'method', 'data', 'food', 'understanding', 'theory', 'law', 'bird', 'literature', 'problem', 'software', 'control', 'knowledge', 'power', 'ability', 'economics', 'love', 'internet', 'television', 'science', 'library', 'nature', 'fact', 'product', 'idea', 'temperature', 'investment', 'area', 'society', 'activity', 'story', 'industry', 'media', 'thing', 'oven', 'community', 'definition', 'safety', 'quality', 'development', 'language', 'management', 'player', 'variety', 'video', 'week', 'security', 'country', 'exam', 'movie', 'organization', 'equipment', 'physics', 'analysis', 'policy', 'series', 'thought', 'basis', 'boyfriend', 'direction', 'strategy', 'technology', 'army', 'camera', 'freedom', 'paper', 'environment', 'child', 'instance', 'month', 'truth', 'marketing', 'university', 'writing', 'article', 'department', 'difference', 'goal', 'news', 'audience', 'fishing', 'growth', 'income', 'marriage', 'user', 'combination', 'failure', 'meaning', 'medicine', 'philosophy', 'teacher', 'communication', 'night', 'chemistry', 'disease', 'disk', 'energy', 'nation', 'road', 'role', 'soup', 'advertising', 'location', 'success', 'addition', 'apartment', 'education', 'math', 'moment', 'painting', 'politics', 'attention', 'decision', 'event', 'property', 'shopping', 'student', 'wood', 'competition', 'distribution', 'entertainment', 'office', 'population', 'president', 'unit', 
'category', 'cigarette', 'context', 'introduction', 'opportunity', 'performance', 'driver', 'flight', 'length', 'magazine', 'newspaper', 'relationship', 'teaching', 'cell', 'dealer', 'finding', 'lake', 'member', 'message', 'phone', 'scene', 'appearance', 'association', 'concept', 'customer', 'death', 'discussion', 'housing', 'inflation', 'insurance', 'mood', 'woman', 'advice', 'blood', 'effort', 'expression', 'importance', 'opinion', 'payment', 'reality', 'responsibility', 'situation', 'skill', 'statement', 'wealth', 'application', 'city', 'county', 'depth', 'estate', 'foundation', 'grandmother', 'heart', 'perspective', 'photo', 'recipe', 'studio', 'topic', 'collection', 'depression', 'imagination', 'passion', 'percentage', 'resource', 'setting', 'ad', 'agency', 'college', 'connection', 'criticism', 'debt', 'description', 'memory', 'patience', 'secretary', 'solution', 'administration', 'aspect', 'attitude', 'director', 'personality', 'psychology', 'recommendation', 'response', 'selection', 'storage', 'version', 'alcohol', 'argument', 'complaint', 'contract', 'emphasis', 'highway', 'loss', 'membership', 'possession', 'preparation', 'steak', 'union', 'agreement', 'cancer', 'currency', 'employment', 'engineering', 'entry', 'interaction', 'mixture', 'preference', 'region', 'republic', 'tradition', 'virus', 'actor', 'classroom', 'delivery', 'device', 'difficulty', 'drama', 'election', 'engine', 'football', 'guidance', 'hotel', 'owner', 'priority', 'protection', 'suggestion', 'tension', 'variation', 'anxiety', 'atmosphere', 'awareness', 'bath', 'bread', 'candidate', 'climate', 'comparison', 'confusion', 'construction', 'elevator', 'emotion', 'employee', 'employer', 'guest', 'height', 'leadership', 'mall', 'manager', 'operation', 'recording', 'sample', 'transportation', 'charity', 'cousin', 'disaster', 'editor', 'efficiency', 'excitement', 'extent', 'feedback', 'guitar', 'homework', 'leader', 'mom', 'outcome', 'permission', 'presentation', 'promotion', 'reflection', 'refrigerator', 'resolution', 'revenue', 'session', 'singer', 'tennis', 'basket', 'bonus', 'cabinet', 
'childhood', 'church', 'clothes', 'coffee', 'dinner', 'drawing', 'hair', 'hearing', 'initiative', 'judgment', 'lab', 'measurement', 'mode', 'mud', 'orange', 'poetry', 'police', 'possibility', 'procedure', 'queen', 'ratio', 'relation', 'restaurant', 'satisfaction', 'sector', 'signature', 'significance', 'song', 'tooth', 'town', 'vehicle', 'volume', 'wife', 'accident', 'airport', 'appointment', 'arrival', 'assumption', 'baseball', 'chapter', 'committee', 'conversation', 'database', 'enthusiasm', 'error', 'explanation', 'farmer', 'gate', 'girl', 'hall', 'historian', 'hospital', 'injury', 'instruction', 'maintenance', 'manufacturer', 'meal', 'perception', 'pie', 'poem', 'presence', 'proposal', 'reception', 'replacement', 'revolution', 'river', 'son', 'speech', 'tea', 'village', 'warning', 'winner', 'worker', 'writer', 'assistance', 'breath', 'buyer', 'chest', 'chocolate', 'conclusion', 'contribution', 'cookie', 'courage', 'dad', 'desk', 'drawer', 'establishment', 'examination', 'garbage', 'grocery', 'honey', 'impression', 'improvement', 'independence', 'insect', 'inspection', 'inspector', 'king', 'ladder', 'menu', 'penalty', 'piano', 'potato', 'profession', 'professor', 'quantity', 'reaction', 'requirement', 'salad', 'sister', 'supermarket', 'tongue', 'weakness', 'wedding', 'affair', 'ambition', 'analyst', 'apple', 'assignment', 'assistant', 'bathroom', 'bedroom', 'beer', 'birthday', 'celebration', 'championship', 'cheek', 'client', 'consequence', 'departure', 'diamond', 'dirt', 'ear', 'fortune', 'friendship', 'funeral', 'gene', 'girlfriend', 'hat', 
'indication', 'intention', 'lady', 'midnight', 'negotiation', 'obligation', 'passenger', 'pizza', 'platform', 'poet', 'pollution', 'recognition', 'reputation', 'shirt', 'sir', 'speaker', 'stranger', 'surgery', 'sympathy', 'tale', 'throat', 'trainer', 'uncle', 'youth']


BING_IMAGE = \
    'https://www.bing.com/images/search?'
usr_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}
SaveFolder = "images"

client = commands.Bot(command_prefix = "-")

version = "1.4.2"

@client.event
async def on_ready():
    print("Bot is ready")
    await client.change_presence(status=discord.Status.online,activity=discord.Game(version))
    await  client.user.edit(username=name)

def SizeImageToFit(url):
    imageToBig = False
    scaleUp = .2
    itter = 1 + scaleUp
    folder = "temp/"
    while imageToBig == False:
        patternW = re.compile(r'w=.{3}')
        patternH = re.compile(r'h=.{3}')

        matchesW = patternW.findall(url)
        matchesH = patternH.findall(url)


        url = url.replace(matchesW[0],"w="+str(int(matchesW[0].replace("w=",""))+.2))

        return url
        
def main(searchTerm):
    if not os.path.exists(SaveFolder):
        os.mkdir(SaveFolder)
    return downloadImages(searchTerm)

def downloadImages(searchTerm):
    data = searchTerm
    print("starting search....")

    searchurl = BING_IMAGE+"q="+data
    print(searchurl)

    response = requests.get(searchurl, headers=usr_agent)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    results = soup.findAll("img",{"class":"mimg"})
    imageLinks = []
    goodLink = ""
    for result in results:
        tempLink = result.__str__()
        tempLink = tempLink.split(" ")
        for i in range(len(tempLink)-1,0,-1):
            if "src=" in tempLink[i]:
                if "data:" in tempLink[i]:
                    goodLink = "no"
                    break
                elif "data-" in tempLink[i]:
                    tempLink[i] = tempLink[i].replace("data-","")
                tempLink = tempLink[i].replace('src="',"")
                tempLink = tempLink[:-1]
                goodLink = tempLink
                break
        if goodLink != "no":
            #makiong the image bigger by changing the URL\
            imageLinks.append(goodLink)
            print("Passed")
    
            print(goodLink)
    if len(imageLinks) == 0:
        return False

    print(len(imageLinks))

    #response = requests.get(random.choice(imageLinks))
    response = requests.get(SizeImageToFit(imageLinks[0]))

    #changing name of the image to be found later
    counter = 0
    data = data.replace("-"," ")
    for file in os.listdir("images"):
        print(file.split("-")[0])
        print(data.replace(" ",""))
        if file.split("-")[0].upper() == data.replace(" ","").upper() :
            counter += 1
    imageName = SaveFolder +"/" + data.lower() +"-"+str(counter) +".jpg"
    imageName = imageName.replace(" ","")
    with open(imageName, "wb") as file:
        file.write(response.content)
    return imageName

@client.event
async def on_member_join(member):
    print(f"{member} has joined the server")

@client.event
async def on_member_remove(member):
    print(f"{member} has left the server")

@client.event
async def on_message(message):
    global client
    if  message.author.id != 672540355765338124:
        if "-image" in message.content:
            #try:
            if "-image" in message.content:
                temp = main(message.content.replace("-image",""))
                if temp == False:
                    await message.channel.send("No Results")
                else:
                    await message.channel.send(file=discord.File(temp))
            elif "-image " in message.content:
                temp = main(message.content.replace("-image ",""))
                if temp == False:
                    await message.channel.send("No Results")
                else:
                    await message.channel.send(file=discord.File(temp))
            print("Sent image")
            #except:
             #   await message.channel.send("Error, invalid character(s)")
        elif "RIP" in message.content.upper():
            await message.channel.send("RIP")
        elif "F" == message.content.upper() or "F IN CHAT" in message.content.upper():
            await message.channel.send("F")
        elif "THANK YOU PLUMPBOT" == message.content.upper():
            await message.channel.send("NP")
    await client.process_commands(message)

@client.command()
async def ping(ctx):
    print("bruh?")
    await ctx.send(f"{round(client.latency*1000)} ms")

@client.command(aliases=["?"])
async def question(ctx,*,question):
    badWordEnds = ["YOU WILL DIE!","IT WILL EAT YOU!","YOU WILL EXPLODE!","YOU WILL GET OOOOOFED!"]
    goodWordEnds = ["YOU WILL BE RICH!","YOU WILL GROW STRONGER!","IT WILL ALL END WELL!"]
    responses = [f"NO DON'T {' '.join(question.split(' ')[2:]).replace('?','')} {random.choice(badWordEnds)}" , f"YES DO {' '.join(question.split(' ')[2:]).replace('?','')} {random.choice(goodWordEnds)}"]
    await ctx.send(random.choice(responses))

@client.command(pass_context=True)
async def stop(ctx):
    channel = ctx.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    await voice.disconnect()

@client.command(pass_context=True)
async def play(ctx,url:str):

    
    try:
        video = YouTube(url)
        videoLength = video.length/60
    except:
        videoLength = 10
    if videoLength > 40:
        await ctx.send("Video Cannot be over 12 minutes!")
    else:
        try:
            channel = ctx.author.voice.channel
        except:
            await ctx.send("**Error** you need to be in a voice channel!")
            channel = ctx.author.voice.channel
        voice = get(client.voice_clients, guild=ctx.guild)
        
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
        
        await voice.disconnect()

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

        ydl_opts = {
            "format":"bestaudio/best",
            'noplaylist' : True,
            "postprocessors":[{
                "key":"FFmpegExtractAudio",
                "preferredcodec":"mp3",
                "preferredquality":"192",
            }],
        }

        fileName = "song"+str(random.randint(0,100000))+".mp3"

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        for file in os.listdir("./"):
            if file.endswith(".mp3"):

                
                os.rename(file,fileName)
                shutil.move(fileName,"audio/")
                #os.rename(file,"song"+random.randint(0,1000000)+".mp3")
        voice.play(discord.FFmpegPCMAudio("audio/"+fileName))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = .5

@client.command(pass_context=True)
async def ad(ctx,searchTerm=""):

    await ctx.send("Serving you up a **spicy** ad")
    fileName = "song"+str(random.randint(0,100000))+".mp3"

    try:
        channel = ctx.author.voice.channel
    except:
        await ctx.send("**Error** you need to be in a voice channel!")
        channel = ctx.author.voice.channel
    
    voice = get(client.voice_clients, guild=ctx.guild)
    
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    
    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    url = getAdUrl(searchTerm,aditional="advertisement")
    #video = YouTube(url)



    print(url)

    ydl_opts = {
        "format":"bestaudio/best",
        'noplaylist' : True,
        "postprocessors":[{
            "key":"FFmpegExtractAudio",
            "preferredcodec":"mp3",
            "preferredquality":"192",
            
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except:
            await ctx.send("**Error** *Unknown*, please try again")
            ydl.download([url])
    print("got stream")

    for file in os.listdir("./"):
        if file.endswith(".mp3"):

            
            os.rename(file,fileName)
            shutil.move(fileName,"ad/")


    voice.play(discord.FFmpegPCMAudio("ad/"+fileName))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = .5


    await ctx.send("||You are listneing to: "+url+"||")



@client.command(pass_context=True,aliases=["get"])
async def getVideo(ctx,searchTerm=""):

    await ctx.send("Serving you up a **spicy** video")
    fileName = "song"+str(random.randint(0,100000))+".mp3"

    try:
        channel = ctx.author.voice.channel
    except:
        await ctx.send("**Error** you need to be in a voice channel!")
        channel = ctx.author.voice.channel
    
    voice = get(client.voice_clients, guild=ctx.guild)
    
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    
    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    url = getAdUrl(searchTerm)
    #video = YouTube(url)



    print(url)

    ydl_opts = {
        "format":"bestaudio/best",
        'noplaylist' : True,
        "postprocessors":[{
            "key":"FFmpegExtractAudio",
            "preferredcodec":"mp3",
            "preferredquality":"192",
            
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except:
            await ctx.send("**Error** *Unknown*, please try again")
            ydl.download([url])
    print("got stream")

    for file in os.listdir("./"):
        if file.endswith(".mp3"):

            
            os.rename(file,fileName)
            shutil.move(fileName,"ad/")


    voice.play(discord.FFmpegPCMAudio("ad/"+fileName))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = .5


    await ctx.send("You are listneing to: "+url)

def getAdUrl(searchTerm,aditional=""):
    if searchTerm == "":
        searchTerm = random.choice(nounList)
    opts = Options()
    opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0")
    opts.add_argument("headless")
    driver = webdriver.Chrome("resources/chromedriver",chrome_options=opts)
    youtubeUrl = 'https://www.youtube.com/results?search_query='+searchTerm+aditional

    driver.get(youtubeUrl)
    itter = 0
    videoLength = 20
    while videoLength > 15:
        listNub = None
        while listNub == None:
            try:
                listNub = driver.find_elements_by_id("thumbnail")[:-1]
            except:
                listNub = None
        videoURL = random.choice(listNub).get_attribute("href")
        videoURL = random.choice(listNub).get_attribute("href")
        #tempVideo = YouTube(videoURL)
        videoLength = 1
        print("just one moment")
        #itter += 1
        #if itter > 13:
        #    raise Exception("Can't find video under 13 minutes")
        
        
    print("Got Soup")
    return videoURL

@client.command(pass_context = True)
async def clear(ctx, number):
    mgs = [] #Empty list to put all the messages in the log
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)



client.run("")