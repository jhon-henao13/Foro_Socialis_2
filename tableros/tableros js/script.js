// formulario
function crearFormulario() {
  var formulario = document.getElementById("formulario");

  if (formulario.style.display === "none") {
    formulario.style.display = "block";
  } else {
    formulario.style.display = "none";
  }
}

  

// footer
window.addEventListener("scroll", function() {
    var alturaPagina = document.documentElement.scrollHeight;
    var alturaViewport = window.innerHeight;
    var posicionActual = window.pageYOffset || document.documentElement.scrollTop;
    var posicionFinal = alturaPagina - alturaViewport;
    
    if (posicionActual >= posicionFinal) {
      document.querySelector(".container").classList.remove("oculto");
    } else {
      document.querySelector(".container").classList.add("oculto");
    }
  });

// Python enlace
  var foro1Boton = document.getElementById("foro1-boton");
foro1Boton.addEventListener("click", function() {
  crear_publicacion(1); // el número 1 es el ID del foro correspondiente
});

var foro2Boton = document.getElementById("foro2-boton");
foro2Boton.addEventListener("click", function() {
  crear_publicacion(2); // el número 2 es el ID del foro correspondiente
});

// y así sucesivamente para cada foro

  