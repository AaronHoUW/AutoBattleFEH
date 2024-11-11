import pyautogui
import pygetwindow
import pytesseract
from PIL import Image
from pytesseract import Output

bluestacks_window = "BlueStacks App Player 1"
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract\\tesseract.exe'

def find_bluestacks_app():
    windows_list = pygetwindow.getAllTitles()  # Updated to use pygetwindow for getting titles
    if bluestacks_window in windows_list:
        window = pygetwindow.getWindowsWithTitle(bluestacks_window)[0]
        return window
    else:
        return None

def locate_text(bs, text):
    cur_screenshot = pyautogui.screenshot(region=(bs.left, bs.top + 32, bs.width, bs.height - 32)).convert('L')
    data = pytesseract.image_to_data(cur_screenshot, output_type=Output.DICT, config='--psm 11')
    coordinates = ()
    for i in range(len(data['text'])):
        if(data['text'][i] == text):
            x = data['left'][i]
            y = data['top'][i]
            width = data['width'][i]
            height = data['height'][i]
            print(x, y, width, height)
            coordinates = (x + width, y + height)
    return coordinates

def debug_locate_text(bs):
    cur_screenshot = pyautogui.screenshot(region=(bs.left, bs.top + 32, bs.width, bs.height - 32)).convert('L')
    data = pytesseract.image_to_data(cur_screenshot, output_type=Output.DICT, config='--psm 11')
    print(data)
    for i in range(len(data['text'])):
        if(data['text'][i] != ''):
            print(data['text'][i])


def locate_image(bs, image_path):
    bluestackRegion = (bs.left, bs.top + 32, bs.width, bs.height - 32) 
    borderx, bordery = pyautogui.locateCenterOnScreen(image_path, confidence=0.5, region=bluestackRegion)
    if borderx & bordery:
        pyautogui.moveTo(borderx, bordery)
        # pyautogui.click()
    

# character = "assets/Corrin_head.png"
# spriteX, spriteY = pyautogui.locateCenterOnScreen(character, grayscale=False, confidence=0.3)
# print(spriteX, spriteY, "TEST")
# pyautogui.moveTo(spriteX, spriteY)


# screenWidth, screenHeight = pyautogui.size()
# print(screenWidth, screenHeight)

# currentMouseX, currentMouseY = pyautogui.position()
# print(currentMouseX, currentMouseY)