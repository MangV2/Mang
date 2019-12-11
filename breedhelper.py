
import os
import discord
import time


client = discord.Client()
#3600초=1시간
#1800초=30분
#1500=25분





#봇 준비 완료 메시지
@client.event 
async def on_ready():
    print(client.user.id)
    print('정상작동! ')

# 봇이 새로운 메시지를 수신했을때
@client.event
async def on_message(message):
    if message.author.bot: #메시지를 보낸 사용자가 봇이라면
        return None #무시
#명령어
@client.event
async def on_message(message):
    if message.content.startswith('%파라케 브리딩'):
        await message.channel.send('```  8시간뒤 알람설정!  ```')
        time.sleep(27000)
        await message.channel.send('30분뒤 파라케 출산!', tts=True)
        time.sleep(1500)
        await message.channel.send('5분뒤 파라케 출산!', tts=True)

    if message.content.startswith('%가스백 브리딩'):
        await message.channel.send('```  8시간뒤 알람설정!  ```')
        time.sleep(27000)
        await message.channel.send('30분뒤 가스백 출산!', tts=True)
        time.sleep(1500)
        await message.channel.send('5분뒤 가스백 출산!', tts=True)

    if message.content.startswith('%라이노 브리딩'):
        await message.channel.send('```  8시간뒤 알람설정!  ```')
        time.sleep(12600)
        await message.channel.send('30분뒤 라이노 출산!', tts=True)
        time.sleep(1500)
        await message.channel.send('5분뒤 라이노 출산!', tts=True)

    if message.content.startswith('%마나 브리딩'):
        await message.channel.send('```  8시간뒤 알람설정!  ```')
        time.sleep(12600)
        await message.channel.send('30분뒤 마나 출산!', tts=True)
        time.sleep(1500)
        await message.channel.send('5분뒤 마나 출산!', tts=True)

access_token = os.envrion[BOT_TOKEN]  
client.run(access_token)
