import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import deque

# Arduino COM Port
PORT = "COM5"
BAUD = 115200

ser = serial.Serial(PORT, BAUD, timeout=1)

# Store last 200 samples
data = deque([0] * 200, maxlen=200)

fig, ax = plt.subplots()
line, = ax.plot(data)

ax.set_title("Arduino Digital Oscilloscope")
ax.set_ylim(0, 1023)
ax.set_xlim(0, 200)
ax.set_ylabel("Sensor Value")
ax.set_xlabel("Samples")
ax.grid(True)

def update(frame):
    try:
        value = ser.readline().decode().strip()

        if value:
            data.append(int(value))

        line.set_ydata(data)

    except:
        pass

    return line,

ani = FuncAnimation(fig, update, interval=20)

plt.show()