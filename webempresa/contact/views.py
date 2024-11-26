from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.urls import reverse
from .forms import ContactForm
from webempresa.settings import EMAIL_HOST_USER

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Obtener los datos del formulario
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            # Crear el correo electrónico
            email_message = EmailMessage(
                subject="Tesis: Nuevo mensaje de contacto",  # Asunto
                body=f"De {name} <{email}>\n\nEscribió:\n\n{content}",  # Cuerpo
                from_email=EMAIL_HOST_USER,  # Email de origen
                to=["1cnachosanchez@gmail.com"],  # Cambia por el email destino
                reply_to=[email]  # Email de respuesta
            )

            try:
                email_message.send()  # Intentar enviar el correo
                # Redireccionar a éxito
                return redirect(reverse('contact') + "?ok")
            except:
                # Redireccionar a fallo
                return redirect(reverse('contact') + "?fail")
    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {"form": form})


    