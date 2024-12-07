import pyautogui as pyauto
import os
import time
from AppOpener import open

screenWidth, screenHeight = pyauto.size()
posX, posY = screenWidth/4, screenHeight/2
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Build\\Flappy_Man.exe"
abs_file_path = os.path.join(script_dir, rel_path)

def openGame():
    os.startfile(abs_file_path)


def Hit():
#    pyauto.moveTo(posX, posY)
    pyauto.press("enter")
    
def Move():
    time.sleep(2)
    pyauto.moveTo(posX, posY)
    pyauto.leftClick()

if __name__ == "__main__":
    openGame()
    


