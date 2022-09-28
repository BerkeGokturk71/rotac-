import kivy
from kivy.app import App 
from kivy.uix.button import Label 
from kvdroid.tools.contact import get_contact_details

a = get_contact_details("phone_book") # gets a dictionary of all contact both contact name and phone mumbers
b = get_contact_details("names") # gets a list of all contact names
c = get_contact_details("mobile_no") # gets a list of all contact phone numbers
class HelloKivy(App): 

	
	def build(self): 

		
		return Label(text =a+b+c) 

helloKivy = HelloKivy() 
helloKivy.run() 
