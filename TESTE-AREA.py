import pyautogui
import pydirectinput
import time

chat = 0
REGION2 = (214, 540, 64, 68)

pyautogui.keyDown('alt')

pyautogui.press('tab')

pyautogui.keyUp('alt')

time.sleep(3)


inicio = time.time()


pydirectinput.keyDown('ctrl')
pydirectinput.keyDown('q')
pydirectinput.keyUp('ctrl')
pydirectinput.keyUp('q')

time.sleep(2)

#CONFIRMAR SAIR
pydirectinput.press('enter')


fim = time.time()
print(fim-inicio)
