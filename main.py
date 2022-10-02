from ast import While
from cgitb import text
from tkinter import Button, Widget
import kivy
from kivy.app import App 
from kivy.uix.button import Label 
# from kvdroid.tools.contact import get_contact_details
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from plyer import gps
from geopy.geocoders import Nominatim
from kivy.properties import StringProperty

#Telefon Kişi Verisi Çekme
'''a = get_contact_details("phone_book") # gets a dictionary of all contact both contact name and phone mumbers
b = get_contact_details("names") # gets a list of all contact names
c = get_contact_details("mobile_no") # gets a list of all contact phone numbers
'''

class BoxLayoutExample(BoxLayout):
    '''def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 =Button(text="A")
        self.add_widget(b1)
       ''' 
    pass

class Rotaci(App):
    
    def on_start(self):
        gps.configure(on_location =self.on_gps_location)
        loc = gps.start(minTime=3000)
        loc_text = StringProperty(loc)
        
    '''def on_gps_location(self,**kwargs):
        kwargs["lat"] = 10.0
        kwargs["lon"] = 10.0
        print(kwargs)
    '''
if __name__ =="__main__":
    Rotaci().run()
