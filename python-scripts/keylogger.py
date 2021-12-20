from pynput import keyboard
import serial
from serial.tools.list_ports import comports

pressed = []

def on_press(key):
    global pressed
    if key not in pressed:
        pressed.append(key)
        try:
            #print('p{0}'.format(key))
            ser.write("p{0}".format(key.char).encode())
        except AttributeError:
            print('special key {0} pressed'.format(key))

def on_release(key):
    global pressed
    if key in pressed:
        pressed.remove(key)
        #print('r{0}'.format(key))
        ser.write('r{0}'.format(key.char).encode())
        if key == keyboard.Key.esc: # Stop listener
            return False

if __name__ == "__main__":
    print("Odaberi usb port:")
    allPorts = comports()
    for i in range (len(allPorts)):
        print(str(i) + " " + allPorts[i].device)
    portPath = int(input())
    ser = serial.Serial(allPorts[portPath].device)
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    print("connected to " + allPorts[i].device)
    while(True):
        r = 1
