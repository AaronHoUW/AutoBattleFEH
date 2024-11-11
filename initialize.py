import character_recognition as cr
import pyautogui
import time

fight = "assets/Button_Fight.png"

def run_forging_bonds():
    bs = cr.find_bluestacks_app()
    if bs:
        pyautogui.moveTo(cr.locate_text(bs, 'Advanced'))
        pyautogui.click()
        time.sleep(1)
        cr.locate_image(bs, fight)
        pyautogui.click()
    else:
        print("Error: Unable to find screen")

run_forging_bonds()