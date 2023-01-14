import picamera
import time
camera = picamera.PiCamera()
camera.resolution = (640,480)
camera.vflip = True

#camera.start_preview()

camera.start_recording('videos/video5.h264')
time.sleep(300)
camera.stop_recording()
#camera.stop_preview()
