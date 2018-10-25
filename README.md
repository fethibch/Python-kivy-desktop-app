# Python-kivy-desktop-app

In order to control the consumption of home electrical energy, this project allows the vision of energy flow in real time in order to minimize energy consumption costs:
    The first phase starts with the acquisition of current values ​​in real time through **ACS712** current sensor then these values ​​are processed by the **Arduino Uno board** and are sent to the central Arduino board through **two Xbee modules**, one is configured as end_device transmitter and the other receiver configured as coordinator. The central Arduino Uno board processes the current values ​​and calculates the energy and power consumed, all these values ​​are sent to the **Thingspeak platform** through an **esp8266 wifi module**. Then, the visualization of the data can be realized either through the Thingspeak server, or via the **Android Thingview application**, or via a **Python desktop application**.
    
