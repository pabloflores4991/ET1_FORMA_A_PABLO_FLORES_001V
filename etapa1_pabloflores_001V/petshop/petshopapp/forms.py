from django import forms 
from django.forms import ModelForm, widgets
from .models import Mascota, TipoMascota, Provedor1
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget


class MascotaForm(ModelForm): 
    
    class Meta: 
        model = Mascota 
        fields = ['nombreMascota', 'nombreDueño', 'raza', 'sexo', 'edad', 'TipoMascota','imagen' ]
    

        labels={
            'nombreMascota': 'Nombre Mascota',
            'nombreDueño': 'Nombre Dueño', 
            'morazadelo': 'raza o especie', 
            'sexo': 'Sexo Mascota',
            'edad': 'edad Mascota',
            'TipoMascota': 'Seleccione tipo de mascota',
            
        }


        widgets={

            'nombreMascota': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'nombreMascota', 
                    'id': 'nombreMascota',
                
                }
            ),
            'nombreDueño': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'nombreDueño', 
                    'id': 'nombreDueño'
                }
            ),
            'raza': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'raza', 
                    'id': 'raza'
                }
            ), 
            'sexo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'sexo', 
                    'id': 'sexo'
                }
            ), 
            'edad': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'edad', 
                    'id': 'edad'
                }
            ), 

            'TipoMascota': forms.Select(
                attrs={
                    'class': 'form-control', 
                    'id':'TipoMascota'
                }
            ),
        }



class ProvedorForm(ModelForm): 
    
    class Meta: 
        model = Provedor1
        fields = ['Run', 'NombreCompleto', 'Pais', 'Ciudad', 'Comuna', 'Direccion','Telefono',
        'Email','Moneda','imagen']
    

        labels={
            'Run': 'Ingrese su rut',
            'NombreCompleto': 'Ingrese nombre completo', 
            'Pais': 'Ingrese país', 
            'Ciudad': 'Ingrese ciudad',
            'Comuna': 'Ingrese comuna',
            'Direccion': 'Ingrese dirección',
            'Telefono': 'ingrese teléfono de contacto', 
            'Email': 'Ingrese correo electrónico',
            'Moneda': 'Ingrese tipo de moneda de pago',
            
            
        }

        widgets={

            'Run': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese rut', 
                    'id': 'Run',
                
                }
            ),
            'NombreCompleto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre completo', 
                    'id': 'NombreCompleto'
                }
            ),
            'Pais': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese pais', 
                    'id': 'Pais'
                }
            ), 
            'Ciudad': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese ciudad', 
                    'id': 'Ciudad'
                }
            ), 
            'Comuna': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese comuna', 
                    'id': 'Comuna'
                }
            ), 
            'Direccion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese direccion', 
                    'id': 'Direccion'
                }
            ), 
            'Telefono': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese telefono', 
                    'id': 'Telefono'
                }
            ), 
            'Email': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Email', 
                    'id': 'Email'
                }
            ), 


            
        }