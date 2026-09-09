// DOM es básicamente la representación que JavaScript tiene de nuestro HTML.

const codigo = document.getElementById("cod_devolucion"); // Busca en el HTML el elemento cuyo id sea cod_devolucion y guárdalo en la variable codigo.
const boton = document.getElementById("btn_consultar")
const correo = document.getElementById("correo_electronico")
const resultado = document.getElementById("resultado")
function imprimir(codigo, correo, resultado) {
    resultado.textContent = `codigo: ${codigo.value}, correo: ${correo.value}`
};


boton.addEventListener("click", function() {
    // fetch() es el mecanismo que utiliza el frontend para hacer una petición HTTP al backend.
    fetch("/api/devolucion", { // Hacer una petición con el backend a la dirrecion /api/devolucion
        method: "POST", // "Flask, aquí tienes información para que la proceses."
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ //Esto es un objeto de JavaScript que convertimos a JSON para enviarlo en la petición HTTP
            codigo: codigo.value,
            correo: correo.value
        })
    })
    .then(response => response.json()) //Luego de que python procese, js recibe la respuesta de flask y la recibe como JSON
    .then(data => { // data contiene, lo que retornó python
        resultado.textContent = `Codigo: ${data.codigo}, correo: ${data.correo} estado: ${data.estado}, mensaje: ${data.mensaje} `;
    });

});