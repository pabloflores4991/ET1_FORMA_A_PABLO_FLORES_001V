$(function()
{
    $("#formulario").validate({
        rules:{
            user:"required",
            pass2:"required",
        },
        messages:{
            user:{
                required:'Ingresa tu usuario',
            },
            pass2:{
                required:'Ingresa tu contraseña',
            }
            
            
        }
    });
}
    );



$(function() 
{
  $("#mi-formulario").validate({
       rules: {
              nombre: true,
              email: {
                  required: true,
                  email: true
              },
              password: "required",
              fono: "required",
              fecha: "required",
              password2: {
                  required: true,
                  equalTo: "#password",
              },
              terminos:"required",
              
          }, //rules
      messages: {
          nombre:{
              required:'Ingresa tu nombre y apellido',
              minlength:'Caracteres insuficientes',
              maxlength:'Demasiados caracteres'
          },
          user2:{
              required:'Ingresa tu nombre de usuario',
              minlength:'Caracteres insuficientes',
          },
          email: {
              required: 'Ingresa tu correo electrónico',
              email: 'Formato de correo no válido'
          },
          password: {
              required: 'Ingresa una contraseña',
              minlength: 'Caracteres insuficientes'
          },
          fono:{
              required: 'Ingrese un número de celular',
              minlength: 'Cantidad de digitos insuficiente'
          },
          fecha:{
              required: 'Seleccione una fecha válida',
              min: 'Fecha no corresponde'
          },
          password2: {
              required: 'Reingresa la contraseña',
              equalTo: 'Las contraseñas ingresadas no coinciden',
              minlength: 'Caracteres insuficientes'

          },
          terminos:{
              required:'debe aceptar los terminos y condiciones'
          }
      }//messages
  }); //$('#mi-formulario').validate
}); //function


function CambiarMayusculas()
{
    var a = document.getElementById("nombre");
    a.value = a.value.toUpperCase();
}
function CambiarMayusculas()
{
    var a = document.getElementById("email");
    a.value = a.value.toUpperCase();
}

function CambiaColorB(a)
{
    a.style.background = "red";
}



function focusFunction(id) {
    // Focus = Changes the background color of input to yellow
    document.getElementById(id).style.background = "white";
  }
  
  function blurFunction(id) {
    // No focus = Changes the background color of input to red
    document.getElementById(id).style.background = "rgba(155, 30, 30, 0.1)";
  }




