from math import sin, pi
import matplotlib.pyplot as plt

SAMPLES = 1000
FRREQ = 400 #Hz
AMPLITUDE = 500

NUM_IN_ROW = 10


ex_file = open('output_wave_table.txt','w')

ex_file.write('{\n    ')

points = []

for i in range(SAMPLES):
    sine_value = int(sin(2 * pi * FRREQ / 48000 * i) * AMPLITUDE)
    points.append(sine_value)
    ex_file.write(f"{sine_value}, {sine_value}")
	
    if i != SAMPLES - 1:
        ex_file.write(", ")

    if (i + 1) % NUM_IN_ROW == 0:
            ex_file.write('\n    ')

ex_file.write('\n}')
ex_file.close()
plt.plot(points)
plt.show()

