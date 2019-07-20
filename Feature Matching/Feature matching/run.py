from kivy.app import App
from kivy.uix.button import Button

from subprocess import call


def callback(instance):
        print("Initiating <%s>"% instance.text)
        call(["python","Subtractor6.py"])

def stopit():
        print("The instance is stopped")
        return

btn1 = Button(text="Start")
btn1.bind(on_press=callback)
btn2 = Button(text="Stop")
btn2.bind(on_press=stopit)

