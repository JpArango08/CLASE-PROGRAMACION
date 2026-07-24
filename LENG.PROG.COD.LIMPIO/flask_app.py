from flask import Flask, request, render_template

app = Flask(__name__) #Nombre del archivo actual que está

#Por cada ruta que vayamos a tener en el navegador creamos unas función en python

@app.route("/formulario") #Indica la ruta que llama a esta función
def hola():
    #Lo que la función retorne, llega en el cuerpo html al navegador
    nombre = request.args.get("nombre", "")
    edad = request.args.get("edad", "")
    futuro = request.args.get("futuro", "")
    mensaje = ""

    if nombre != "" and edad != "" and futuro != "":
        mensaje = f"""
        <h1 style="text-align:center; font-size:60px;">
            <strong><em>Hola, {nombre}, tienes {edad} años y quieres {futuro}</em></strong>
        </h1>
        """
    return f"""
    
    <h1 style="text-align:center; font-size:60px;">
        <strong><em>Hola mundo web!</em></strong>
    </h1>

    <form style="text-align:center;">

        <h2 style="font-size:40px;">
            <strong><em>Ingresa tu nombre:</em></strong>
        </h2>

        <input 
            type="text" 
            name="nombre"
            placeholder="Escribe aquí tu nombre"
            style="font-size:25px; padding:10px;"
        >
        <input 
            type="text" 
            name="edad"
            placeholder="Tu edad"
            style="font-size:25px; padding:10px;"
        >
        <input 
            type="text" 
            name="futuro"
            placeholder="Escribe aquí sobre tu futuro"
            style="font-size:25px; padding:10px;"
        >

        <br><br>

        <button style="font-size:20px;">
            Enviar
        </button>

    </form>

    <h1 style="text-align:center; font-size:20px;">
        <strong><em>{mensaje}</em></strong>
    </h1>

    """
#Iniciar la app flask
app.run() #En la terminal crea una web con un servidor que muestra lo que escribí