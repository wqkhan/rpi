from picamera import PiCamera
from time import sleep
from gpiozero import Button

  button = Button(16)
  camera = PiCamera()

  camera.start_preview()
  button.wait_for_press()
  camera.capture('~/Pictures/image.jpg')
  camera.stop_preview()