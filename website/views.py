from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.
def index(request):
    return render(
        request,
        'website/index.html',
        {

        }
        )

def contact(request):

    if request.method == "POST":
        message_name = request.POST['name']
        message_email = request.POST['email']
        message_subject = request.POST['subject']
        message_message = request.POST['message']

        send_mail(
            f'Appointment request for {message_name}', # subject
            message_message, # message
            message_email, # from email
            ['admin@email.com'], # to email

        )

        return render(
            request,
            'website/contact.html',
            {
                'message_name': message_name,
            }
            )

    else:
        return render(
        request,
        'website/contact.html',
        {

        }
        )