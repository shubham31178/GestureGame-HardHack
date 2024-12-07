import pyautogui as pyauto

while True:
    posX, posY = pyauto.position()
    print('x', posX, 'y', posY)