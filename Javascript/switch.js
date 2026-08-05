const rol = "Admin"
switch (rol) {
    case "Admin":
        console.log("Acceso total")
        break
    case "Editor":
        console.log("Puede editar solo contenido")
        break
    case "Usuario":
        console.log("Solo lectura")
        break
    default:
        console.log("Rol no válido")
}