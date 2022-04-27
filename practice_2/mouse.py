from pynput import mouse, keyboard
import time

# using ubuntu
text = 'Ali Rahmani'

m = mouse.Controller()
k = keyboard.Controller()

# right click to open the context menu
m.position = (300, 300)
m.click(mouse.Button.right)

# click on the "New Folder" item
m.move(0, 20)
m.click(mouse.Button.left)

# wait for a second, click on the text box & press keys to write my name
time.sleep(1)
m.move(550, 220)
m.click(mouse.Button.left)

for c in text:
    time.sleep(.4)
    k.press(c)
    time.sleep(0.15)
    k.release(c)
