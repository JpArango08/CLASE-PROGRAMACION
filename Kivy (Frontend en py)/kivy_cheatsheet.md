# Kivy Cheat Sheet

## Básico

-   from kivy.app import App
-   from kivy.uix.label import Label

## Crear App

class MiApp(App): def build(self): return Label(text="Hola mundo")

MiApp().run()

## Propiedades de Label

-   text="Texto"
-   font_size=30
-   color=(1,0,0,1)

## Tamaño y Posición

-   size = (200,100)
-   size_hint = (None,None)
-   pos = (100,100)
-   pos_hint = {"center_x":0.5,"center_y":0.5}

## Alineación

-   halign="center"
-   valign="top"
-   text_size = label.size

## Botones

from kivy.uix.button import Button

btn = Button(text="Click")

## Eventos

btn.bind(on_press=funcion)

## Layouts

-   BoxLayout
-   GridLayout
-   FloatLayout

## Canvas (fondo)

from kivy.graphics import Color, Rectangle

with widget.canvas.before: Color(1,0,0,1) Rectangle(size=widget.size,
pos=widget.pos)

## Fuentes

label.font_name = "ruta.ttf"

## Ejecutar

python main.py
