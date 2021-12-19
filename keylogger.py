from pynput import keyboard
import serial

pressed = []
#portPath = '/dev/serial0'
#ser = serial.Serial(portPath)

def on_press(key):
    global pressed
    if key not in pressed:
        pressed.append(key)
        try:
            print('p{0}'.format(key))
            #ser.write('p{0}'.format(key)).encode()
        except AttributeError:
            print('special key {0} pressed'.format(key))

def on_release(key):
    global pressed
    if key in pressed:
        pressed.remove(key)
        print('r{0}'.format(key))
        #ser.write('r{0}'.format(key)).encode()
        if key == keyboard.Key.esc: # Stop listener
            return False

if __name__ == "__main__":
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
            listener.join()
    while(True):
        r = 1
