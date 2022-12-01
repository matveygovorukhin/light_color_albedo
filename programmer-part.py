from time import sleep
from picamera import PiCamera 


#import modules

camera = PiCamera()
camera.brightness = 53

camera.start_preview() # Camera warm-up time
sleep(2)
camera.capture('D_mercury12_BHYTPNHHOCTb.png') # Take a picture

#'D_nakal10_Y.png'


#camera.stop_preview()

# camera.resolution = (1280, 720)
# camera.contrast = 10