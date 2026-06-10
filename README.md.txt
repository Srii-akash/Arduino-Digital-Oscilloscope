# Arduino Digital Oscilloscope

A simple Digital Storage Oscilloscope (DSO) built using an Arduino Uno, an LDR sensor, and Python. The project captures real-time analog sensor data from the Arduino through serial communication and visualizes it as a live waveform on a computer, similar to a traditional CRO (Cathode Ray Oscilloscope).

---

## Project Overview

This project demonstrates the complete workflow of:

* Analog signal acquisition using Arduino ADC
* Serial communication between Arduino and Python
* Real-time data visualization
* Basic digital oscilloscope concepts
* Sensor interfacing and signal monitoring

The system reads analog values from an LDR-based voltage divider circuit, transmits the sampled data over USB serial communication, and displays the waveform on a computer using Python.

---

## Features

* Real-time waveform display
* Live serial communication between Arduino and Python
* Analog signal acquisition using Arduino ADC
* Continuous waveform updates
* Beginner-friendly implementation
* Low-cost hardware setup
* Easily extendable to other sensors

---

## Hardware Components

| Component                      | Quantity    |
| ------------------------------ | ----------- |
| Arduino Uno/Nano               | 1           |
| LDR (Light Dependent Resistor) | 1           |
| 10kΩ Resistor                  | 1           |
| Breadboard                     | 1           |
| Jumper Wires                   | As Required |
| USB Cable                      | 1           |

---

## Software Requirements

### Arduino Side

* Arduino IDE

### Python Side

Install required libraries:

```bash
pip install pyserial pyqtgraph pyqt5 numpy
```

---

## Circuit Diagram

### Voltage Divider Configuration

```text
5V
 |
[LDR]
 |
 +------ A0
 |
[10kΩ]
 |
GND
```

The LDR and resistor form a voltage divider.

As light intensity changes:

* LDR resistance changes
* Voltage at A0 changes
* Arduino measures this voltage using its ADC

---

## Working Principle

### Step 1: Signal Acquisition

The LDR senses ambient light.

Changes in light intensity produce changes in voltage across the voltage divider.

### Step 2: Analog-to-Digital Conversion

Arduino reads the voltage using:

```cpp
analogRead(A0);
```

The ADC converts the analog voltage into a digital value between:

```text
0 – 1023
```

### Step 3: Serial Transmission

Arduino sends the ADC values to the computer using UART serial communication:

```cpp
Serial.println(sensorValue);
```

### Step 4: Data Reception

Python receives the incoming serial data using the PySerial library.

### Step 5: Waveform Visualization

PyQtGraph continuously plots incoming samples, creating a live oscilloscope-like display.

---

## System Architecture

```text
LDR Sensor
     │
     ▼
Voltage Divider
     │
     ▼
Arduino ADC
     │
     ▼
USB Serial Communication
     │
     ▼
Python (PySerial)
     │
     ▼
PyQtGraph
     │
     ▼
Live Waveform Display
```

---

## Arduino Code

```cpp
void setup()
{
    Serial.begin(115200);
}

void loop()
{
    int value = analogRead(A0);

    Serial.println(value);

    delay(10);
}
```

---

## Python Code

```python
import serial
import pyqtgraph as pg
from pyqtgraph.Qt import QtWidgets
from collections import deque

ser = serial.Serial('COM3', 115200)

app = QtWidgets.QApplication([])

win = pg.GraphicsLayoutWidget(show=True)
win.setWindowTitle("Arduino Digital Oscilloscope")

plot = win.addPlot()
curve = plot.plot()

buffer = deque([0] * 500, maxlen=500)

def update():
    while ser.in_waiting:
        try:
            value = int(ser.readline().decode().strip())
            buffer.append(value)
        except:
            pass

    curve.setData(list(buffer))

timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(20)

app.exec()
```

---

## Sample Output

### Circuit Setup

![Circuit Diagram](circuit_diagram.png)

### Oscilloscope Display

![Waveform Output](output_waveform.png)

---

## Project Structure

```text
Arduino-Digital-Oscilloscope/
│
├── README.md
├── oscilloscope.py
├── oscilloscope.ino
├── circuit_diagram.png
└── output_waveform.png
```

---

## Applications

* Sensor signal monitoring
* Educational electronics experiments
* ADC visualization
* Embedded systems learning
* Real-time data acquisition
* Basic signal analysis

---

## Concepts Learned

This project helped in understanding:

* Embedded systems fundamentals
* Arduino programming
* Analog-to-Digital Conversion (ADC)
* Serial Communication (UART)
* Python programming
* Real-time plotting
* Signal acquisition
* Digital Storage Oscilloscope (DSO) fundamentals

---

## Future Improvements

Potential upgrades include:

* Voltage scaling (V/div)
* Time scaling (ms/div)
* Trigger functionality
* RMS voltage calculation
* Peak-to-Peak voltage measurement
* Frequency measurement
* FFT Spectrum Analyzer
* Multi-channel support
* Data logging to CSV
* GUI controls

---

## Results

The developed system successfully acquires analog sensor data from an Arduino and visualizes it in real time using Python. The project demonstrates a low-cost implementation of a basic Digital Storage Oscilloscope and provides a foundation for more advanced signal processing and instrumentation projects.

---

## Author

**Sri**

A beginner embedded systems and Python project developed to explore sensor interfacing, serial communication, and real-time waveform visualization.
