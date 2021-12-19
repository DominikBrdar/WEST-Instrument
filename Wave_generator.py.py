from math import sin, pi

SAMPLES = 1000
FRREQ = 400 #Hz
AMPLITUDE = 500

NUM_IN_ROW = 10


ex_file = open('output_wave_table.txt','w')

ex_file.write('{\n    ')

for i in range(SAMPLES):
    sine_value = abs(int(sin(2 * pi * FRREQ / 48000 * i) * AMPLITUDE))

    ex_file.write(f"{sine_value}, {sine_value}")

    if i != SAMPLES - 1:
        ex_file.write(", ")

    if (i + 1) % NUM_IN_ROW == 0:
            ex_file.write('\n    ')

ex_file.write('\n}')
ex_file.close()

