from flask import Flask, render_template, jsonify, request

app = Flask(__name__) #Objeto que representa nuestro servidor

@app.route("/") #Este representa la pag principal, Cuando alguien entre a /, ejecuta la funcion que viene debajo
def inicio():
    return render_template("index.html") #Le decimos a flask busca dentro de templates y envialo al navegador

@app.route("/compras") 
def compras():
    return "Aquí veremos las compras"

@app.route("/api/hola") # Crea una ruta api  para comunicar el front con el back
def api_hola():
    return jsonify({
        "mensaje": "Hola desde flask"
    })
"""
Hasta ahora teníamos:

@app.route("/api/devolucion")

Eso utiliza GET por defecto.

GET normalmente significa:

"Quiero consultar información."

POST normalmente significa:

"Quiero enviar información al servidor."
"""

@app.route("/api/devolucion", methods=["POST"]) # Cuando recibas una petición HTTP POST dirigida a /api/devolucion, ejecuta esta función.
def api_devolucion():

    datos = request.json

    codigo = datos["codigo"]
    correo = datos["correo"]

    if codigo == "DEV-123" and correo == "juan@gmail.com":
        return jsonify({
            "codigo": codigo,
            "correo": correo,
            "estado": "aprobada",
            "mensaje": "La devolución fue encontrada"
        })

    else:
        return jsonify({
            "codigo": codigo,
            "correo": correo,
            "estado": "no encontrada",
            "mensaje": "No existe una devolución con esos datos"
        })


app.run(debug=True) #Esto inicia nuestro servidores