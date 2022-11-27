from gtts import gTTS 

text=str(input('Please enter the text you want to convert to audio : '))
lan='''Please enter the accent :
       English : en
       French : fr
       Mandarin(China Mainland) : zh-CN
       Mandarin(Taiwan) : zh-TW
       Portuguese : pt
       Spanish : es    
    '''
print(lan)
language=str(input())

translate=gTTS(text,lang=language)
translate.save('audio.mp3')

print('Success!')