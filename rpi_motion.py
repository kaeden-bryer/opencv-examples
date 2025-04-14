from picamera2 import Picamera2
import numpy as np
import cv2
import time

# Initialize the camera
picam2 = Picamera2()
picam2.configure(picam2.preview_configuration(main={"format": "RGB888", "size": (640, 480)}))
picam2.start()

last_mean = 0

while True:
    # Capture a frame
    frame = picam2.capture_array()  # Returns a NumPy array in RGB format

    # Optional: display the frame (converted to BGR for OpenCV display)
    cv2.imshow('frame', cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    print(gray)

    # Simple motion detection
    current_mean = np.mean(gray)
    result = np.abs(current_mean - last_mean)
    if result > 0.3:
        print("Motion detected!")
        print("Started recording.")
    last_mean = current_mean

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cv2.destroyAllWindows()
picam2.close()
