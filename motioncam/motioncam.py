import RPi.GPIO as GPIO, time, cam

class motioncam(object):
    cam = None;
    motion_sensor = None;

    def __init__(self):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        self.cam = cam.cam("/var/smbshare/motionimage/")
        
        self.motion_sensor = 17;
        GPIO.setup(self.motion_sensor, GPIO.IN)

    def start(self):
        while True:
            while (GPIO.input(self.motion_sensor) == True):
                   self.cam.take_pic()
                   #we only need to capture every few seconds of the target.
                   time.sleep(1); 

#no need for another file.

mo_cam = motioncam()

mo_cam.start()