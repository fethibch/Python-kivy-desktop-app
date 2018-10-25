import kivy
kivy.require("1.10.0") 
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.pagelayout import PageLayout
from kivy.base import runTouchApp
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import NumericProperty
import httplib2
import json
from urllib.request import urlopen
import urllib.request
import serial
import numpy  
import matplotlib.pyplot as plt 
from drawnow import *

arduinoData = serial.Serial('com10', 9600)

class ScreenOne(Screen):
    pass
    
    	
class ScreenTwo(Screen):

    def current(self):
        while (arduinoData.inWaiting()==0): #Wait here until there is data
            pass
        arduinoString = arduinoData.readline()
        c= arduinoString.decode('utf-8')
        self.display.text=c
        print(c)
    def a(self):
        current= []
        plt.ion()
        cnt=0
        def makeFig(): #Create a function that makes our desired plot
            plt.ylim(0,10)                                 #Set y min and max values
            plt.title('real time current ')                 #Plot the title
            plt.grid(True)                                  #Turn the grid on
            plt.ylabel('current')                            #Set ylabels
            plt.plot(current, 'ro-', label='Ampere mA')       #plot the temperature
            plt.legend(loc='upper left')                    #plot the legend
            
        while True: # While loop that loops forever
            while (arduinoData.inWaiting()==0): #Wait here until there is data
                pass #do nothing
            arduinoString = arduinoData.readline() #read the line of text from the serial port
            c = float(arduinoString)            #Convert first element to floating number and put in temp
            current.append(c)                     #Build our tempF array by appending temp readings
            drawnow(makeFig)                       #Call drawnow to update our live graph
            plt.pause(.000001)                     #Pause Briefly. Important to keep drawnow from crashing
            cnt=cnt+1
            print(c)
    
            if(cnt>50):                            #If you have 50 or more points, delete the first one from the array
                current.pop(0)                       #This allows us to just see the last 50 data points

            
    
class ScreenThree(Screen):
   
    def energy(self):
        READ_API_KEY='9BRZU34V8EU1O0JW'
        CHANNEL_ID= '431348'
        TS = urllib.request.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                               % (CHANNEL_ID,READ_API_KEY))
        response = TS.read()
        data=json.loads(response.decode('utf-8'))
        a = data['created_at']
        b = data['field1']
        c = data['field2']
        d = data['field3']
        self.ener.text=c
   
class ScreenFour(Screen):
    pass
class ScreenFive(Screen):
    def s1(self):
        arduinoData.write('a'.encode('ascii'))
        self.ss.text="scenario 1 en cours.."
        self.sss.text=" "
        self.ssss.text=" "
    def s2(self):
        arduinoData.write('b'.encode('ascii'))
        self.sss.text="scenario 2 en cours.."
        self.ss.text=" "
        self.ssss.text=" "
    def s3(self):
        arduinoData.write('c'.encode('ascii'))
        self.ssss.text="scenario 3 en cours.."
        self.sss.text=" "
        self.ss.text=" "
class ScreenManagement(ScreenManager):
    pass

my_frame = Builder.load_file("main.kv")

class mainApp(App):
    def build(self):
        return my_frame
 
mainApp().run()
