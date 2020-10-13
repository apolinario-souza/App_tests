from kivy.app import App
from kivy.uix.button import Button
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import smtplib
fromaddr = "mayemail1988@gmail.com"
toaddrs  = "edf.tercio@hotmail.com"
msg = "Fala Guilherme, Oh teste do App!"




username = "mayemail1988@gmail.com"
password = "tercioapolinario"
server = smtplib.SMTP('smtp.gmail.com:587')



def callback(instance):     
     server.starttls()
     server.login(username,password)    
     server.sendmail(fromaddr, toaddrs, msg)
     server.quit()

class TestApp(App):
    def build(self):
        b=Button(text='press me')
        b.bind(on_press=callback)
        return b    

if __name__ == '__main__':
    TestApp().run()
    
    

