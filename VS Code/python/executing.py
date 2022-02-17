from time import sleep
import keyboard

sleep(3)

i = 0

while i < 5:
    keyboard.press_and_release('windows+r')
    sleep(0.05)
    keyboard.write("cmd")
    sleep(0.05)
    keyboard.press_and_release('enter')
    sleep(0.5)
    keyboard.write('cd OneDrive')
    sleep(0.05)
    keyboard.press_and_release('enter')
    sleep(0.05)
    keyboard.write('cd Documentos')
    sleep(0.05)
    keyboard.press_and_release('enter')
    sleep(0.05)
    keyboard.write('cd Código')
    sleep(0.05)
    keyboard.press_and_release('enter')
    sleep(0.05)
    keyboard.write('cd VS Code')
    sleep(0.05)
    keyboard.press_and_release('enter')
    sleep(0.05)
    keyboard.write('python apsd.py')
    sleep(0.05)
    keyboard.press_and_release('enter')
    sleep(0.5)
    keyboard.write('Camilo')
    sleep(0.05)
    keyboard.press_and_release('enter')
    sleep(0.5)
    keyboard.write('exit')
    sleep(0.05)
    keyboard.press_and_release('enter')
    sleep(0.5)
    i += 1
s = 2


