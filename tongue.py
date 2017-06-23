from pygame import mixer
import base64
import os
import sys
import io

class Tongue(object):
    def sayIt(self, audio): 
        sound = bytes(audio)
        sound = base64.b64decode(sound)

        f = open("temp.ogg",'wb')
        f.write(sound)
        os.fsync(f)
        f.close()

        mixer.init()
        mixer.music.load('temp.ogg')
        mixer.music.play()
