import pyautogui
# import PIL

character = "assets/Corrin_head.png"

spriteX, spriteY = pyautogui.locateCenterOnScreen(character, grayscale=False, confidence=0.3)
# print(spriteX, spriteY, "TEST")
pyautogui.moveTo(spriteX, spriteY)


# screenWidth, screenHeight = pyautogui.size()
# print(screenWidth, screenHeight)

# currentMouseX, currentMouseY = pyautogui.position()
# print(currentMouseX, currentMouseY)