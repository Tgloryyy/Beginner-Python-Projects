import os,shutil

path=r'C:\Users\Admin\Downloads'
documents_path=r'C:\Users\Admin\Desktop\New folder\Documents'
audio_path=r'C:\Users\Admin\Desktop\New folder\Audio'
video_path=r'C:\Users\Admin\Desktop\New folder\Videos'
images_path=r'C:\Users\Admin\Desktop\New folder\Images'

listoffiles=os.listdir(path)


for x in listoffiles:

    string=str(path+'\\'+x)
    
    if x.lower().endswith(('.jpg','.png','.gif','.webp','.tiff','.psd','.raw','.bmp','.heif','.indd','.jpeg')):   
        shutil.move(string,images_path)
    elif x.lower().endswith(('.webm','.mpg','.mp2','.mpeg','.mpe','.mpv','.ogg','.mp4','.m4p','.m4v','.avi','.wmv','.mov','.qt','.flv','.swf','.avchd')):
        shutil.move(string,video_path)
    elif x.lower().endswith(('.mp3','.m4a','.aac','.oga','.ogg')):
        shutil.move(string,audio_path)
    elif x.lower().endswith(('.doc','.docx','.html','.htm','.odt','.pdf','.xls','.xlsx','.ods','.ppt','.pptx','.txt')):
        shutil.move(string,documents_path)
   
print('DONE !')


   
