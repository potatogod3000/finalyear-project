import cv2
from PIL import Image
from picamera2 import Picamera2, Preview	# Raspberry Pi Camera and Preview library
from picamera2.previews import QtGlPreview	# QtGlPreview from Camera Previews library
from libcamera import controls
from push_button import push_count
from screenshot import onscreen
from time import sleep						# Sleep from Time library
import pytesseract							# TesseractOCR library
import espeakng								# eSpeakNG library

# Initialize eSpeakNG TTS
speaker = espeakng.Speaker()
speaker.rate=130


print("Welcome to Raspberry Pi-based Reader.\n")
speaker.say("Welcome to Raspberry Pi-based Reader.")

# Initialize and start camera
camera = Picamera2()

# Push-button loop unconditionally
while True:
	print(">> Press the push-button ONCE if you want to capture image and convert it into audio. <<\n>> Press the push-button twice if you want to convert an on-screen image (with text) into audio. <<\n")
	speaker.say("Press the push-button once if you want to capture image and convert it into audio. Press the push-button twice if you want to convert an on-screen image (with text) into audio.", wait4prev=True)
	btn_count = push_count()
	if btn_count == 1:
		# Capture image and stop camera preview and usage
		camera.start(show_preview=True)
		camera.set_controls({"AfMode": controls.AfModeEnum.Continuous, "AfSpeed": controls.AfSpeedEnum.Fast})
		sleep(5)

		camera.start_and_capture_file("Images/captured.jpg")
		speaker.say("Image Captured. Please standby, saving image and processing...")
		camera.stop_preview()
		camera.stop()

		# OpenCV
		image = "Images/captured.jpg"
		img = cv2.imread(image)
		# Convert to Grayscale
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

		# Detect texts from captured image
		#tess_config = r'--oem 1 --psm 3'
		texts = pytesseract.image_to_string(img) #config=tess_config
		print(texts)

		# TTS Output from Tesseract output
		speaker.say(texts, wait4prev=True)

	elif btn_count() == 2:
		onscreen()

	sleep(2)
	print("\nRepeating the process...\n")
	speaker.say("Repeating the process...", wait4prev=True)
