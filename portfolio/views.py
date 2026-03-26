from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Proyecto

def index(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'portfolio/index.html', {'proyectos': proyectos})

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')
        
        try:
            send_mail(
                f'Contacto desde portfolio: {asunto}',
                f'Nombre: {nombre}\nEmail: {email}\n\nMensaje:\n{mensaje}',
                email,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            messages.success(request, f'¡Gracias {nombre}! Tu mensaje fue enviado. Te responderé pronto.')
        except Exception as e:
            messages.error(request, f'Error al enviar: {e}')
        
        return redirect('index')
    
    return redirect('index')