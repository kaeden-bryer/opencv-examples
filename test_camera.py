from picamera2 import Picamera2

picam = Picamera2()

picam.start()
picam.capture_file("test.jpg")
picam.stop()