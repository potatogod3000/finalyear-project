import pyautogui
import cv2
import pytesseract
import espeakng
from screenshot_current_window import get_focused_window

def onscreen():
	# Get Focused window name with PID
	window = get_focused_window()

	# Take screenshot
	sshot_loc = 'Images/screenshot.png'
	screenshot = pyautogui.screenshot(sshot_loc)

	# Reading image
	image = cv2.imread(sshot_loc)
	# Convert to RGB
	img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	# Show the Output
	cv2.imshow("Output", image)
	#cv2.waitKey(0)

	# Detect texts from image
	tess_config = r'--oem 1'
	texts = pytesseract.image_to_string(img,config=tess_config)
	print(texts)

	speaker = espeakng.Speaker()
	speaker.rate=130
	speaker.say(texts)
