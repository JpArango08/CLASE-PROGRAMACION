from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
# Cada componente que vaya a utilizar, debe ser importado 
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image

class TriquiApp( App ):

    def build(self):
        tablero = BoxLayout(orientation= "vertical")
        self.casillas = []
        for fila in range(3):
            fila= BoxLayout()
            for i in range(3):
                casilla= Button(text= "")
                fila.add_widget(casilla)
                casilla.bind(on_press = self.callback)
                self.casillas.append(casilla)
            tablero.add_widget(fila)
        self.turno=True
        self.contador_jugado= 0
        return tablero
        
    def callback(self, sender):
        if self.contador_jugado == 9:
            for casilla in self.casillas:
                casilla.text= ""
                casilla.background_normal = 'atlas://data/images/defaulttheme/button'
                casilla.background_color = (1, 1, 1, 1)
            self.contador_jugado= 0
            return
        if sender.text != "":
            return
        if self.turno:
            sender.text= "X"
            self.turno= False
            sender.background_color = (0.4, 0.7, 1, 1)
        else:
            sender.text= "O"
            self.turno= True
            sender.background_color = (1, 0, 0, 1)
        self.contador_jugado += 1
            
if __name__ == "__main__":
    TriquiApp().run()
