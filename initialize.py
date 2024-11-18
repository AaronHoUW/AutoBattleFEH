import character_recognition as cr
from PIL import Image
import pyautogui
import time
import keyboard

fight = "assets/Button_Fight.png"
clear = "assets/stage_clear.png"
auto_battle = "assets/Button_Auto_Battle.png"

def pause():
    while True:
        if keyboard.read_key():
            break

def run_forging_bonds():
    bs = cr.find_bluestacks_app()
    if bs:
        pyautogui.moveTo(cr.locate_text(bs, 'Advanced'))
        pyautogui.click()
        print("Success: Clicked Advanced")
        
        print(" ")
        
        print("waiting for fight")
        pause()
        cr.locate_image(bs, fight)
        pyautogui.click()
        print("Success: Clicked Fight Loadout")

        print(" ")

        print("waiting for fight on map load")
        pause()
        cr.locate_image(bs, fight)
        pyautogui.click()
        print("Success: Clicked Fight on Map")
        
        pause()
        print("waiting for auto battle")
        cr.locate_image(bs, auto_battle)
        pyautogui.click()

        cr.locate_image(bs, clear)
    else:
        print("Error: Unable to find screen")

run_forging_bonds()