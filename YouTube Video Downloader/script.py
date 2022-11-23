from pytube import YouTube

link=input('Enter the URL: ')

yt=YouTube(link)

video=yt.streams.all()

vid=list(enumerate(video))
for x in vid:
    print(x)

stream=int(input('Select Quality : '))


video[stream].download()
print('Your video has been downloaded !')





