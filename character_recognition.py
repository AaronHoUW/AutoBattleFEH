import pyautogui
import pygetwindow

bluestacks_window = "BlueStacks App Player 1"

def find_bluestacks_app():
    windows_list = pygetwindow.getAllTitles()  # Updated to use pygetwindow for getting titles
    if bluestacks_window in windows_list:
        window = pygetwindow.getWindowsWithTitle(bluestacks_window)[0]
        return window
    else:
        return None

def get_screenshot(bs):
    im = pyautogui.screenshot(region=(bs.left, bs.top + 32, bs.width, bs.height - 32))
    im.show()

def start():
    bs = find_bluestacks_app()
    if bs:
        get_screenshot(bs)
    else:
        print("Error: Unable to find screen")

start()

# character = "assets/Corrin_head.png"
# spriteX, spriteY = pyautogui.locateCenterOnScreen(character, grayscale=False, confidence=0.3)
# print(spriteX, spriteY, "TEST")
# pyautogui.moveTo(spriteX, spriteY)


# screenWidth, screenHeight = pyautogui.size()
# print(screenWidth, screenHeight)

# currentMouseX, currentMouseY = pyautogui.position()
# print(currentMouseX, currentMouseY)