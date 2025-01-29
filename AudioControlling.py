import vlc
import time

class Controls:
    
    def __init__(self):
        self.flag = 1
        #print("init")
        pass
    def init_play(self,file_path):
        self.player = vlc.MediaPlayer(file_path)
        self.player.play()
    def play(self):
        if not self.player.is_playing():
            self.player.play()
            time.sleep(1)  # Wait for the player to initialize
        #print("played")
   
    def pause(self):
        self.player.pause()
        time.sleep(1)

    def resume(self):
        self.player.play()
        time.sleep(1)
        

    def fast_forward(self, seconds):
        current_time = self.player.get_time()
        self.player.set_time(current_time + seconds * 1000)

    def rewind(self, seconds):
        current_time = self.player.get_time()
        self.player.set_time(current_time - seconds * 1000)

    def mute(self):
        self.player.audio_toggle_mute()

    def unmute(self):
        self.player.audio_toggle_mute()

    def Two_x(self):
        self.player.set_rate(2)

    def increase_volume(self, amount):
        current_volume = self.player.audio_get_volume()
        self.player.audio_set_volume( amount)

    def decrease_volume(self, amount):
        current_volume = self.player.audio_get_volume()
        self.player.audio_set_volume(current_volume - amount)

    def stop(self):
        self.player.stop()
        time.sleep(1)
        
    
    def get_time(self):
        current_time = float(self.player.get_time()) / 1000
        return current_time
    
    def Totaltime(self):
        self.play()
        return self.player.get_length() / 1000