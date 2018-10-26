# Python-kivy-desktop-app

In order to control the consumption of home electrical energy, this project allows the vision of energy flow in real time in order to minimize energy consumption costs:
    The first phase starts with the acquisition of current values ​​in real time through **ACS712** current sensor then these values ​​are processed by the **Arduino Uno board** and are sent to the central Arduino board through **two Xbee modules**, one is configured as end_device transmitter and the other receiver configured as coordinator. The central Arduino Uno board processes the current values ​​and calculates the energy and power consumed, all these values ​​are sent to the **Thingspeak platform** through an **esp8266 wifi module**. Then, the visualization of the data can be realized either through the Thingspeak server, or via the **Android Thingview application**, or via a **Python desktop application**.
 In this part of the project we created a desktop application using **Kivy**
## What is kivy    
Kivy is a complete framework for creating new interfaces like multitouch applications. Developed in **Python / Cython / OpenGL ES 2** and under LGPL license, this Framework has the ability to run on **Windows, MacOSX, Linux, Android (iOS in development)**.
## How to Run the Application
once downloading the zip file from the repository https://github.com/fethibch/Python-kivy-desktop-app.git 
* download Python3.6
* with ``pip install`` from the command line download all packages needed for the application
* install kivy https://kivy.org/doc/stable/installation/installation-windows.html
* **pip install httplib2** for the HTTP communication with the cloud server
* **pip install  serial** for the communication with the arduino board throw serial port
* **pip install  numpy , pip install  matplotlib ,  pip install drawnow** for plotting the charts
```
if the application doesn't run log into <<main.py>> and download packages missed from the import session
```
for the simulation plug an arduino board in the desktop and send random float values in the serial monitor
```
* In the file main.py you will find this instruction arduinoData = serial.Serial('com10', 9600)
in my case the arduino board in plugged on port10 and the baud rate is 9600,so make the necessary changes
```
**the application will run properly now**
## Screenshots of Demo

