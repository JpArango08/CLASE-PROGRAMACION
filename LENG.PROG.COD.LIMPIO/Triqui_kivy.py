from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
# Cada componente que vaya a utilizar, debe ser importado 
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.uix.popup import Popup

class TriquiApp(App):

    def build(self):
        tablero = BoxLayout(orientation="vertical")
        self.casillas = []
        for fila in range(3):
            fila_layout = BoxLayout()
            for i in range(3):
                casilla = Button(text="")
                fila_layout.add_widget(casilla)
                casilla.bind(on_press=self.callback)
                self.casillas.append(casilla)
            tablero.add_widget(fila_layout)
        self.turno = True
        self.contador_jugado = 0
        return tablero

    def mostrar_notificacion(self, mensaje, segundos=1):
        popup = Popup(
            title="",
            content=Label(text=mensaje),
            size_hint=(0.6, 0.2),
            auto_dismiss=True
        )
        popup.open()
        Clock.schedule_once(lambda dt: popup.dismiss(), segundos)

    def callback(self, sender):
        if self.contador_jugado == 9:
            for casilla in self.casillas:
                casilla.text = ""
                casilla.background_normal = 'atlas://data/images/defaulttheme/button'
                casilla.background_color = (1, 1, 1, 1)
            self.contador_jugado = 0
            return
        if sender.text != "":
            self.mostrar_notificacion("¡Ya jugaste ahí!")
            return
        if self.turno:
            sender.text = "X"
            self.turno = False
            sender.background_color = (0.4, 0.7, 1, 1)
        else:
            sender.text = "O"
            self.turno = True
            sender.background_color = (1, 0, 0, 1)
        self.contador_jugado += 1


if __name__ == "__main__":
    TriquiApp().run()
