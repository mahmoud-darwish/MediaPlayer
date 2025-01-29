from AudioControlling import Controls
import time
song = Controls()
song.init_play("videoplayback.weba")
print(song.Totaltime())

song.play()
time.sleep(2)
song.pause()
while(1):
    print("paused")


