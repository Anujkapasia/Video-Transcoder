import os
import subprocess

dick={
    "l":["360p","480p","720p","1080p"],
    "name":"brokeasfd",
    "input":"C:/inputvids/vid.mp4",
    "outputlocation":"C:/Users/anujk/Desktop/wotimmaheadout",
}



def converter(dick):
    res="640x480"
    path=os.path.join(dick["outputlocation"],dick["name"])
    os.mkdir(path)
    for i in range(len(dick["l"])):
        if (dick["l"][i]=="360p"):
            res="480x360"
        elif (dick["l"][i]=="720p"):
            res="1280x720"
        elif (dick["l"][i]=="1080p"):
            res="1920x1080"
        subprocess.call(f'ffmpeg -i {dick["input"]} -filter:v fps=fps=60 -profile:v baseline -level 3.0 -s {res} -start_number 0 -hls_time 10 -hls_list_size 0 -f hls {dick["outputlocation"]}/{dick["name"]}/{dick["name"]}_{dick["l"][i]}_.m3u8', shell=True)



