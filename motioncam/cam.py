#Class that exposes the webcam conected to the pi
#you will need foscam to actually take the picture.
import os
import time

class cam(object):
    
    path = None
    resolution = None 

    def __init__(self, path):
        self.path = path

    #Use foscam to take a picture.
    def take_pic(self):
        snap_time = time.time()
        command = "sudo fswebcam -d /dev/video0 --jpeg 90 -r 320x240 --save " + self.path + str(snap_time) + ".jpg"
        os.system(command)