from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
# Cada componente que vaya a utilizar, debe ser importado 
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image



# Cada aplicación Kivy es una clase descendiente de la clase kivy.app.App
class HelloApp(App):
    
    # El método Build es el encargado de crear los controles visuales
    # que comprenden la ventana principal de la aplicación
    def build(self):
        # build() debe retornar el componente que contiene a todos los
        # demás controles de la ventana
        self.textinput= TextInput(hint_text="Escriba aquí su nombre: ")
        self.etiqueta= Label(text= "Aqui pondre tu nombre")
        contenedor = BoxLayout(orientation = "vertical")
        img= Image(source= "")
        contenedor.add_widget(self.textinput)
        contenedor.add_widget(self.etiqueta)
        btn= Button(text="Te saludo, hazme click")
        btn.bind(on_press = self.callback)
        btn.background_color = (1, 1, 0, 1)
        btn.color = (0, 0, 0, 1)  
        contenedor.add_widget(btn)
        return contenedor
    
    def callback(self, sender):
        self.etiqueta.text = f"{self.textinput.text}"
        self.etiqueta.color = (1, 1, 0, 1)  # amarillo
        self.etiqueta.background_color = (0, 0, 1, 1)  
        with self.etiqueta.canvas.before:
            Color(1, 0, 0, 1)  # rojo
            Rectangle(size=self.etiqueta.size, pos=self.etiqueta.pos)
        self.textinput.text= ""
        
# Para ejecutar la aplicación, se debe llamar al método run() de
# la clase principal descendiente de kivy.app.App
if __name__ == "__main__":
    HelloApp().run()
